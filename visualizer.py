import numpy as np
import matplotlib.pyplot as plt
from util.angle import *
from util.depth import *
from util.path import *
from util.object_dection import *

def visualize(model, img, point_cloud, max_dist, fix_dist, angle, ANGLE_CLASS):
    max_dist = max_dist
    ori_img = img.copy()
    seg_img, only_sidewalk = seg_predict(img,model)
    yolo_img, _, __ = YOLO(img.copy())
    depth = point2dist(point_cloud, 1/4)
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


    obstacle_angle =  vision_angle(angle, obstacle)

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


    selly_vision, angle = selly_vision_img(model, img.copy(), point_cloud, max_dist, fix_dist, angle, ANGLE_CLASS)

    plt.figure(figsize=(20,16))
    plt.subplot(4,3,2)
    plt.axis("off")
    plt.title("img")
    plt.imshow(RGB(ori_img/255))

    plt.subplot(4,3,4)
    plt.axis("off")
    plt.title("depth")
    plt.imshow(depth/50)

    plt.subplot(4,3,5)
    plt.axis("off")
    plt.title("segementation")
    plt.imshow(RGB(seg_img))

    plt.subplot(4,3,6)
    plt.axis("off")
    plt.title("object detection")
    plt.imshow(RGB(yolo_img))

    '''plt.subplot(3,3,5)
    plt.axis("off")
    plt.title( "only sidewalk in "+str(max_dist)+"M")
    plt.imshow(RGB(only_sidewalk_limited_dist))

    plt.subplot(3,3,6)
    plt.axis("off")
    plt.title( "img in "+str(max_dist)+"M")
    plt.imshow(RGB(obstacle_depth/255))

    plt.subplot(3,3,7)
    plt.axis("off")
    plt.title("only sidewalk")
    plt.imshow(RGB(only_sidewalk))'''

    plt.subplot(4,3,7)
    plt.axis("off")
    plt.title( "obstacle in "+str(max_dist)+"M")
    plt.imshow(obs_obj)

    '''plt.subplot(3,3,6)
    plt.axis("off")
    plt.title( "obstacle angle")
    plt.imshow(obstacle_angle/(ANGLE_CLASS))'''

    '''plt.subplot(3,3,6)
    plt.axis("off")
    plt.title( "obstacle in "+str(fix_dist)+"M")
    obs_obj[(depth> fix_dist)] = 0
    plt.imshow(obs_obj)'''

    plt.subplot(4,3,8)
    plt.axis("off")
    plt.title( "moving_obstacle in "+str(max_dist)+"M")
    plt.imshow(RGB(moving_obstacle/(ANGLE_CLASS)))

    plt.subplot(4,3,9)
    plt.axis("off")
    plt.title( "fixed_obstacle in "+ str(fix_dist)+"M")
    plt.imshow(fixed_obstacle/(ANGLE_CLASS))

    plt.subplot(4,3,11)
    plt.axis("off")
    plt.title( "selly_vision")
    plt.imshow(RGB(selly_vision/255))

def RGB(frame): 
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)