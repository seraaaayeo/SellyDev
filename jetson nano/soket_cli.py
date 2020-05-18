import socket 
import numpy as np
import cv2
import time
from _thread import *
from queue import Queue
import pyzed.sl as sl
import sys
import base64

HOST = '123.254.187.65'
PORT = 9999

zed = sl.Camera()

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

err = zed.open(init)
if err != sl.ERROR_CODE.SUCCESS :
    print(repr(err))
    zed.close()
    exit(1)

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client_socket.connect((HOST, PORT)) 

image_zed, point_cloud = sl.Mat(), sl.Mat()

image_size = zed.get_camera_information().camera_resolution
image_size.width = image_size.width/4
image_size.height = image_size.height/4

point_size = zed.get_camera_information().camera_resolution
point_size.width = point_size.width/16
point_size.height = point_size.height/16

while True:
    start_time = time.time()
    err = zed.grab(runtime)
    if err == sl.ERROR_CODE.SUCCESS :
        zed.retrieve_image(image_zed,sl.VIEW.LEFT, sl.MEM.CPU, image_size)
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZ,  sl.MEM.CPU, point_size)
        image_ocv = image_zed.get_data()[:,:,:3]
        point_cloud_data =point_cloud.get_data()[:,:,:3]

    point_cloud_data = point_cloud_data.tobytes()
    result, imgencode = cv2.imencode('.jpg', image_ocv)
    data = np.array(imgencode)
    stringData = data.tostring()
    client_socket.send(str(len(stringData)).ljust(16).encode())
    client_socket.send(stringData)
    client_socket.send(str(len(point_cloud_data)).ljust(16).encode())
    client_socket.send(point_cloud_data)
    print(time.time() - start_time)
client_socket.close() 

