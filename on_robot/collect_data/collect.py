#!/usr/bin/env python3
import time
import click
import math
import sys
sys.path.append("..")
import cv2
import numpy as np
import penguinPi as ppi
import pygame

#~~~~~~~~~~~~ SET UP Game ~~~~~~~~~~~~~~
pygame.init()
pygame.display.set_mode((300,300)) #size of pop-up window
pygame.key.set_repeat(100) #holding a key sends continuous KEYDOWN events. Input argument is milli-seconds delay between events and controls the sensitivity
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# stop the robot 
ppi.set_velocity(0,0)
print("initialise camera")
camera = ppi.VideoStreamWidget('http://localhost:8080/camera/get')

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
    im_number = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    angle = 0
                    print("straight")
                if event.key == pygame.K_DOWN:
                    angle = 0
                if event.key == pygame.K_RIGHT:
                    print("right")
                    angle += 0.1
                if event.key == pygame.K_LEFT:
                    print("left")
                    angle -= 0.1
                if event.key == pygame.K_SPACE:
                    print("stop")                    
                    ppi.set_velocity(0,0)
                    raise KeyboardInterrupt
        
        # get an image from the the robot
        image = camera.frame
        
        angle = np.clip(angle, -0.5, 0.5)
        Kd = 30 #base wheel speeds, increase to go faster, decrease to go slower
        Ka = 30 #how fast to turn when given an angle
        left  = int(Kd + Ka*angle)
        right = int(Kd - Ka*angle)
        
        ppi.set_velocity(left,right) 

        cv2.imwrite("data/"+str(im_number).zfill(6)+'%.2f'%angle+".jpg", image) 
        im_number += 1
        
        
except KeyboardInterrupt:    
    ppi.set_velocity(0,0)