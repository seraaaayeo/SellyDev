# cartographer SLAM

![carto](path)


### cartographer : google open package for SLAM
- docs :
- download : 

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
    -odom
    -Laserscan
    -map

- save map
    <pre>
    <code>
    rosrun map_server map_saver
    </code>
    </pre>
    - map_server : ROS open package
    - format : pgm or yaml