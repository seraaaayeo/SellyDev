#!/usr/bin/python3
import cv2
import tensorflow as tf
import keras 
import numpy as np

def sensor_analysis_result(image, lidar, buf_motor_speed, buf_motor_angle):
    motor_speed =0
    motor_angle = 65
    
    return motor_speed, motor_angle