import cv2
import pyzed.sl as sl

def main():
    zed = sl.Camera()

    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.NONE

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS :
        print(repr(err))
        zed.close()
        exit(1)

    # Get camera information
    info = zed.get_camera_information()
    cam_model = info.camera_model
    print('cam model', cam_model)

    calibration_parmas = zed.get_camera_information().calibration_parameters
    # Focal length
    fx_left = calibration_parmas.left_cam.fx
    fy_left = calibration_parmas.left_cam.fy
    fx_right = calibration_parmas.right_cam.fx
    fy_right = calibration_parmas.right_cam.fy
    print('focal length_X', fx_left, fx_right)
    print('focal length_y', fy_left, fy_right)

    # Principal points
    cx_left = calibration_parmas.left_cam.cx
    cx_right = calibration_parmas.right_cam.cx
    print('cx', cx_left, cx_right)
    cy_left = calibration_parmas.left_cam.cy
    cy_right = calibration_parmas.right_cam.cy
    print('cy', cy_left, cy_right)

    # Focal radial distortion coefficient
    k1_left = calibration_parmas.left_cam.disto[0]
    k1_right = calibration_parmas.right_cam.disto[0]
    print('distortion_k1', k1_left, k1_right)
    k2_left = calibration_parmas.right_cam.disto[1]
    k2_right = calibration_parmas.right_cam.disto[1]
    print('distortion_k2', k2_left, k2_right)


if __name__ == "__main__":
    main()
