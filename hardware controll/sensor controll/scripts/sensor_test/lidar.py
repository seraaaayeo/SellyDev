#!/usr/bin/python3 
#import PyLidar3
import rospy
from sensor_msgs.msg import LaserScan
import time

def callback(msg):   # index 0~719 , 0.5 degree 
    a = list(map(lambda x : 999.0 if x<0.1 else round(x, 2), msg.ranges))
    print(a[:10])

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()