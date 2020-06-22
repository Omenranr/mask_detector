from flask import Flask, request
import numpy as np
import argparse
import cv2

app = Flask(__name__)


@app.route('/')
def showHello():
    return "hello world"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
