# Image analysis project for object avoidance 

![ezgif com-optimize (11)](https://user-images.githubusercontent.com/52908154/81503161-18585c00-931d-11ea-8954-599d4eebb8e1.gif)

#### We will use [object detection](https://github.com/JunHyeok96/object-dection), [image segmentation](https://github.com/JunHyeok96/Road-Segmentation), and depth images to make judgments to avoid objects.  
  
  

### 1. Receive image and point cloud from camera.

<img src= "https://user-images.githubusercontent.com/52908154/81503230-68cfb980-931d-11ea-9132-758583537914.png" width="70%"></img>

### 2. Use object detection, image segmentation, depth images to determine obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/81503254-8b61d280-931d-11ea-9aa2-b9823b09553b.png" width="80%"></img>

* #### Obtain a distance within 5M of the depth image.
* #### Locate a part that is not recognized as a sidewalk in image segmentation.
* #### Locate the mobile and non-mobile objects in Use object detection.

### 3. We need to know which direction these obstacles are located.

<img src= "https://user-images.githubusercontent.com/52908154/80003038-65ee5f80-84fb-11ea-86d9-d7c403957758.png" width="40%"></img>

* #### Calculate the angle between the x and y coordinates of the obstacle and the center of the bottom.

### 4. It is now time to distinguish the types of obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/81503271-a0d6fc80-931d-11ea-8fd1-67dd5fa37f89.png" width="80%"></img>

* #### Generally, for mobile devices, avoiding preparations should be made from a distance. 
* #### Prepare to avoid objects that come in less than 5m as a result of object detection
* #### however,  For fixed things,   a closer distance can be accommodated.
* #### So the red circle, which is more than 2.5 meters away, is not marked as an obstacle.

### 5. path determination
<img src= "https://user-images.githubusercontent.com/52908154/81503290-c82dc980-931d-11ea-927b-24cd20368680.png" width="40%"></img>

* #### Indicates a movable direction based on the angle of the obstacle.




