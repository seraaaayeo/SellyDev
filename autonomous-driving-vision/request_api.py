import numpy as np
import requests
import time
import base64
from PIL import Image
import io 
import cv2
import ast
import math
from selly_vision_api import *
from visualizer import *

data = np.load("video_data.npz")
data = data["arr_0"]

img = data[:,0,:,:,:]
point_cloud = data[:,1,:,:,:]

angle_url = "http://127.0.0.1:5000/vision_angle"
img_url = "http://127.0.0.1:5000/vision_img"

def angle_receiver(img, point_cloud):
    img =  np.array(img, dtype=np.float32).tobytes()
    point =  np.array(point_cloud, dtype=np.float32).tobytes()
    files = {'img': img, 'point' : point}
    response = requests.post(angle_url, files=files)
    angle_list = ast.literal_eval(response.text)
    return angle_list

i=0
while True:
    start = time.time()

    angle_list = angle_receiver(img[i].copy(), cv2.resize(point_cloud[i].copy(), (67,120)))
    for angle in angle_list:
        x = 100 * math.cos(math.radians(angle+ (180/15)/2))
        y = 100 * math.sin(math.radians(angle+ (180/15)/2))
        cv2.arrowedLine(img[i], (240, 270) , (240+int(x),270-int(y)), (0,255,0), 3, tipLength=0.15 )
    cv2.imshow(" ", img[i]/255)
    #cv2.imshow(" ", selly_vision_redis(img[i], point_cloud[i])[0]/255)
    cv2.waitKey(1)
    print(time.time() - start)
    i+=1