from flask import Flask 
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from predictMask import predictionfile

app = Flask(__name__) 
  
@app.route("/") 
def home_view():
	(labels, image) = predictMask('images/pic1.jpeg')
	return labels