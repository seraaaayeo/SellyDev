import numpy as np
import requests
import time
import base64
import cv2
import ast
import math
import sys
import pyzed.sl as sl
import math 
import redis    
import io
from PIL import Image
import datetime
from multiprocessing import Pool
import asyncio

r = redis.StrictRedis(host='' ,port=6379)
loop = asyncio.get_event_loop()

def img2byte(image_ocv):
    image = Image.fromarray(image_ocv,'RGB')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

def point2byte(point):
    return point_cloud_data.tobytes()

def send_img(image_ocv, point_cloud_data , num): 
    start_time = time.time()
    r.hmset('zed_img_'+str(num), {"img" : str(img2byte(image_ocv)), "point" : point_cloud_data.tobytes(), "time" : start_time})

async def main(num):
    time.sleep(num*0.05)
    while True:
        start_time = time.time()
        err = zed.grab(runtime)
        if err == sl.ERROR_CODE.SUCCESS :
            zed.retrieve_image(image_zed,sl.VIEW.LEFT, sl.MEM.CPU, image_size)
            zed.retrieve_measure(point_cloud, sl.MEASURE.XYZ,  sl.MEM.CPU, point_size)
            image_ocv = image_zed.get_data()[:,:,:3]
            point_cloud_data =point_cloud.get_data()[:,:,:3]
            await loop.run_in_executor(None, send_img,image_ocv, point_cloud_data , num)
            print(time.time() - start_time)


zed = sl.Camera()
input_type = sl.InputType()
if len(sys.argv) >= 2 :
    input_type.set_from_svo_file(sys.argv[1])
init = sl.InitParameters(input_t=input_type)
init.camera_resolution = sl.RESOLUTION.HD1080
init.depth_mode = sl.DEPTH_MODE.PERFORMANCE
init.coordinate_units = sl.UNIT.METER
init.depth_maximum_distance = 20
init.depth_minimum_distance = 0.5
runtime = sl.RuntimeParameters()
runtime.sensing_mode = sl.SENSING_MODE.FILL

err = zed.open(init)
if err != sl.ERROR_CODE.SUCCESS :
    print(repr(err))
    zed.close()
    exit(1)

image_size = zed.get_camera_information().camera_resolution
image_size.width = image_size.width/8
image_size.height = image_size.height/8

point_size = zed.get_camera_information().camera_resolution
point_size.width = point_size.width/16
point_size.height = point_size.height/16

image_zed, point_cloud = sl.Mat(), sl.Mat()

loop.run_until_complete(asyncio.gather(main(1),main(2),main(3),main(4)))

