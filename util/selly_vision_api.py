import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import tensorflow as tf
import time
from model.pspunet import pspunet
from util.angle import *
from util.depth import *
from util.path import *
from util.visualizer import *
from util.object_dection import *
from PIL import Image
import io

gpus = tf.config.experimental.list_physical_devices('GPU')

IMG_WIDTH = 480
IMG_HEIGHT = 272
n_classes = 7

if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(
       gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=500)])
    except RuntimeError as e:
        print(e)
        
model = pspunet((IMG_HEIGHT, IMG_WIDTH ,3), n_classes)
model.load_weights("pspunet_weight.h5")

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
    return selly_vision_img(model, img, point, moving_dist, fixed_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG)

def selly_vision_visual(img, point, moving_dist=5, fixed_dist=2.5):
    return image_pred(model, img, point, moving_dist, fixed_dist, ANGLE, ANGLE_CLASS, ANGLE_IMG)
