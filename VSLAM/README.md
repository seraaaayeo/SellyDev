# visual SLAM with ZED camera

![vslam](path)

### openVSLAM : visual SLAM open package
- docs : https://openvslam.readthedocs.io/en/master/index.html
- paper : https://arxiv.org/pdf/1910.01122.pdf

### dev options
- dependencies : DBoW2, eigen, g2o, glog, Panglin, SuiteSparse, yaml-cpp
- all of them is latest version(based on 2020-04-22)

### config file
- ZED camera parameter
    ```
    Camera.name: "Selly vision"
    Camera.setup: "monocular"
    Camera.model: "perspective"

    Camera.fps: 25.0
    Camera.cols: 480
    Camera.rows: 270
    Camera.focal_x_baseline: 119.471

    Camera.color_order: "RGB"

    # Camera Calibration
    Camera.fx: 537.021240234375
    Camera.fy: 537.021240234375
    Camera.cx: 623.784423828125
    Camera.cy: 355.7088623046875

    Camera.k1: 0.0
    Camera.k2: 0.0
    Camera.p1: 0.0
    Camera.p2: 0.0
    Camera.k3: 0.0
    ```

### how to run
- visual slam with recorded video
    ```
    ./run_video_slam
    -v /path/orb_vocab/orb_vocab.dbow2 //vocabulary file path
    -m /path/selly_vision/video.mp4 //video path
    -c /path/selly_vision/config.yaml //camera config file path
    ```
