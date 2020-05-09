import numpy as np
import math
from util.depth import *

def angle_value(x, y):
    myradians = math.atan2(x[1]-y[1], x[0]-y[0])        
    mydegrees = math.degrees(myradians)
    return mydegrees + 90

def angle_dict(ANGLE_CLASS):
    angle={}
    center = (270,240)
    for i in range(270):
        for j in range(480):
            angle[str(i)+","+str(j)] = angle_value(center,(i, j))//(180/ANGLE_CLASS) + 1
    return angle 

def vision_angle(angle, obstacle):
    obs = np.where(obstacle!=0) 
    obs_idx = [(i,j) for i,j in zip(obs[0], obs[1])]
    obstacle[obstacle!=0] = np.array(list(map(lambda x : angle[str(x[0])+","+str(x[1])] , obs_idx)))
    return obstacle
    
def angle_img(angle, ANGLE_CLASS):
    img = np.zeros((270,480,3))
    for i in range(270):
            for j in range(480):
                img[i,j,:] = angle[str(i)+","+str(j)]     
    return img