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

