#!/usr/bin/env python3
import time
import click
import math
import cv2
import os
import sys
import numpy as np
import torch
import torch.nn as nn

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_path, "../PenguinPi-robot/software/python/client/")))
from pibot_client import PiBot

bot = PiBot('192.168.50.5')
# stop the robot 
bot.setVelocity(0, 0)

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
        img = bot.getImage()

        #TO DO: apply any image transformations

        #TO DO: pass image through network to get a prediction for the steering angle
        
        angle = np.clip(angle, -0.5, 0.5)
        Kd = 30 #base wheel speeds, increase to go faster, decrease to go slower
        Ka = 30 #how fast to turn when given an angle
        left  = int(Kd + Ka*angle)
        right = int(Kd - Ka*angle)
        
        bot.setVelocity(left, right)
        
        
except KeyboardInterrupt:    
    bot.setVelocity(0, 0)
