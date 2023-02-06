## Clone the Repo to Your Machine

``` git clone https://github.com/dimitymiller/RVSS_Need4Speed.git```

## Design Your Network
In the Github repo, you will find an example of a possible network structure at RVSS2019-WS/on_laptop/steer_net/steerNet.py

This file contains the SteerNet class, which details an example _not very good_ network architecture. Read through the network structure: it uses convolutional layers, rectified linear units, max pooling layers and fully connected layers. 

**Regression or Classification? You pick!**

The example network is a regression network, where a single output is produced - see line 16: ```self.fc3 = nn.Linear(10,1)```, there is only 1 output from the final layer. You could follow this approach and train the network to produce the steering direction, or you could adapt the network to be a classification task, where it gives more than one output (as an example, your network could classify between three classes: 'left', 'right' or 'straight' - this would involve changing line 16: ```self.fc3 = nn.Linear(10, 3)``` to allow for 3 outputs from the final layer).

## Train Your Network
### Copy the training data to your laptop
Store the training data in the following folder: RVSS2019-WS/on_laptop/data/

You can copy the training data by executing the following command from the data folder on your laptop:

``` scp -r pi@192.168.50.5:~/RVSS_Need4Speed/on_robot/collect_data/data/* . ```

### Training
We have not provided an example training script for you, you will need to create this on your own! We recommend looking at pytorch tutorials for training classification or regression networks (depending on what you have chosen when you designed your network). You can find some example tutorials saved as pdf's on the documentation page of this website. 

We have created a custom dataset class for you, to make it easier to load in the images and use them with the pytorch DataLoader. This custom dataset class, along with a test() function that shows how to use it, is stored in RVSS2019-WS/on_laptop/steer_net/steerDS.py

Once your network has finished training, make sure to save the network weights! For a network named steerNet, you can use the following command to do this:

``` torch.save(steerNet.state_dict(), "steerNet.pt") ```

Now you can finally deploy your network on the robot and test the performance!
