import cv2
import time
import sys
import numpy as np
import pyzed.sl as sl
import math 
import redis
import base64
import io
from PIL import Image

def main() :           
    zed = sl.Camera()

    # Set configuration parameters
    input_type = sl.InputType()
    if len(sys.argv) >= 2 :
        input_type.set_from_svo_file(sys.argv[1])
    
    init = sl.InitParameters(input_t=input_type)
    init.camera_resolution = sl.RESOLUTION.HD1080
    init.coordinate_units = sl.UNIT.METER
    runtime = sl.RuntimeParameters()
    runtime.sensing_mode = sl.SENSING_MODE.FILL

    # Open the camera
    err = zed.open(init)
    if err != sl.ERROR_CODE.SUCCESS :
        print(repr(err))
        zed.close()
        exit(1)

    # Prepare new image size to retrieve half-resolution images
    image_size = zed.get_camera_information().camera_resolution
    image_size.width = image_size.width/4
    image_size.height = image_size.height/4

    # set video codec
    codec = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('selly_vison3.mp4', codec, 30.0, (480, 270))

    # Declare your sl.Mat matrices
    image_zed = sl.Mat() 
    while True:
        start_time = time.time()
        err = zed.grab(runtime)
        if err == sl.ERROR_CODE.SUCCESS :
            zed.retrieve_image(image_zed,sl.VIEW.LEFT, sl.MEM.CPU, image_size)
            image_frame = image_zed.get_data()[:,:,:3]
            start =time.time()

            cv2.imshow("Image2", image_frame)
            out.write(image_frame)

            if cv2.waitKey(1) & 0xFF == 32:
                break
            print("fps : ",round(1/(time.time()- start_time),2))

    out.release()
    cv2.destroyAllWindows()
    zed.close()
    print("\nFINISH")

if __name__ == "__main__":
    main()