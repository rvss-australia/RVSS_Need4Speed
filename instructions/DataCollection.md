## Gathering the training and testing data

To complete the task, you need to train a deep neural network to drive around the track. This will require data that contains an input (in this case an image), as well as an associated action (in this case a driving-related action).

You're going to collect this data by teleoperating the robot around a track. Be aware: this means the training data for your network is controlled by how well you can drive the robot!

#### Data Collection script
We are providing you with a script that can be used to collect and label data by using keyboard controls to drive the robot along a track. At every time step, the robot takes a photo and saves the steering angle of the robot at that time. 

To run the script, navigate to the workshop repository and run:

``` python scripts/collect.py --ip xxx.xxx.xx.x --folder <folder_name>```

**READ BEFORE RUNNING:**
- You should create a sample driving track for your data collection. Ideally, this should contain a selection of the driving track tiles, and include a range of driving track shapes (i.e. not just a straight track with a single curve).
- The script combines a steering angle with a base speed and turning speed to control the motor velocities. You can adapt these in the script if you want to change how fast the robot drives around the track, though generally it is good to stick with a lower speed initially as you refine your driving.
- When you start the script, the terminal will display a count-down: "Get ready....3....2...1...GO!". The robot will then start moving.
- You should use the following commands to control the steering angle of the robot:
  - tap left arrow key: steer a little more left
  - tap right arrow key: steer a little more right
  - tap up or down arrow key: drive straight
  - tap space bar: stop moving and end script
- The script will save images inside the "data/<folder_name>" folder. Initially, you should use "--folder train" to collect some data to train on. It's also important to collect a test dataset that you can use to check the performance of your neural network on unseen data. After you've collected some data in the "train" folder, consider making a "test" folder and collecting more data into this folder.
- The script will save images as "<im_number><steering_angle>.jpg". `im_number` is by default initialised to 0 when you run the script -- this means that you can accidentally overwrite previous data that you've collected if you run the script several times. If you interrupt the script but want to restart it to collect more data, you can pass in an additional ``im_num`` argument to the script that will change the starting im_number variable so that you don't overwrite the data you have already collected! e.g. ```python scripts/collect.py --ip xxx.xxx.xx.x --im_num 100```
- The _**more data and the more diverse data**_ you collect, the more robust and accurate your trained model should be. We managed to train the robot after collecting only 300 images, but feel free to get more than this! 
