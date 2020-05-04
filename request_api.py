import numpy as np
import requests
import time
data = np.load("video_data.npz")
data = data["arr_0"]

img = data[:,0,:,:,:]
point_cloud = data[:,1,:,:,:]

angle_url = "http://127.0.0.1:5000/vision_angle"
img_url = "http://127.0.0.1:5000/vision_img"

def angle_receiver(img, point_cloud):
    frame =  np.array((img, point_cloud), dtype=np.float32).tobytes()
    files = {'file': frame}
    response = requests.post(angle_url, files=files)
    return response.text

def img_receiver(img, point_cloud):
    frame =  np.array((img, point_cloud), dtype=np.float32).tobytes()
    files = {'file': frame}
    response = requests.post(img_url, files=files)
    return response

print(img_receiver(img[0], point_cloud[0]))

'''i=0
while True:
    start = time.time()
    print(angle_receiver(img[i], point_cloud[i]))
    print(time.time() - start)
    i+=1'''