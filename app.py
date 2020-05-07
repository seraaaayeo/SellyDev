#-*- coding:utf-8 -*-
from flask import Flask, request, jsonify, send_file
import numpy as np
from selly_vision_api import *
from PIL import Image
import base64
import io
import time

app = Flask(__name__)

@app.route('/vision_angle', methods=['POST'])
def vision_angle():
    if request.method == 'POST':
        img = request.files['img']
        img_bytes = img.read()
        point = request.files['point']
        point_bytes = point.read()
        result = selly_vision(img_bytes, point_bytes)[1]
    return str(result)

@app.route('/vision_img', methods=['POST'])
def vision_img():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        result = selly_vision(img_bytes)[0]
        img = Image.fromarray(result, 'RGB')
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
        data = {}
        data["key"] = {"result_img": encoded_img}
    print("send!")

    return jsonify(data) 