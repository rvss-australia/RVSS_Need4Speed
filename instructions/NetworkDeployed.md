## Test your robot's ability to drive autonomously.

By now, you should have a trained neural network that can take an image and predict a steering action. Optionally, you should also have developed a function that allows you to identify stop signs on the road (if you want to avoid the stop sign penalty!). It's time to put these together to deploy your robot on the road!

### A deploy script to control your robot
We have created a script that you can use to deploy your robot in ```scripts/deploy.py```. Read through this script and follow the instructions to complete your robot's deployment. 

Things to consider:
1. What transformations do you need to apply before providing the pi bot image to your network? For example, cropping, resizing or normalizing the image? Check what you used during training.
2. Make sure you load the correct network definition and initialise the network with the saved training weights. See section 5 of [this tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html).
3. How do you go from the network prediction to a steering angle? If you have designed a regression network, this should be fairly trivial. If you have designed a classification network, you may need to think carefully about this. Do the predictions act similar to a keyboard press?
4. How will you implement your stop sign detector into the action process of the robot? For example -- how do you make sure it comes to a complete stop, and how do you make sure this doesn't trigger over and over?
5. Make sure you pass in your robot's wlan ip with the ```--ip``` argument.

### Test your robot on a track
Now you're ready to test the robot on some road configurations! Remember, you're being assessed on how quickly and accurately the robot can follow the road. If you're not happy with your robot's performance, try to figure out why. Sometimes it can be helpful to notice when the robot fails. Here are some potential hints for things to check if your robot is not performing well:
* Is your robot seeing data that is different to what you trained it on?
  * maybe you were a great driver, and never showed it edge cases so it could learn recovery behaviour?
  * are you applying the data transformations that you used during training?
  * how diverse was the data you trained on?
* How are you converting your network steering predictions into a robot steering command?
