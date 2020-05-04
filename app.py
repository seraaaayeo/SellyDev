#-*- coding:utf-8 -*-
from flask import Flask, request, jsonify
import numpy as np
from selly_vision_api import *

app = Flask(__name__)

@app.route('/vision_angle', methods=['POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        result = selly_vision(img_bytes)
    print(result)
    return str(result)
