# Image analysis project for object avoidance 

![image](https://user-images.githubusercontent.com/52908154/83771788-9c53f880-a6bd-11ea-973e-dad678bef87f.png)
![image](https://user-images.githubusercontent.com/52908154/83771816-a4ac3380-a6bd-11ea-9630-d7e427bb8da9.png)

#### We will use [object detection](https://github.com/JunHyeok96/object-dection), [image segmentation](https://github.com/JunHyeok96/Road-Segmentation), and depth images to make judgments to avoid objects.  
  
  

### 1. Receive image and point cloud from camera.

<img src= "https://user-images.githubusercontent.com/52908154/83318785-f9415000-a272-11ea-940f-f129740a45a6.png" width="30%"></img>

### 2. Use object detection, image segmentation, depth images to determine obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/83318927-699ca100-a274-11ea-94d5-7509acbe4ca4.png" width="80%"></img>


* #### Obstacle detection begins with the assumption that the portion of the segmentation that is not recognized as a sidewalk is an obstacle.

* #### However, considering errors in segmentation, it is more efficient to detect obstacles by object detection. Object detection was designated as the first priority.

<img src= "https://user-images.githubusercontent.com/52908154/83318934-889b3300-a274-11ea-8244-ae132426f4fc.png" width="80%"></img>

* #### The y-value of the point cloud was used to limit the effective range of obstacles.

### 3. We need to know which direction these obstacles are located.

<img src= "https://user-images.githubusercontent.com/52908154/83318705-2e00d780-a272-11ea-9742-ccf78f5603e9.png" width="40%"></img>

* #### Calculate the angle corresponding to each pixel with the x and z coordinates of the point cloud.

### 4. It is now time to distinguish the types of obstacles.

<img src= "https://user-images.githubusercontent.com/52908154/83318991-1d059580-a275-11ea-9887-1d738c98220d.png" width="80%"></img>

* #### Generally, for mobile devices, avoiding preparations should be made from a distance. 
* #### however,  For fixed things,  a closer distance can be accommodated.


![image](https://user-images.githubusercontent.com/52908154/83319146-b4b7b380-a276-11ea-868c-3b00d490db66.png)

* #### Finally, the distance can be set to detect obstacles in that section. (There is no need to detect obstacles too far away.)

