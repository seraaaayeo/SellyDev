import numpy as np
import matplotlib.pyplot as plt
from util.angle import *
from util.depth import *
from util.path import *
from util.object_dection import *

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

    frame[((pre!=4) & (pre!=6) & (pre!=1)& (pre!=3)).all(axis=2)]=0
    
    frame = cv2.resize(frame,(480,270))
    frame2 = cv2.resize(frame2,(480,270))

    return frame2, frame
    
def image_pred(model, img, point_cloud, max_dist, fix_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG):
    max_dist = max_dist
    ori_img = img.copy()
    seg_img, only_sidewalk = seg_predict(img,model)
    yolo_img, _, __ = YOLO(img.copy())
    depth = point2dist(point_cloud, 1/16)
    only_sidewalk_limited_dist = only_sidewalk.copy()
    only_sidewalk_limited_dist[(depth>max_dist)] = 0
    obstacle = img.copy()
    obstacle_depth = img.copy()
    obstacle_depth[(depth>max_dist)] = 0 
    obj_frame, moving_object, fixed_object = YOLO(obstacle_depth)
    obstacle[~((only_sidewalk ==0) & (obstacle_depth!=0))] = 0
    obs_obj = (obstacle).copy()
    for i in moving_object:
        cv2.rectangle(obs_obj, i[0], i[1], (100, 255 ,255), 3) 
        cv2.putText(obs_obj,
                        "Moving object",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)

    for i in fixed_object:
        cv2.rectangle(obs_obj, i[0], i[1], (255, 100 ,255), 3) 
        cv2.putText(obs_obj,
                        "Fixed_object",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)


    obstacle_angle =  vision_angle(ANGLE, obstacle)

    moving_obstacle = np.zeros_like(obstacle)
    fixed_obstacle = np.zeros_like(obstacle)

    for i in moving_object:
        crop_obstacle_angle = obstacle_angle[i[0][1] : i[1][1], i[0][0] : i[1][0], :]
        obj = np.zeros((i[1][1] - i[0][1],i[1][0] - i[0][0],3))
        obj[crop_obstacle_angle!=0] = crop_obstacle_angle[crop_obstacle_angle!=0]
        moving_obstacle[i[0][1] : i[1][1], i[0][0] : i[1][0], :] = obj


    fixed_obstacle[(moving_obstacle==0) & (obstacle!=0)] = obstacle[(moving_obstacle==0) & (obstacle!=0)]
    fixed_obstacle[(depth> fix_dist)] = 0
    obstacle_depth[(depth> fix_dist)] = 0
    _, _, fixed_object = YOLO(obstacle_depth)


    for i in moving_object:
        cv2.rectangle(moving_obstacle, i[0], i[1], (100, 255 ,255), 3) 
        cv2.putText(moving_obstacle,
                                "Moving object",
                                (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                [0, 255, 0], 2)

    for i in fixed_object:
        cv2.rectangle(fixed_obstacle, i[0], i[1], (255, 100 ,255), 3) 
        cv2.putText(fixed_obstacle,
                                "Fixed_object",
                                (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                [0, 255, 0], 2)


    selly_vision, angle = selly_vision_img(model, img.copy(), point_cloud, max_dist, fix_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG)

    return seg_img, yolo_img, moving_obstacle/(ANGLE_CLASS), fixed_obstacle/(ANGLE_CLASS), obs_obj, selly_vision

