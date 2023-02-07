#!/usr/bin/env python3
import time
import click
import math
import sys
sys.path.append("..")
import cv2
import numpy as np
import penguinPi as ppi
import torch
import torch.nn as nn

# stop the robot 
ppi.set_velocity(0,0)
print("initialise camera")
camera = ppi.VideoStreamWidget('http://localhost:8080/camera/get')

#INITIALISE NETWORK HERE

#LOAD NETWORK WEIGHTS HERE

#countdown before beginning
print("Get ready...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!")

try:
    angle = 0
    while True:
        # get an image from the the robot
        image = camera.frame

        #TO DO: apply any image transformations

        #TO DO: pass image through network to get a prediction for the steering angle
        
        angle = np.clip(angle, -0.5, 0.5)
        Kd = 30 #base wheel speeds, increase to go faster, decrease to go slower
        Ka = 30 #how fast to turn when given an angle
        left  = int(Kd + Ka*angle)
        right = int(Kd - Ka*angle)
        
        ppi.set_velocity(left,right) 
        
        
except KeyboardInterrupt:    
    ppi.set_velocity(0,0)
