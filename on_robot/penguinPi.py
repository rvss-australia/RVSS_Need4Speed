import numpy as np
import requests
import cv2      
from picamera import PiCamera
import time

def set_velocity(vel0, vel1):
    r = requests.get("http://localhost:8080/robot/set/velocity?value="+str(vel0)+","+str(vel1))


class CameraPiBot():
    def __init__(self, framerate = 30, resolution = (160, 128)):
        self.framerate = framerate
        self.resolution = resolution

        self.camera = PiCamera(framerate = self.framerate)
        self.camera.resolution = self.resolution

        time.sleep(2) #give camera time to setup and change resolution

    def get_image(self):
        img = np.empty((self.resolution[1]*self.resolution[0]*3,), dtype = np.uint8)
        self.camera.capture(img, "bgr", use_video_port=True)
        img = img.reshape((self.resolution[1], self.resolution[0], 3)) 
        img = img[::-1, ::-1] #image will be upside down

        return img