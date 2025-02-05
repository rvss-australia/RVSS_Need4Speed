#!/usr/bin/env python
import time
import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

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
bot.setVelocity(0, 0)

# Initialize variables
angle = 0
is_stopped = False
im_number = args.im_num
continue_running = True

# Create matplotlib figure before countdown
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(8,6))
ax.set_title('Press arrow keys to control\nSpace to toggle stop/start')
plt.axis('off')
fig.canvas.manager.window.raise_()  # Bring window to front

def on_key(event):
    global angle, is_stopped
    
    if event.key == 'up':
        angle = 0
    elif event.key == 'down':
        angle = 0
    elif event.key == 'right':
        angle += 0.1
    elif event.key == 'left':
        angle -= 0.1
    elif event.key == ' ':
        is_stopped = not is_stopped  # Toggle stop state
        if is_stopped:
            bot.setVelocity(0, 0)

# Connect event handler before countdown
fig.canvas.mpl_connect('key_press_event', on_key)

# countdown before beginning
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
    while continue_running:
        # Get an image from the robot
        img = bot.getImage()
        
        # Display the image in matplotlib window
        ax.clear()
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(f'Angle: {angle:.2f}')
        plt.axis('off')
        plt.draw()
        plt.pause(0.01)  # Small pause to update the plot
        
        angle = np.clip(angle, -0.5, 0.5)
        Kd = 15  # Base wheel speeds
        Ka = 15  # Turn speed
        
        if not is_stopped:
            left  = int(Kd + Ka*angle)
            right = int(Kd - Ka*angle)
            bot.setVelocity(left, right)

        cv2.imwrite(script_path+"/../data/"+args.folder+"/"+str(im_number).zfill(6)+'%.2f'%angle+".jpg", img) 
        im_number += 1

except KeyboardInterrupt:    
    bot.setVelocity(0, 0)
    plt.close()

finally:
    bot.setVelocity(0, 0)
    plt.close()

