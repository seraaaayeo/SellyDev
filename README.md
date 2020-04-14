# cartographer SLAM

![carto](https://user-images.githubusercontent.com/53554014/79229579-39ed3180-7e9e-11ea-8735-46107d80ca2b.gif)


### cartographer : google open package for SLAM
- docs : https://google-cartographer-ros.readthedocs.io/en/latest/index.html
- download : https://github.com/cartographer-project/cartographer_ros

### how to run
- camera sensor
    ```
    roslaunch zed_wrapper zed2.launch
    ```

- cartographer
    ```
    roslaunch carto_mapper mapper.launch
    ```
    - include ydlidar, rviz 
    - rviz topic
        - odom
        - Laserscan
        - map

- save map
    ```
    rosrun map_server map_saver
    ```
    - map_server : ROS open package
    - format : pgm or yaml
