We have created a custom dataset class for you, to make it easier to load in the images and use them with the pytorch DataLoader. This custom dataset class, along with a test() function that shows how to use it.

Navigate to the workshop repository (RVSS_Need4Speed) and run:

```python steer_net/steerDS.py```

This should print the number of images in the dataset, and print an example image shape and matching ground-truth steering angle label.

## Design and Train Your Network
### Data curation
1. _Collating Training, Validation and Testing Data_


You should have, at the very least, a distinct training and testing dataset. This will allow you to get a sense of the performance of your network after training -- whether it has overfit to the training data, or whether it can generalise to the test data. You may choose to create sub-folders in the data folder to place images into these categories. 

2. _Image augmentation and transformations_


What is a reasonable input image size? Does it make sense to use the entire image, or should you use a crop from the image? Are there any clever transformations you can do to your existing dataset to augment it and create more images? HINT: if you have an image where the robot was steering left, if you mirror this image, can you infer what the new steering image would be?

To answer some of these questions, it may be helpful to visually inspect the data.

### Design and train a network
All training will take place on your personal laptops. We would recommend following this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html) for building and training your network for the first time. Sections 2, 3, 4, and 5 should be particularly helpful.

1. _Design a network_

See section 2 off this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). This is a good starting point that only needs minor modifications to function fairly well. 
Consider:
Do you want a classification network (e.g. predict 'left', 'right', or 'straight') or a regression network (predict the exact steering angle)? For a classification network, the final layer should have the same size output as the number of classes you will be sorting the data into. For a regression network, the final layer should have a single output. 

Note:
The size of _self.fc1_ will change depending on the input image size you use -- be prepared to adapt this.

2. _Train your network_

See section 3-5 off this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). 

Notes:
- you will need to use a different loss if you are designing a regression network. [MSE Loss](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html) may be a good starting point.
- if you have designed a classification network, you will need to adapt steerDS.py to return a class label rather than a raw steering angle

3. _Check for reasonable performance on your test dataset_

See section 5 off this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). 

If your performance is poor, consider the following:
- during training, did you see 'healthy' loss behaviour? Do you need to experiment with different learning rates?
- do you have enough training data?
- do you have balanced training data? e.g. if 80% of your data is labelled as 'straight', your network may have learnt to always go 'straight'.
- do you need to try cropping input images, or down-sizing input images?

**If you are really stuck, come chat to one of the workshop organisers.**

4. _Saving the network weights_
Once your network has finished training and you are satisfied with the performance on the test data, make sure to save the weights! For a network named steerNet, you can use the following command to do this:

``` torch.save(net.state_dict(), "steerNet.pt") ```

Now you can finally deploy your network on the robot and test the performance!
