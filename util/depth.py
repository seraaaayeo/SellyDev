import math
import cv2
from util.angle import *


def distance(value):
    dist = math.sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2])
    return (dist, dist, dist)

def point2dist(arr, size):    
    width, height = int(480 * size), int(240 * size)
    arr  = cv2.resize(arr, (width ,height))
    arr = np.reshape(arr, (height*width,3))
    dist = list(map(lambda value : distance(value) , arr))  
    dist= np.array(dist)
    dist = np.reshape(dist, (height,width,3))
    dist[(dist>50)] = 50
    dist = cv2.resize(dist, (480 ,270))
    return dist