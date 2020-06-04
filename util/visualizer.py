import numpy as np
import matplotlib.pyplot as plt
from util.depth import *
from util.path import *
from util.object_dection import *

def seg_predict_visual(img, point, model):
    frame = cv2.resize(img,(480,272))
    point = cv2.resize(point,(480,272))

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame/=255
    
    #tensorrt model
    trt = model(tf.convert_to_tensor(frame[tf.newaxis, ...]))
    trt = trt['conv2d_37'].numpy()
    
    pre = create_mask(trt).numpy()
    
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
    
def visualize(model, img, point_cloud, max_dist, fix_dist, height_max):
    ori_img = img.copy()
    seg_img, only_sidewalk = seg_predict_visual(img, point_cloud.copy() ,model)
    obj_frame, moving_object, fixed_object  = YOLO(img.copy())
    point = point_cloud.copy()
    point[200 :,:, 2][(point[200 :,:, 2] >5) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 2][(point[:,:, 2]<2)& (only_sidewalk[:,:,0] !=0)])
    point[200 :,:, 1][(point[200 :,:, 1] >3) & (only_sidewalk[200:,:,0] !=0)] = np.mean(point[:,:, 1][(point[:,:, 1]<3)& (only_sidewalk[:,:,0] !=0)])
    point[200 :,:, 0][(point[200 :,:, 0] ==np.inf) | (np.abs(point[200 :,:, 0])>2)] = np.mean(point[200:,:, 0][point[200:,:, 0]<2])
    point[:,:, 2][point[:,:, 2]==np.inf] = 40
    seg_img[((point[:,:,1] < height_max) |  (point[:,:,1] ==np.inf)) & (only_sidewalk[:,:,1]!=0)] -= [0.5, 0, 0]  #일정 높이 이상 segmetation 오차 제거
    only_sidewalk[(point[:,:,1] < height_max) |  (point[:,:,1] ==np.inf)] = 0  #일정 높이 이상 segmetation 오차 제거

    depth = point2dist(point)
    obstacle = np.ones_like(img)
    obstacle[only_sidewalk!=0] = 0
    obstacle[(point[:,:,1] < height_max) |  (point[:,:,1] ==np.inf)]=0 #일정 높이이상 장애물 제거

    obstacle_visual = obstacle.copy()
    obstacle_moving = img.copy()/2
    obstacle_fixed = img.copy()/2
    obstacle_other = obstacle.copy()

    angle = point.copy()
    angle[angle[:, :,2]==np.inf]=1
    angle = np.arctan((angle[:, :,0]/angle[:,:,2]
                            ))/np.pi * 180
    angle = angle[:,:, np.newaxis]
    angle= np.concatenate((angle,angle,angle) , axis = 2)

    for i in range(480):
        target = angle[:,i:i+1,:]
        angle_mean = np.mean(target[(target>-42) & (target<42)])
        target[np.abs(target - angle_mean)>4 ] = angle_mean
        
    moving_object_position, fixed_object_position =[] ,[]
    moving_object_angle, fixed_object_angle =[] ,[]


    if len(moving_object):
        moving_object_position = object_dist(moving_object, point.copy(), depth)
        moving_object_angle = object_angle(moving_object, angle.copy(), depth)     
    if len(fixed_object):
        fixed_object_position = object_dist(fixed_object, point.copy(), depth)
        fixed_object_angle = object_angle(fixed_object, angle.copy(), depth)     
  
    for i, j in zip(moving_object, moving_object_position):
        obstacle_visual[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0
        cv2.rectangle(obstacle_visual, i[0], i[1], (1, 1 ,1), 3) 
        cv2.putText(obstacle_visual,
                        str(j[2])+"M",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        cv2.rectangle(obstacle_moving, i[0], i[1], (255, 255 ,100), 3) 
        cv2.putText(obstacle_moving,
                        str(j[2])+"M",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0
        obstacle_other[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 1

    for i, j in zip(fixed_object, fixed_object_position):
        obstacle_visual[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0
        cv2.rectangle(obstacle_visual, i[0], i[1], (1, 1 ,1), 3) 
        cv2.putText(obstacle_visual,
                        str(j[2])+"M",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        cv2.rectangle(obstacle_fixed, i[0], i[1], (255, 100 ,255), 3) 
        cv2.putText(obstacle_fixed,
                        str(j[2])+"M",
                        (i[0][0], i[0][1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        [0, 255, 0], 2)
        obstacle[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 0    
        obstacle_other[i[0][1] :i[1][1], i[0][0] : i[1][0], :] = 1

    obstacle_other[(depth[:,:,0] > fix_dist) |(point[:,:,1] < -3) |  (point[:,:,1] ==np.inf)]=0 #일정 높이이상 장애물 제거
    obs_count={}
    oba = np.unique(np.round(angle[(obstacle_other!=0) & (obstacle_other<fix_dist)]), return_counts=True)
    for i, j in zip(oba[0],oba[1]):
        obs_count[i] = j
    for i in range(-40,40):
        if not i in obs_count.keys():
            obs_count[i] = 0
    for i in moving_object_angle:
        if i[2] < 7:
            for j in range(int(i[0]), int(i[1])+1, 1):
                if j in obs_count.keys():
                    obs_count[j] =9999
    for i in fixed_object_angle:

        if i[2] < 2:
            for j in range(int(i[0]), int(i[1])+1,1 ):
                if j in obs_count.keys():
                    obs_count[j] =9999
    able_angle = sorted(obs_count.items(), key =  lambda x : (x[1], np.abs(x[0])))
    able_angle = np.array(able_angle)
    ang_dict = {}
    for i in able_angle[:,0]:
        value =np.round(np.mean(able_angle[:,1][(able_angle[:,0] >= -10+i) & (able_angle[:,0] <= +10+i)]))
        if value != np.nan:
            ang_dict[i] = value 
    able_angle = sorted(ang_dict.items(), key =  lambda x : (x[1], np.abs(x[0])))

    plt.figure(figsize=(20,6))
    plt.subplot(2,4,1)
    plt.axis("off")
    plt.title("img")
    plt.imshow(RGB(ori_img/255))

    plt.subplot(2,4,2)
    plt.axis("off")
    plt.title("depth")
    plt.imshow(depth/40)

    plt.subplot(2,4,3)
    plt.axis("off")
    plt.title("segementation")
    plt.imshow(RGB(seg_img))

    plt.subplot(2,4,4)
    plt.axis("off")
    plt.title("object detection")
    plt.imshow(RGB(obj_frame))
    

    plt.subplot(2,4,5)
    plt.axis("off")
    plt.title( "obstacle")
    plt.imshow(obstacle_visual)


    plt.subplot(2,4,6)
    plt.axis("off")
    plt.title( "obstacle moving")
    plt.imshow(RGB(obstacle_moving)/255)

    plt.subplot(2,4,7)
    plt.axis("off")
    plt.title( "obstacle fixed")
    plt.imshow(RGB(obstacle_fixed)/255)    
    
    plt.subplot(2,4,8)
    plt.axis("off")
    plt.title( "obstacle other")
    plt.imshow(obstacle_other)

    plt.figure(figsize=(15,7))
    plt.subplot(1,2,1)
    if len(moving_object_position):
        moving_object_position_x = (moving_object_position[:, 0]+moving_object_position[:, 1])/2
        plt.scatter(moving_object_position_x , moving_object_position[:,2], c='r' , label = 'Moving',  marker = 's', zorder=2, s =50)
    else:
        plt.scatter([] , [], c='r' , label = 'Moving',  marker = 's', zorder=2, s =50)
        
    if len(fixed_object_position):
        fixed_object_position_x = (fixed_object_position[:, 0]+fixed_object_position[:, 1])/2
        plt.scatter(fixed_object_position_x , fixed_object_position[:,2], c='g', label = 'Fixed',  marker = 'D', zorder=2, s =50)
    else:
        plt.scatter([] , [], c='g', label = 'Fixed',  marker = 'D', zorder=2, s =50)

    sidewalk_x = point[:, :, 0][(only_sidewalk[:, :, 0]!=0) & (only_sidewalk[:, :, 2]!=0)]
    sidewalk_y = point[:, :, 2][(only_sidewalk[:, :, 0]!=0) & (only_sidewalk[:, :, 2]!=0)]

    px = point[:,:,0][obstacle[:,:,0]!=0]
    py = point[:,:,2][obstacle[:,:,0]!=0]

    plt.subplot(1,2,1)
    plt.scatter(0,0, zorder=3, s =100, c='b', label = 'Robot',  marker = 'h')
    plt.scatter(sidewalk_x, sidewalk_y, c='skyblue', label = "Side Walk", zorder=0,alpha = 0.1,  s =30)
    plt.scatter(px, py, c='orange', label = "Obstable", zorder=0, alpha = 0.1,  s =30)
    plt.arrow(0, 0, 5*np.sin(np.pi/(180/able_angle[0][0])), 5*np.cos(np.pi/(180/able_angle[0][0])),  linewidth = 3, head_width=1, head_length=0.5, color = "lime", label = "Path")
    plt.ylim(0,30)
    plt.xlim(-10,10)
    plt.legend(labels = ["Robot", "Moving", "Fixed","Side Walk", "Obstable", "Path"], loc="upper right")
    plt.ylabel("depth(m)")
    plt.xlabel("dist(m)")
    plt.title("2D map - dist")

    plt.subplot(1,2,2)


    moving_object_x = []
    moving_object_y = []
    for i in moving_object_angle:
        arr_x = []
        arr_y = []
        for j in range(int(i[0]), int(i[1])):
            arr_x.append(j)
            arr_y.append(i[2])
        moving_object_x.extend(arr_x)
        moving_object_y.extend(arr_y)

    fixed_object_x = []
    fixed_object_y = []
    for i in fixed_object_angle:
        arr_x = []
        arr_y = []
        for j in range(int(i[0]), int(i[1])):
            arr_x.append(j)
            arr_y.append(i[2])
        fixed_object_x.extend(arr_x)
        fixed_object_y.extend(arr_y)
    plt.scatter(0,0, zorder=3, s =100, c='b', label = 'Robot',  marker = 'h')
    plt.scatter(moving_object_x , moving_object_y, c='r' , label = 'Moving',  marker = 's', zorder=2, s =50)
    plt.scatter(fixed_object_x , fixed_object_y, c='g', label = 'Fixed',  marker = 'D', zorder=2, s =50)
        
    sidewalk_x = angle[:, :, 0][(only_sidewalk[:, :, 0]!=0) & (only_sidewalk[:, :, 2]!=0)]
    sidewalk_y = point[:, :, 2][(only_sidewalk[:, :, 0]!=0) & (only_sidewalk[:, :, 2]!=0)]

    px = angle[:,:,0][obstacle[:,:,0]!=0]
    py = point[:,:,2][obstacle[:,:,0]!=0]

    plt.scatter(sidewalk_x, sidewalk_y, c='skyblue', label = "Side Walk", zorder=0,alpha = 0.1,  s =30)
    plt.scatter(px, py, c='orange', label = "Obstable", zorder=0, alpha = 0.1,  s =30)
    plt.arrow(able_angle[0][0], 0, 0 , 5, linewidth = 4, head_width=2, head_length=0.5, color = "lime", label = "Path")
    plt.ylim(0,30)
    plt.xlim(-45,45)
    plt.legend(labels = ["Robot", "Moving", "Fixed","Side Walk", "Obstable", "Path"], loc="upper right")
    plt.ylabel("depth(m)")
    plt.xlabel("angle(degree)")
    plt.title("2D map - angle")



def RGB(frame): 
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)