import cv2
import redis
import io
from PIL import Image
import base64
import numpy as np
import time
from datetime import datetime
from util.selly_vision_api import *

r = redis.StrictRedis(port=6379)
first_time = r.hget('zed_img', 'time')

while True:
    st = time.time()
    data = r.hgetall('zed_img')
    if first_time == data.get('time'.encode()):
        continue
    first_time =  data.get('time'.encode())
    #dt = datetime.now().strftime('%H:%M:%S')

    img = data.get('img'.encode())
    img = base64.b64decode(img.decode())
    img = Image.open(io.BytesIO(img)) 
    img = np.array(img, dtype=np.float32)

    point = data.get('point'.encode())
    point = np.frombuffer(point, dtype=np.float32)
    point = np.reshape(point,(67,120,3))

    result = selly_vision_redis(img.copy(), point.copy(),fixed_dist=2.5)
    #result = selly_vision_visual(img.copy(), point.copy(),fixed_dist=2.5)

    '''cv2.imshow("seg_img", result[0])
    cv2.waitKey(1)
    cv2.imshow("yolo_img", result[1])
    cv2.waitKey(1)
    cv2.imshow("moving_obstacle", result[2])
    cv2.waitKey(1)
    cv2.imshow("fixed_obstacle", result[3])
    cv2.waitKey(1)
    cv2.imshow("obs_obj", result[4])
    cv2.waitKey(1)
    cv2.imshow("selly_vision", result[5]/255)
    cv2.waitKey(1)'''

    r.hmset('result', {"result" : str(result[1]), "time" : st})

    '''cv2.imshow(" ", result[0]/255)
    cv2.waitKey(1)'''
    #print(result[1])
    print(time.time()-st)

