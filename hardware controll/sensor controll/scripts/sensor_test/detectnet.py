#!/usr/bin/python3
# rospy for the subscriber
import rospy
import cv2
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import jetson.inference
import jetson.utils
import time
import numpy as np

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
    rospy.init_node('detect')
    # Define your image topic
    output_image_topic = "/detect"
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=3), cv2.CAP_GSTREAMER)
    net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
    pub = rospy.Publisher(output_image_topic, Image, queue_size=1)
    while True:
        start_time = time.time()
        ret_val, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        cuda_frame = jetson.utils.cudaFromNumpy(img)
        detections = net.Detect(cuda_frame, img.shape[1], img.shape[0])
        jetson.utils.cudaDeviceSynchronize ()
        aimg = jetson.utils.cudaToNumpy(cuda_frame, img.shape[1], img.shape[0], 4)
        aimg1 = cv2.cvtColor (aimg.astype (np.uint8), cv2.COLOR_RGBA2BGR)
        image_message = bridge.cv2_to_imgmsg(aimg1, encoding="bgr8")
        pub.publisgh(image_message)
        print(time.time()- start_time)


if __name__ == '__main__':
    main()
