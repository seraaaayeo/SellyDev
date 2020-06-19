<h3 align="center">Sejong delivery : Selly</h3>
<p align="center">
  :oncoming_automobile:Sejong University Selly Project Developers in 2020:oncoming_automobile:
</p>

* * *

## Description
교내 카페 '팬도로시'부터 AI센터까지 인도 보행으로 자율주행하는 배달로봇입니다.

This is an Autonomous-driving robot software which drives on pavement only. First test path is pavement in front of main gate, Sejong University along with road from 'cafe Pandorosi' to 'AI center'.

## Our purpose
카메라 센서만을 사용한 vision 기반 자율주행 알고리즘 개발. 

This is an auto-driving algorithm based on vision.

## Main Project List
* [autonomous-driving-vision](https://github.com/seraaaayeo/SellyDev/tree/selly/autonomous-driving-vision) : Image analysis to aviod obstacle:pushpin:
* [road-segmentation](https://github.com/seraaaayeo/SellyDev/tree/selly/road-segmentation) : Segmentation for pavement driving
* [object-detection](https://github.com/seraaaayeo/SellyDev/tree/selly/Obejct-Detection) : object detection to divide moving obstacle such as car and fixed object such as tree
* [VSLAM](https://github.com/seraaaayeo/SellyDev/tree/selly/VSLAM) : Visual SLAM for mapping and localization to let robot know where it is
  * If you use Lidar sensor, you can use [cartographer](https://github.com/seraaaayeo/SellyDev/tree/cartographer) for SLAM

## Contributor
* [이준혁 (JunHyeok Lee)](https://github.com/JunHyeok96):crown:
* [여다솔 (Dasol Yeo)](https://github.com/seraaaayeo)
* [김연우 (Yeonwoo Kim)](https://github.com/Yeonwoo-Kim)

***

## Period
Junuary/2020 - June/2020

## Stack
* Embedded : Jetson nano, Arduino
* Vision : Python3, Jupyter Notebook, Tensorflow 2.0
* Navigation : C++, ROS, Android studio

## Pre-requisties
|  <center>Requirement</center> |  <center>Description</center> |  
|:--------|:--------:|
|**ZED2** | <center>camera sensor</center> |
|**ydlidar** | <center>Lidar sensor for test</center> |
|**ROS_melodic** | <center>We need melodic version of ROS, because of ubuntu</center> |
|**Jetson_Nano** | <center>Main embedded, which uses ubuntu 18.04</center> |
|**python** | <center>v3.6 or higher</center> |
|**opencv** | <center>v4.1.1 or higher</center> |
|**tensorflow** | <center>v1.13.0 or higher</center> |
|**git** | <center>We follow github flow</center> |

***

## Test Project List
* [cartographer](https://github.com/seraaaayeo/SellyDev/tree/cartographer) : 2D SLAM based on LIDAR sensor
* [selly_vision](https://github.com/seraaaayeo/SellyDev/tree/selly_vision) : Proto Image analysis to aviod obstacle
* [software](https://github.com/seraaaayeo/SellyDev/tree/software) : lidar, rasberry camera, arduino motor test codes and Practice code about auto-driving robot
* [selly_motor](https://github.com/seraaaayeo/SellyDev/tree/selly_motor) : arduino ROS subscriber and jetson nano ROS publisher, which controll motor

***

## To-do Project List
* navigation
* selly_service
* ~selly_motorControl~

