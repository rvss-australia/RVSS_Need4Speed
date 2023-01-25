There is a script on the robot that can be used to collect and label data. This script allows you to use keyboard controls to control the motion of the robot; at every time step, the robot takes a photo and saves the steering angle at that time. Be aware: this means the training data for your network is controlled by how well you can drive the robot!

Find it at RVSS2019-WS/on_robot/collect_data/collect.py.

**IMPORTANT: If you interrupt the script but want to restart it to collect more data, make sure to change the starting image Id so that you don't overwrite the data you have already collected! Change the 'lead' variable on line 39.**

The _**more data and the more diverse data**_ you collect, the more robust and accurate your trained model should be. We managed to train the robot on only 500 images, but feel free to get more than this! 
