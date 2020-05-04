import numpy as np
import requests
import time
data = np.load("video_data.npz")
data = data["arr_0"]

img = data[:,0,:,:,:]
point_cloud = data[:,1,:,:,:]

url = "http://127.0.0.1:5000/vision_angle"

for i in range(100):
    start = time.time()
    frame =  np.array((img[i], point_cloud[i]), dtype=np.float32).tobytes()
    files = {'file': frame}
    response = requests.post(url, files=files)
    print(response.text)
    print(time.time() - start)
