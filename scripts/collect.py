#!/usr/bin/env python
import time
import sys
import os
import cv2
import numpy as np
from pynput import keyboard
import argparse

from controller import Controller
from steer_labels import LABELS, steering_to_class
from steer_limits import clamp_angle

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_path, "../PenguinPi-robot/software/python/client/")))
from pibot_client import PiBot

parser = argparse.ArgumentParser(description='PiBot client')
parser.add_argument('--ip', type=str, default='localhost', help='IP address of PiBot')
parser.add_argument('--im_num', type = int, default = 0)
parser.add_argument('--folder', type = str, default = 'train')
args = parser.parse_args()

if not os.path.exists(script_path+"/../data/"+args.folder):
    data_path = script_path.replace('scripts', 'data')
    print(f'Folder "{args.folder}" in path {data_path} does not exist. Please create it.')
    exit()

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
label = 2
im_number = args.im_num
continue_running = True
controller = Controller()

def on_press(key):
    global angle, label, continue_running
    try:
        if key == keyboard.Key.up:
            angle = 0
        elif key == keyboard.Key.down:
            angle = 0
        elif key == keyboard.Key.right:
            angle += 0.2
        elif key == keyboard.Key.left:
            angle -= 0.2
        elif key == keyboard.Key.space:
            print("Toggle stop")
            controller.toggle_stop()
        elif key == keyboard.Key.esc:
            print("Stopping script")
            continue_running = False

        angle = clamp_angle(angle)
        label = steering_to_class(angle)

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
        
        left, right = controller(label)
        controller_angle = controller.angle

        bot.setVelocity(left, right)

        label_name = LABELS[label]
        cv2.imwrite(
            script_path
            + "/../data/"
            + args.folder
            + "/"
            + str(im_number).zfill(6)
            + "_"
            + label_name
            + ".jpg",
            img,
        )
        im_number += 1

        time.sleep(0.1)  # Small delay to reduce CPU usage

    # Clean up
    bot.setVelocity(0, 0)
    listener.stop()
    print("Script ended")


except KeyboardInterrupt:    
    bot.setVelocity(0, 0)
    listener.stop()