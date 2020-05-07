import cv2
import redis
import io
from PIL import Image
import base64
import numpy as np
import time
from datetime import datetime
from selly_vision_api import *

r = redis.StrictRedis(host='123.254.187.65' ,port=6379)

while True:
    st = time.time()
    dt = datetime.now().strftime('%H:%M:%S')

    img = r.hget('zed_img', 'img')
    img = base64.b64decode(img.decode())
    img = Image.open(io.BytesIO(img)) 
    img = np.array(img, dtype=np.float32)

    point = r.hget('zed_img', 'point')
    point = np.frombuffer(point, dtype=np.float32)
    point = np.reshape(point,(67,120,3))

    result = selly_vision_redis(img.copy(), point.copy(),fixed_dist=1)
    r.hmset('result', {"result" : str(result[1]), "datetime" : str(dt)})


    ''cv2.imshow(" ", result[0]/255)
    cv2.waitKey(1)''

    print(result[1])
    print(time.time()-st)

