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
img = r.get("img")
img = base64.b64decode(img)
point = r.get("point")
point = base64.b64decode(point)
print(selly_vision_redis(img, point)[1])