### Create a deployment file.
We have adapted the script for collecting data to a deployment script in ```~/RVSS_Need4Speed/deploy.py```.

You will need to update this to use your network (loaded with your trained weights) to predict how the robot should move, and send this as a command to the motors. 

Things to update:
1. Make sure that you don't use the raw camera image in the network, unless this is how you trained your network! Do you need to: crop the image? resize the image? normalize the image?
2. Make sure you load the correct network definition and initialise the network with the saved training weights. See [section 5 of this tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html).
3. How do you go from the network prediction to a steering angle? If you have designed a regression network, this should be fairly trivial. If you have designed a classification network, you may need to think carefully about this. Do the predictions act similar to a keyboard press?

### Test the robot on a track.
Now you're ready to test the robot on some road configurations! Remember, you're being assessed on how quickly and accurately the robot can follow the road. If you're not happy with your robot's performance, try to figure out why. Sometimes it can be helpful to notice when the robot fails. Here are some potential hints for things to check if your robot is not performing well:
* Is your robot seeing data that is different to what you trained it on?
  * maybe you were a great driver, and never showed it edge cases so it could learn recovery behaviour?
  * are you applying the data transformations that you used during training?
  * how diverse was the data you trained on?
* How are you converting your network steering predictions into a robot steering command?
