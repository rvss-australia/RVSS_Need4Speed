#!/usr/bin/env python
import time
import sys
import os
import cv2
import numpy as np
from pynput import keyboard
import argparse

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_path, "../PenguinPi-robot/software/python/client/")))
from pibot_client import PiBot

parser = argparse.ArgumentParser(description='PiBot client')
parser.add_argument('--ip', type=str, default='localhost', help='IP address of PiBot')
parser.add_argument('--im_num', type = int, default = 0)
parser.add_argument('--folder', type = str, default = 'train')
args = parser.parse_args()

bot = PiBot(ip=args.ip)
# stop the robot

bot.setVelocity(0, 0)

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


# Initialize variables
angle = 0
im_number = args.im_num
continue_running = True

def on_press(key):
    global angle, continue_running
    try:
        if key == keyboard.Key.up:
            angle = 0
            print("straight")
        elif key == keyboard.Key.down:
            angle = 0
        elif key == keyboard.Key.right:
            print("right")
            angle += 0.1
        elif key == keyboard.Key.left:
            print("left")
            angle -= 0.1
        elif key == keyboard.Key.space:
            print("stop")
            bot.setVelocity(0, 0)
            continue_running = False
            # return False  # Stop listener

    except Exception as e:
        print(f"An error occurred: {e}")
        bot.setVelocity(0, 0)

# Start the listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while continue_running:
        # Get an image from the robot
        img = bot.getImage()
        
        angle = np.clip(angle, -0.5, 0.5)
        Kd = 20  # Base wheel speeds
        Ka = 20  # Turn speed
        left  = int(Kd + Ka*angle)
        right = int(Kd - Ka*angle)
        
        bot.setVelocity(left, right)

        cv2.imwrite(script_path+"/../data/"+args.folder+"/"+str(im_number).zfill(6)+'%.2f'%angle+".jpg", img) 
        im_number += 1

        time.sleep(0.1)  # Small delay to reduce CPU usage

    # Clean up
    bot.setVelocity(0, 0)
    listener.stop()
    print("Script ended")


except KeyboardInterrupt:    
    bot.setVelocity(0, 0)
    listener.stop()

