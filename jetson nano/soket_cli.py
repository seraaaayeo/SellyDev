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

def point2dist(arr): 
    width, height = int(480 * 1/4), int(270 * 1/4)
    arr  = cv2.resize(arr, (width ,height))
    arr = np.reshape(arr, (height*width,3))
    dist = np.sqrt(np.sum(np.square(arr), axis = 1))
    dist = np.reshape(dist, (height,width,1))
    dist = np.concatenate((dist,dist, dist), axis=2)
    dist[(dist>30)] = 30
    dist = cv2.resize(dist, (120 ,67))
    return dist

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
        point_cloud_data = point_cloud.get_data()[:,:,:3]
        point_cloud_data = point2dist(point_cloud_data)
        point_cloud_data = (point_cloud_data*255)/30
        point_cloud_data = np.array(point_cloud_data, dtype = np.uint8)


    _, img_encode = cv2.imencode('.jpg', image_ocv)
    img_data = np.array(img_encode)
    img2str = img_data.tostring()

    _, depth_encode = cv2.imencode('.jpg', point_cloud_data)
    depth_data = np.array(depth_encode)
    depth2str = depth_data.tostring()

    client_socket.send(str(len(img2str)).ljust(16).encode())
    client_socket.send(img2str)

    client_socket.send(str(len(depth2str)).ljust(16).encode())
    client_socket.send(depth2str)

    '''msg = client_socket.recv(1024)
    msg = msg.decode()'''

    #print("주행 가능 방향 : ", msg)
    print("경과 시간 : ", round(time.time() - start_time, 3),"초")

client_socket.close() 

