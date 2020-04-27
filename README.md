# Image analysis project for object avoidance 

![ezgif com-optimize (3)](https://user-images.githubusercontent.com/52908154/79710635-97e7a200-8300-11ea-8067-691b4fd930e0.gif)

#### We will use object detection, [image segmentation](https://github.com/JunHyeok96/Road-Segmentation), and depth images to make judgments to avoid objects.  
  
  

### 1. Receive image and point cloud from camera.

<img src= "https://user-images.githubusercontent.com/52908154/80001163-05f6b980-84f9-11ea-9566-101b69783483.png" width="70%"></img>

### 2. Use object detection, image segmentation, depth images to determine obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/80002651-dd6fbf00-84fa-11ea-9849-f119be3d8e30.png" width="80%"></img>

* #### Obtain a distance within 5M of the depth image.
* #### Locate a part that is not recognized as a sidewalk in image segmentation.
* #### Locate the mobile and non-mobile objects in Use object detection.

### 3. We need to know which direction these obstacles are located.

<img src= "https://user-images.githubusercontent.com/52908154/80003038-65ee5f80-84fb-11ea-86d9-d7c403957758.png" width="40%"></img>

* #### Calculate the angle between the x and y coordinates of the obstacle and the center of the bottom.

### 4. It is now time to distinguish the types of obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/80003326-d1d0c800-84fb-11ea-881c-5ac8f26b9c9b.png" width="80%"></img>

* #### Generally, for mobile devices, avoiding preparations should be made from a distance. 
* #### Prepare to avoid objects that come in less than 5m as a result of object detection
* #### however,  For fixed things,   a closer distance can be accommodated.
* #### So the red circle, which is more than 2.5 meters away, is not marked as an obstacle.

### 5. path determination
<img src= "https://user-images.githubusercontent.com/52908154/80003782-77843700-84fc-11ea-8fae-32806499a355.png" width="40%"></img>

* #### Indicates a movable direction based on the angle of the obstacle.




