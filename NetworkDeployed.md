### Move the trained weights from your laptop to the robot.
You can copy the network weights to the robot by executing the following command from the saved directory on your laptop:

``` scp steerNet.pt pi@192.168.50.5:~/RVSS_Need4Speed/on_robot/deploy/ ```

### Create a deployment file.
We have copied the script for collecting data to a deployment script in ```/RVSS_Need4Speed/on_robot/deploy/deploy.py```.

You will need to adapt this to use your network (loaded with your trained weights) to predict how the robot should move, and send this as a command to the motors.

### Test the robot on a track.
Now you're ready to test the robot on some road configurations! Remember, you're being assessed on how quickly and accurately the robot can follow the road. If you're not happy with your robot's performance, try to figure out why. Is the controller for different steering commands the problem? Or is it the output from the network - do you need more data for training?
