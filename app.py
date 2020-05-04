#-*- coding:utf-8 -*-
from flask import Flask, request, jsonify, send_file
import numpy as np
from selly_vision_api import *
from PIL import Image

app = Flask(__name__)

@app.route('/vision_angle', methods=['POST'])
def vision_angle():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        result = selly_vision(img_bytes)[1]
    print("send!")
    return str(result)

@app.route('/vision_img', methods=['POST'])
def vision_img():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        result = selly_vision(img_bytes)[0]
        result = result.tobytes()
        image = Image.open(result)
    print("send!")
    return send_file(
                     image,
                     attachment_filename='result.jpeg',
                     mimetype='result/jpg'
               )