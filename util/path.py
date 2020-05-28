import math
import numpy as np
import cv2
import tensorflow as tf
from util.angle import *
from util.depth import *
from util.object_dection import *
import time 

def selly_vision_img(model, img, point_cloud, max_dist, fix_dist, ANGLE, ANGLE_CLASS):
    only_sidewalk = seg_predict(img.copy(),model)
    obj_frame, moving_object, fixed_object  = YOLO(img.copy())
    point = point_cloud.copy()
    point[200 :,:, 2][(point[200 :,:, 2] >5) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 2][(point[:,:, 2]<2)& (only_sidewalk[:,:,0] !=0)])
    point[200 :,:, 1][(point[200 :,:, 1] >3) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 1][(point[:,:, 1]<3)& (only_sidewalk[:,:,0] !=0)])
    point[200 :,:, 0][(point[200 :,:, 0] ==np.inf) | (np.abs(point[200 :,:, 0])>2)] = np.mean(point[200:,:, 0][point[200:,:, 0]<2])
    
    point[:,:, 2][point[:,:, 2]==np.inf] = 40
    only_sidewalk[(point[:,:,1] < -3) |  (point[:,:,1] ==np.inf)] = 0  #일정 높이 이상 segmetation 오차 제거

    depth = point2dist(point)
    obstacle = np.ones_like(img)
    obstacle[only_sidewalk!=0] = 0

    moving_object_position, fixed_object_position =[] ,[]
    
    if len(moving_object):
        moving_object_position = object_dist(moving_object, point.copy(), depth)
        moving_object_position[:, :2] = object_angle(moving_object_position)
    if len(fixed_object):
        fixed_object_position = object_dist(fixed_object, point.copy(), depth)
        fixed_object_position[:, :2] = object_angle(fixed_object_position)
        
    for i in moving_object:
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0
    for i in fixed_object:
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0    
        
    obstacle[(point[:,:,1] < -3) |  (point[:,:,1] ==np.inf)]=0 #일정 높이이상 장애물 제거

    '''angle_max = int(np.max(angle[:,:,0][angle[:,:,0]< 45]))
    angle_min = int(np.min(angle[:,:,0]))
    able_angle = [ i for i in range(angle_min, angle_max, 1) ] 
    able_angle_dict = {}
    for i in moving_object_position:
        if i[2] < max_dist:
            for j in range(int(i[0])-1, int(i[1])+1, 1):
                if j in able_angle:
                    able_angle.remove(j)

    for i in fixed_object_position:
        if i[2] < fix_dist:
            for j in range(int(i[0])-1, int(i[1])+1,1 ):
                if j in able_angle:
                    able_angle.remove(j)

    for i in able_angle:
        obs_angle = obstacle[(angle > i-1) & (angle < i+1) & (obstacle!=0)].shape[0]
        able_angle_dict[i] = obs_angle
        '''
    
    return moving_object_position, fixed_object_position

def seg_predict(img, infer):
    '''
    1 ""bike_lane_normal", "sidewalk_asphalt", "sidewalk_urethane""
    2  "caution_zone_stairs", "caution_zone_manhole", "caution_zone_tree_zone", "caution_zone_grating", "caution_zone_repair_zone"]
    3"alley_crosswalk","roadway_crosswalk"
    4"braille_guide_blocks_normal", "braille_guide_blocks_damaged"
    5"roadway_normal","alley_normal","alley_speed_bump", "alley_damaged""
    6"sidewalk_blocks","sidewalk_cement" , "sidewalk_soil_stone", "sidewalk_damaged","sidewalk_other"
    '''
    frame = cv2.resize(img,(480,272))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame/=255
    #tensorrt model
    trt = infer(tf.convert_to_tensor(frame[tf.newaxis, ...]))
    trt = trt['conv2d_37'].numpy()
    pre = create_mask(trt).numpy()
    frame[((pre!=4) & (pre!=6) & (pre!=1)).all(axis=2)]=0
    frame = cv2.resize(frame,(480,270))

    return frame

def create_mask(pred_mask):
    pred_mask = tf.argmax(pred_mask, axis=-1)
    pred_mask = pred_mask[..., tf.newaxis]
    return pred_mask[0]   

def object_angle(object_position, angle, depth):
    object_dist_array = []
    for i in object_position:
        cen_x = (i[1][0]-i[0][0])//6
        cen_y = (i[1][1]-i[0][1])//6
        obj_depth = depth[i[0][1] + cen_y : i[1][1] -cen_y , i[0][0] + cen_x: i[1][0]-cen_x , :]
        obj_angle = angle[i[0][1] : i[1][1], i[0][0] : i[1][0], :]
        min_range = np.min(obj_depth)
        max_range = min_range + 0.5
        obj_depth = depth[i[0][1]: i[1][1] +1 , i[0][0]: i[1][0]+1 , :]
        angle_min =  np.round(np.min(obj_angle[obj_angle<45]),1)
        angle_max =  np.round(np.max(obj_angle[obj_angle<45]),1)
        object_dist_array.append([angle_min, angle_max, np.round(min_range,1)])
    object_dist_array = np.array(object_dist_array)
    return object_dist_array

def object_dist(object_position, point_cloud, depth):
    object_dist_array = []
    for i in object_position:
        cen_x = (i[1][0]-i[0][0])//6
        cen_y = (i[1][1]-i[0][1])//6
        obj_depth = depth[i[0][1] + cen_y : i[1][1] -cen_y , i[0][0] + cen_x: i[1][0]-cen_x , :]
        obj_position = point_cloud[i[0][1]: i[1][1] +1 , i[0][0]: i[1][0]+1 , :]
        min_range = np.min(obj_depth)
        max_range = min_range + 0.5
        obj_depth = depth[i[0][1]: i[1][1] +1 , i[0][0]: i[1][0]+1 , :]
        x_min =  np.round(np.min(obj_position[:,:, 0][(obj_depth[:,:, 2] >= min_range) & (obj_depth[:,:, 2] <= max_range)]),1)
        x_max =  np.round(np.max(obj_position[:,:, 0][(obj_depth[:,:, 2] >= min_range) & (obj_depth[:,:, 2] <= max_range)]),1)
        object_dist_array.append([x_min, x_max, np.round(min_range,1)])
    object_dist_array = np.array(object_dist_array)
    return object_dist_array