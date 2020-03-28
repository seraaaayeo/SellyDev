import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

label_rgb =dict()
label_rgb["background"] = np.array([0, 0, 0])
label_rgb["sidewalk_blocks"] = np.array([0, 0, 255])
label_rgb["sidewalk_cement"] = np.array([217, 217, 217])
label_rgb["sidewalk_urethane"] = np.array([198, 89, 17])
label_rgb["sidewalk_asphalt"] = np.array([128, 128, 128])
label_rgb["sidewalk_soil_stone"] = np.array([255, 230, 153])
label_rgb["sidewalk_damaged"] = np.array([55, 86, 35])
label_rgb["sidewalk_other"] = np.array([110, 168, 70])
label_rgb["braille_guide_blocks_normal"] = np.array([255, 255, 0])
label_rgb["braille_guide_blocks_damaged"] = np.array([128, 96, 0])
label_rgb["roadway_normal"] = np.array([255, 128, 255])
label_rgb["roadway_crosswalk"] =np.array([255, 0, 255])
label_rgb["alley_normal"] = np.array([230, 170, 255])
label_rgb["alley_crosswalk"] = np.array([208, 88, 255])
label_rgb["alley_speed_bump"] = np.array([138, 60, 200])
label_rgb["alley_damaged"] = np.array([88, 38, 128])
label_rgb["bike_lane_normal"] = np.array([255, 155, 155])
label_rgb[ "caution_zone_stairs"] = np.array([255, 192, 0])
label_rgb[ "caution_zone_manhole"] = np.array([255, 0, 0])
label_rgb[ "caution_zone_tree_zone"] = np.array([0, 255, 0])
label_rgb[ "caution_zone_grating"] = np.array([255, 128, 0])
label_rgb[ "caution_zone_repair_zone"] = np.array([105, 105, 255])

def train_images():
    top_foloder = "./data/"
    total_train_images = list()
    data_folder = os.listdir(top_foloder)
    for foloder_name in data_folder:
        images = [top_foloder+foloder_name+"/"+img for img in os.listdir(top_foloder+foloder_name) if img.endswith(".jpg")]
        total_train_images.extend(images)
    total_train_images.sort()
    return total_train_images

def mask_images():
    top_foloder = "./data/"
    total_mask_images = list()
    mask_folder = os.listdir(top_foloder)
    for foloder_name in mask_folder:
        masks = [top_foloder+foloder_name+"/MASK/"+"/"+img for img in os.listdir(top_foloder+foloder_name+"/MASK/") if img.endswith(".png")]
        total_mask_images.extend(masks)
    total_mask_images.sort()
    return total_mask_images

def load_data(image_width, image_height, batch_size):
    train_list = train_images()
    mask_list = mask_images()
    train_img = [cv2.resize(cv2.imread(path), (image_height, image_width)) for path in train_list[:batch_size]]
    mask_img = [cv2.resize(cv2.imread(path), (image_height, image_width)) for path in mask_list[:batch_size]]
    mask_img = convert_class(mask_img)
    train_img = list(map(lambda x : x/255.0, train_img))
    train_x, train_y, label_x, label_y   =train_test_split(train_img, mask_img, test_size=0.25, random_state=42)
    train_x = np.array(train_x)
    train_y = np.array(train_y)
    label_x = np.array(label_x)
    label_y = np.array(label_y)
    return train_x, train_y, label_x, label_y 

def convert_class(label_img):
    for idx, key in enumerate(label_rgb.keys()):
        for i in range(len(label_img)):
            label_img[i][(label_img[i]==label_rgb[key]).all(axis=2)] = idx
    label_img = np.array(label_img)
    label_img = label_img[:,:,:,0]
    label_img = label_img[..., tf.newaxis]
    return label_img