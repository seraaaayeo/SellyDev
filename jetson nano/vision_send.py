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

r = redis.StrictRedis(host='123.254.187.65' ,port=6379)

def img2byte(image_ocv):
    image = Image.fromarray(image_ocv,'RGB')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

def point2byte(point):
    return point_cloud_data.tobytes()

zed = sl.Camera()
    # Set configuration parameters
input_type = sl.InputType()
if len(sys.argv) >= 2 :
    input_type.set_from_svo_file(sys.argv[1])
init = sl.InitParameters(input_t=input_type)
init.camera_resolution = sl.RESOLUTION.HD1080
init.depth_mode = sl.DEPTH_MODE.PERFORMANCE
init.coordinate_units = sl.UNIT.METER
init.depth_maximum_distance = 40
init.depth_minimum_distance = 0.2
runtime = sl.RuntimeParameters()
runtime.sensing_mode = sl.SENSING_MODE.FILL
    # Open the camera
err = zed.open(init)
if err != sl.ERROR_CODE.SUCCESS :
    print(repr(err))
    zed.close()
    exit(1)

    # Prepare new image size to retrieve half-resolution images
image_size = zed.get_camera_information().camera_resolution
image_size.width = image_size.width/4
image_size.height = image_size.height/4

point_size = zed.get_camera_information().camera_resolution
point_size.width = point_size.width/16
point_size.height = point_size.height/16


    # Declare your sl.Mat matrices
image_zed, point_cloud = sl.Mat(), sl.Mat()
while True:
    start_time = time.time()
    dt = datetime.datetime.now().strftime('%H:%M:%S')
    err = zed.grab(runtime)
    if err == sl.ERROR_CODE.SUCCESS :
        zed.retrieve_image(image_zed,sl.VIEW.LEFT, sl.MEM.CPU, image_size)
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZ,  sl.MEM.CPU, point_size)
        start_time = time.time()

        image_ocv = image_zed.get_data()[:,:,:3]
        point_cloud_data =point_cloud.get_data()[:,:,:3]
        #image_ocv = np.array(image_ocv, dtype = np.float32)
        r.hmset('zed_img', {"img" : str(img2byte(image_ocv)), "point" : point2byte(point_cloud_data), "datetime" : dt})

        print(time.time() - start_time)
