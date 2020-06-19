# Sensor_Test

* ### camera.py  
  카메라를 작동시켜 frame을 publishing한다.  
* ### lidar.py  
  라이다 센서에서 subscription한 값을 확인한다.  
* ### motor.py  
  아두이노에 motor값을 publishing한다.  
* ### detectnet.py  
  카메라를 통해 object detection한 frame을 publishing한다.  
  
  
# Delivery_robot  

* ### auto_controller.py  
  publishing된 데이터들을 종합하여 아두이노 모터를 auto controll한다.  

* ### sensor_analysis.py  
  auto_controller.py에 사용되는 모듈로서 publishing된 데이터들을 분석한다.     


# Issue  
* ### auto_controller에서 아두이노로 publishing하는 속도가 빠르기때문에 buffer가 쌓여 동작이 지연됨  
  -> motor_speed or motor_angle이 변할 때만 publishing 함  

* ### lidar sensor는 거리제한 0.12m ~ 10m를 벗어나는 경우 값이 0으로 출력됨  
  -> 0.12m 반경 안에 위치하는 것은 로봇의 프레임과 거의 밀접하게 있어야하므로 고려대상에서 제외.  
     0m값을 99m로 mapping
  
# 자율 주행 실행 방법   
```
roscore    

rosrun rosserial_python serial_node.py  _port:=/dev/ttyUSB0  #아두이노 연결 USB포트번호는 유동적

rosrun ydlidar ydlidar_node   #라이다 실행

rosrun selly camera.py #카메라 실행

rosrun selly auto_controller.py #자율 주행 실행

```
