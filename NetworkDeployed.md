### Move the trained weights from your laptop to the robot.
You can copy the network weights to the robot by executing the following command from the saved directory on your laptop:

``` scp steerNet.pt pi@192.168.50.5:~/RVSS_Need4Speed/on_robot/deploy/ ```

You will also need to copy any files that contain the network definition to the robot in a similar manner.

### Create a deployment file.
We have copied the script for collecting data to a deployment script in ```/RVSS_Need4Speed/on_robot/deploy/deploy.py```.

You will need to adapt this to use your network (loaded with your trained weights) to predict how the robot should move, and send this as a command to the motors. 

1. Make sure that you don't use the raw camera image in the network, unless this is how you trained your network! Do you need to: crop the image? resize the image?
2. Make sure you load the correct network definition and initialise the network with the saved training weights. See [section 5 of this tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html).
3. How do you go from the network prediction to a steering angle? If you have designed a regression network, this should be fairly trivial. If you have designed a classification network, you may need to think carefully about this. Do the predictions act similar to a keyboard press?

### Test the robot on a track.
Now you're ready to test the robot on some road configurations! Remember, you're being assessed on how quickly and accurately the robot can follow the road. If you're not happy with your robot's performance, try to figure out why. Is the controller for different steering commands the problem? Or is it the output from the network - is the network not generalising to the deployment environment?
