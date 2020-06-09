import math
import numpy as np
import cv2
import tensorflow as tf
from util.depth import *
from util.object_dection import *
import time 
def selly_vision_img(model, img, point_cloud, max_dist, fix_dist):
    only_sidewalk = seg_predict(img.copy(),model)
    obj_frame, moving_object, fixed_object  = YOLO(img.copy())
    point = point_cloud.copy()
    point[200 :,:, 2][(point[200 :,:, 2] >5) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 2][(point[:,:, 2]<2)& (only_sidewalk[:,:,0] !=0)])
    point[200 :,:, 1][(point[200 :,:, 1] >3) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 1][(point[:,:, 1]<3)& (only_sidewalk[:,:,0] !=0)])
    #point[200 :,:, 0][(point[200 :,:, 0] ==np.inf) | (np.abs(point[200 :,:, 0])>2)] = np.mean(point[200:,:, 0][point[200:,:, 0]<2])
    
    point[:,:, 2][point[:,:, 2]==np.inf] = 40
    only_sidewalk[(point[:,:,1] < -3) |  (point[:,:,1] ==np.inf)] = 0  #일정 높이 이상 segmetation 오차 제거

    depth = point2dist(point)
    obstacle = np.ones_like(img)
    obstacle[only_sidewalk!=0] = 0
    
    angle = point.copy()
    angle[angle[:, :,2]==np.inf]=1
    angle = np.arctan((angle[:, :,0]/angle[:,:,2]
                            ))/np.pi * 180
    angle = angle[:,:, np.newaxis]
    angle= np.concatenate((angle,angle,angle) , axis = 2)

    for i in range(480):
        target = angle[:,i:i+1,:]
        angle_mean = np.mean(target[(target>-42) & (target<42)])
        target[np.abs(target - angle_mean)>3 ] = angle_mean
        
    moving_object_position, fixed_object_position =[] ,[]
    
    if len(moving_object):
        moving_object_position = object_angle(moving_object, angle.copy(), depth)
    if len(fixed_object):
        fixed_object_position = object_angle(fixed_object, angle.copy(), depth)
        
    for i in moving_object:
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 1
        
    for i in fixed_object:
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 1

    obstacle[(depth[:,:,0] > fix_dist) |(point[:,:,1] < -3) |  (point[:,:,1] ==np.inf)]=0 #일정 높이이상 장애물 제거
    obs_count={}
    oba = np.unique(np.round(angle[(obstacle!=0) & (obstacle<fix_dist)]), return_counts=True)
    for i, j in zip(oba[0],oba[1]):
        obs_count[i] = j
    for i in range(int(np.min(angle)), int(np.max(angle))):
        if not i in obs_count.keys():
            obs_count[i] = 0
      
    for i in moving_object_position:
        if i[2] < 7:
            for j in range(int(i[0]), int(i[1])+1, 1):
                if j in obs_count.keys():
                    obs_count[j] =9999
                    
    for i in fixed_object_position:
        if i[2] < 2:
            for j in range(int(i[0]), int(i[1])+1,1 ):
                if j in obs_count.keys():
                    obs_count[j] =9999
                    
    able_angle = sorted(obs_count.items(), key =  lambda x : (x[1], np.abs(x[1])))
    able_angle = np.array(able_angle)
    ang_dict = {}
    for i in able_angle[:,0]:
        value =np.round(np.mean(able_angle[:,1][(able_angle[:,0] >= -10+i) & (able_angle[:,0] <= +10+i)]))
        if value != np.nan:
            ang_dict[i] = value 
    able_angle = sorted(ang_dict.items(), key =  lambda x : (x[1], np.abs(x[0])))

    '''plt.imshow(obstacle)
    plt.title("move :"+str(max_dist)+ "M," + "fixed : "+str(fix_dist)+"M")
    plt.axis("off")'''
    return  able_angle

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
        try:
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
        except: 
            continue
    object_dist_array = np.array(object_dist_array)
    return object_dist_array

def object_dist(object_position, point_cloud, depth):
    object_dist_array = []
    for i in object_position:
        try:
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
        except: 
            continue
    object_dist_array = np.array(object_dist_array)
    return object_dist_array