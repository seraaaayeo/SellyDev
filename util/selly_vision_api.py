import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from util.angle import *
from util.depth import *
from util.path import *
from util.visualizer import *
from util.object_dection import *

gpus = tf.config.experimental.list_physical_devices('GPU')

if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(
       gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=500)])
    except RuntimeError as e:
        print(e)
    
loaded = tf.saved_model.load("./trt_fp16")
infer = loaded.signatures["serving_default"]

ANGLE_CLASS = 18

ANGLE = angle_dict(ANGLE_CLASS)
ANGLE_IMG = angle_img(ANGLE, ANGLE_CLASS)

def selly_vision(img, point, moving_dist=5, fixed_dist=2.5):
    img = np.frombuffer(img, dtype=np.float32)
    img = np.reshape(img, (270,480,3))
    point = np.frombuffer(point, dtype=np.float32)
    point = np.reshape(point, (67,120,3))
    result = selly_vision_img(model, img, point, moving_dist, fixed_dist, ANGLE, ANGLE_CLASS,ANGLE_IMG)
    return result

def selly_vision_redis(img, point, moving_dist=5, fixed_dist=2.5):
    return selly_vision_img(infer, img, point, moving_dist, fixed_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG)

def selly_vision_visual(img, point, moving_dist=5, fixed_dist=2.5):
    return image_pred(infer, img, point, moving_dist, fixed_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG)
