import socket 
import cv2
import numpy as np
from queue import Queue
import time
from util.selly_vision_api import *

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

HOST = '0.0.0.0'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('server start')


client_socket, addr = server_socket.accept() 

while True: 
    print('wait')
    start= time.time()
    img_length = recvall(client_socket,16)
    img_data = recvall(client_socket, int(img_length))
    '''point_length = recvall(client_socket,16)
    point_data = recvall(client_socket, int(point_length))'''
    img_data = np.frombuffer(img_data, dtype='uint8') 
    #print(img_length, point_length)
    '''point_data = np.frombuffer(point_data, dtype='float32') 
    point_data = np.reshape(point_data, (67,120,3))'''
    img_data=cv2.imdecode(img_data,1)
    img_data = np.array(img_data, dtype=np.float32)
    #result = selly_vision_redis(img_data.copy(), point_data.copy(), fixed_dist=1)
    cv2.imshow(" ", img_data/255)
    cv2.waitKey(1)
    print(time.time() - start)




server_socket.close()