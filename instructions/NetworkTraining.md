## Training a network to predict driving actions from images
_Note: you may want to work together as a team on this section, or you may want to split up and have some of the team investigate the stop sign detection._

It's time to train your neural network! There are generally a number of important steps required here:
1. Loading and preparing your train and test dataset
2. Selecting a neural network architecture
3. Initialising a loss function and optimizer for training
4. Training your network
5. Testing performance on the test dataset
6. Saving the optimal network weights

You will be using PyTorch to complete these steps. An amazing resource to guide you through this process is this [pytorch tutorial on training a classifier](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). You can also read the sub-sections below if you need some guidance on these steps.

### 1. Loading and preparing your train and test dataset
Remember that the training data you have collected is saved as "<im_number><steering_angle>.jpg" in the "data/train" folder. We have created a custom dataset class for you to make it easier to load in the images and extract the steering angle. This custom dataset also works nicely with the pytorch DataLoader, which can effectively batch up the dataset and shuffle it during training. 

The custom dataset can be found in ```scripts/steerDS.py```. You can run the following script to see how to use the custom dataset with a DataLoader:

```python scripts/train_net.py```

This should print the number of images in the train dataset, and print an example image shape, and print the ground-truth steering angles in your dataset and their respective counts.

Things to consider:
- **What will your network predict?** Will you train your network to regress the steering angle? Or, will you train it to predict a classification (e.g. 'right', 'straight', 'left')? We would recommend predicting a classification, as this will allow to you follow the pytorch tutorial fairly closely and is an effective but simple approach. However, to do this, you'll need to make sure that you convert the dataset steering angle into the correct category.
- **How balanced is your dataset?** Do you have balanced training data in terms of your ground-truth steering angles? e.g. if 80% of your data is labelled as 'straight' or steering_angle 0.0, your network may have learnt to always go straight.
- **Image augmentation and transformations?** You should consider applying additional transformations to your dataset. To identify useful transformation, it may be helpful to visually inspect the data. For example:
  - do you need a high-resolution image, or can you down-sample the image to make the network run more efficiently?
  - do you need the entire image, or can you only take the bottom half that contains the track?
  - can you flip images horizontally, as well as the steering angle, to create more data?

### 2. Design a neural network architecture.
See section 2 off this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). The network used in this tutorial is a good starting point that only needs minor modifications to function fairly well. It's a convolutional neural network, that works well with image data.

Things to consider:
- Match the architecture of your network with the output you selected above. For example, a regression network will have a final layer with a single output, whereas a classification network with 10 classes with have a final layer with 10 outputs.
- The size of _self.fc1_ will change depending on the input image size you use -- be prepared to adapt this. You can check what size this should be by printing ```x.size()``` right before ```x``` passes through ```self.fc1```.

### 3-5. Initialise an optimiser and loss function, train your network, and test performance on the test dataset. 
See section 3-5 off this [pytorch tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html). 

Things to consider:
- you will need to use a different loss if you are designing a regression network. [MSE Loss](https://pytorch.org/docs/stable/generated/torch.nn.MSELoss.html) may be a good starting point.
- if you have designed a classification network, you will need to adapt steerDS.py to return a class label rather than a raw steering angle

If your performance is poor, consider the following:
- during training, did you see 'healthy' loss behaviour? Do you need to experiment with different learning rates?
- do you have enough training data?
- do you have balanced training data? e.g. if 80% of your data is labelled as 'straight', your network may have learnt to always go 'straight'.
- do you need to try cropping input images, or down-sizing input images?

**If you are stuck, come chat to one of the workshop organisers and we're happy to help.**

### 6. Saving the optimal network weights
Once you are happy with the performance of your network on the test data, make sure to save the weights! You can use the following command to do this:

``` torch.save(net.state_dict(), "steerNet.pth") ```

Now you can finally deploy your network on the robot and test the performance!
