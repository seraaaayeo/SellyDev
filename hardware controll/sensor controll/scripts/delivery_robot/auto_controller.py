#!/usr/bin/env python3
import time 
import rospy
import cv2
from std_msgs.msg import UInt16
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from sensor_analysis import *
 
rospy.init_node('Controller', anonymous = True)

bridge = CvBridge()

image_data = []
lidar_data = []

buf_motor_speed = 0
buf_motor_angle = 65

def image_callback(msg):  #image receiver
      global image_data 
      start_time =time.time()
      frame = bridge.imgmsg_to_cv2(msg, "bgr8")
      image_data = frame
      return 

def lidar_callback(msg):   # lidar receiver index 0~719 , 0.5 degree 
      global lidar_data 
      start_time =time.time()
      lidar_data = list(map(lambda x : 99 if x<0.1 else round(x, 2), msg.ranges))
      return 

def Analysis():  # custom about sensor_analysis_result function!
      global image_data, lidar_data, buf_motor_speed, buf_motor_angle
      image = image_data.copy()
      lidar = lidar_data[:]
      motor_speed, motor_angle = sensor_analysis_result(image, lidar, buf_motor_speed, buf_motor_angle) 
      return motor_speed, motor_angle

def auto_controll():  
      global  buf_motor_speed, buf_motor_angle
      pub_motor_speed = rospy.Publisher('motor_speed',UInt16)
      pub_motor_angle = rospy.Publisher('motor_angle',UInt16)
      time.sleep(3)  #sensor loading...
      while not rospy.is_shutdown():
            start_time =time.time()
            motor_speed, motor_angle = Analysis()
            if buf_motor_speed != motor_speed:
                  pub_motor_speed.publish(motor_speed)
                  buf_motor_speed = motor_speed
            elif buf_motor_angle != motor_angle:
                  pub_motor_angle.publish(motor_angle)
                  buf_motor_angle = motor_angle
            else :
                  continue
            print("speed = ", motor_speed, ", angle = ", motor_angle)
      return

if __name__=='__main__':
      try:
            rospy.Subscriber('/scan', LaserScan, lidar_callback)
            rospy.Subscriber('/image', Image, image_callback)
            auto_controll()
      except rospy.ROSInterruptException:
            pass


