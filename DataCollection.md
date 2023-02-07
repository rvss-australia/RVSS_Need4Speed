There is a script on the robot that can be used to collect and label data. This script allows you to use keyboard controls to drive the robot along a track.

At every time step, the robot takes a photo and saves the steering angle of the robot at that time. Be aware: this means the training data for your network is controlled by how well you can drive the robot!

Find it at RVSS2019-WS/on_robot/collect_data/collect.py.

``` python  RVSS2019-WS/on_robot/collect_data/collect.py```

A little window will pop up, and if this is in focus, you can use the following commands:
- Tap left arrow key: steer a little more left
- Tap right arrow key: steer a little more right 
- Tap up or down arrow key: drive straight
- Space bar: close script

You can adapt the base speed and turning speed of the robot by editing lines 60-61. The _angle_ variable also will influence the turning speed. Feel free to adapt this script as you see fit.

**IMPORTANT: If you interrupt the script but want to restart it to collect more data, make sure to change the starting im_number variable on Line 36 so that you don't overwrite the data you have already collected! **

The _**more data and the more diverse data**_ you collect, the more robust and accurate your trained model should be. We managed to train the robot after collecting only 300 images, but feel free to get more than this! 
