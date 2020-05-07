import math
import numpy as np
import cv2
import tensorflow as tf
from util.angle import *
from util.depth import *
from util.object_dection import *
import time 

def decision_path(obstacle_angle, ANGLE_CLASS):
    angle_dict = {}
    for i in range(1,ANGLE_CLASS+1):
        try:
            angle_dict[i] = len(obstacle_angle[obstacle_angle==i])
        except:
            angle_dict[i] = 0
    return angle_dict

def selly_vision_path(img, redundant_obstacle, fixed_object, moving_object, ANGLE_CLASS, ANGLE_DICT):
    redundant_obstacle = vision_angle(ANGLE_DICT, redundant_obstacle)
    path_dict_redundant = decision_path(redundant_obstacle, ANGLE_CLASS)
    angle_range = []
    center = (240, 270)

    for i in moving_object :
        angle = [ANGLE_DICT[str(i[0][1])+","+str(i[0][0])],  
            ANGLE_DICT[str(i[1][1])+","+str(i[1][0])], 
            ANGLE_DICT[str(i[0][1])+","+str(i[1][0])],
            ANGLE_DICT[str(i[1][1])+","+str(i[0][0])]]
        
        min = int(np.min(angle))
        max = int(np.max(angle))   
        temp = [j for j in range(min, max+1)]
        angle_range += temp

    for i in fixed_object :
        angle = [ANGLE_DICT[str(i[0][1])+","+str(i[0][0])],  
            ANGLE_DICT[str(i[1][1])+","+str(i[1][0])], 
            ANGLE_DICT[str(i[0][1])+","+str(i[1][0])],
            ANGLE_DICT[str(i[1][1])+","+str(i[0][0])]]

        min = int(np.min(angle))
        max = int(np.max(angle))   
        temp = [j for j in range(min, max+1)]
        angle_range += temp

    angle_range = set(angle_range)

    return_angle = []

    for i in range(ANGLE_CLASS):
        if path_dict_redundant[i+1] < 100 and not i in angle_range:
            x = 100 * math.cos(math.radians((180/ANGLE_CLASS)*i+ (180/ANGLE_CLASS)/2))
            y = 100 * math.sin(math.radians((180/ANGLE_CLASS)*i+ (180/ANGLE_CLASS)/2))
            return_angle.append((180/ANGLE_CLASS)*i)
            cv2.arrowedLine(img, center , (240+int(x),270-int(y)), (0,255,0), 3, tipLength=0.15 )
    
    return img, return_angle

def selly_vision_img(model, img, point_cloud, max_dist, fix_dist, ANGLE, ANGLE_CLASS):

    seg_img, only_sidewalk = seg_predict(img,model)
    depth = point2dist(point_cloud, 1/16)

    only_sidewalk_limited_dist = only_sidewalk.copy()
    only_sidewalk_limited_dist[(depth>max_dist)] = 0
    obstacle = img.copy()
    obstacle_depth = img.copy()

    obstacle_depth[(depth>max_dist)] = 0
    obj_frame, moving_object, _  = YOLO(obstacle_depth)
    obstacle[~((only_sidewalk ==0) & (obstacle_depth!=0))] = 0
    redundant_obstacle = obstacle.copy()


    obstacle_depth[(depth>fix_dist)] = 0
    redundant_obstacle[(depth>fix_dist)] = 0
    _, _, fixed_object  = YOLO(obstacle_depth)

    for i in moving_object:
        redundant_obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0
    for i in fixed_object:
        redundant_obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0

    selly_vision, angle = selly_vision_path(img.copy(), redundant_obstacle.copy(), fixed_object, moving_object, ANGLE_CLASS, ANGLE)

    return selly_vision, angle

def seg_predict(img, model):
    frame = cv2.resize(img,(480,272))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame/=255
    pre = model.predict(frame[tf.newaxis, ...])
    pre = create_mask(pre).numpy()
    frame2 = frame/2
    frame2[(pre==1).all(axis=2)] += [0, 0, 0] #""bike_lane_normal", "sidewalk_asphalt", "sidewalk_urethane""
    frame2[(pre==2).all(axis=2)] += [0.5, 0.5,0] # "caution_zone_stairs", "caution_zone_manhole", "caution_zone_tree_zone", "caution_zone_grating", "caution_zone_repair_zone"]
    frame2[(pre==3).all(axis=2)] += [0.2, 0.7, 0.5] #"alley_crosswalk","roadway_crosswalk"
    frame2[(pre==4).all(axis=2)] += [0, 0.5, 0.5] #"braille_guide_blocks_normal", "braille_guide_blocks_damaged"
    frame2[(pre==5).all(axis=2)] += [0, 0, 0.5] #"roadway_normal","alley_normal","alley_speed_bump", "alley_damaged""
    frame2[(pre==6).all(axis=2)] += [0.5, 0, 0] #"sidewalk_blocks","sidewalk_cement" , "sidewalk_soil_stone", "sidewalk_damaged","sidewalk_other"
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    frame[(pre!=6).all(axis=2)]=0
    
    frame = cv2.resize(frame,(480,270))
    frame2 = cv2.resize(frame2,(480,270))

    return frame2, frame

def create_mask(pred_mask):
    pred_mask = tf.argmax(pred_mask, axis=-1)
    pred_mask = pred_mask[..., tf.newaxis]
    return pred_mask[0]   
