from flask import Flask, request
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2

app = Flask(__name__)


@app.route('/')
def showHello():
    return "hello world"
@app.route('/classifyMask', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        print("test")
