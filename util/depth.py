import math
import cv2
from util.angle import *


def distance(value):
    dist = math.sqrt(value[0]*value[0] + value[1]*value[1] + value[2]*value[2])
    return (dist, dist, dist)

def point2dist(arr, size): 
    width, height = int(480 * 1/4), int(270 * 1/4)
    arr  = cv2.resize(arr, (width ,height))
    arr = np.reshape(arr, (height*width,3))
    dist = np.sqrt(np.sum(np.square(arr), axis = 1))
    dist = np.reshape(dist, (height,width,1))
    dist = np.concatenate((dist,dist, dist), axis=2)
    dist[(dist>30)] = 30
    dist = cv2.resize(dist, (480 ,270))
    return dist