#!/usr/bin/python3
# rospy for the subscriber
import rospy
import cv2
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import time

# Instantiate CvBridge
bridge = CvBridge()

def gstreamer_pipeline(
    capture_width=640,
    capture_height=360,
    display_width=640,
    display_height=360,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

def main():
    #rospy.init_node('image_listener')
    rospy.init_node('image')
    # Define your image topic
    output_image_topic = "/image"
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=3), cv2.CAP_GSTREAMER)
    pub = rospy.Publisher(output_image_topic, Image, queue_size=1)
    while True:
        start_time = time.time()
        ret_val, img = cap.read()
        image_message = bridge.cv2_to_imgmsg(img, encoding="bgr8")
        pub.publish(image_message)
        print(time.time()- start_time)


if __name__ == '__main__':
    main()
