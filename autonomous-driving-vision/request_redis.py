import numpy as np
import requests
import time
import base64
import cv2
import ast
import math
import sys
import math 
import redis    
import io
from PIL import Image
import datetime

r = redis.StrictRedis(port=6379)

def img2byte(image_ocv):
    image = Image.fromarray(image_ocv,'RGB')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

def point2byte(point):
    return point_cloud_data.tobytes()

data = np.load("video_data.npz")
data = data["arr_0"]

img = data[:,0,:,:,:]
point_cloud = data[:,1,:,:,:]

i=0
while True:
    start_time = time.time()
    #dt = datetime.datetime.now().strftime('%H:%M:%S')
    image_ocv = img[i].copy()
    point_cloud_data = point_cloud[i].copy()
    point_cloud_data= cv2.resize(point_cloud_data, (120,67))
    r.hmset('zed_img', {"img" : str(img2byte(image_ocv)), "point" : point2byte(point_cloud_data), "time" : start_time})

    i+=1
    #data = r.hgetall('zed_img')

    print(time.time() - start_time)
