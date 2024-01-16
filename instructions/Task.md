
<img src="../pics/FrontPage_Need4Speed.jpg" width="1000" height="500">

## Your task: An autonomous delivery robot!

### Driving between cities and rural environments, you must create a robot that can safely and quickly navigate Australian roads. 

To achieve this, you will deploy a deep neural network on a mobile robot. You will go through all the stages of this process: data collection and labelling, network architecture design and implementation, training and testing, and deployment on the robot. Given an RGB image from the robot's camera, you will train a deep neural network to produce a steering command that safely drives the robot along the road. 

## Your challenge:
On the day, teams will take turns testing their robot on the **qualifier track**. Each team has a 3 minute slot, where you will have one attempt and your time from that attempt is your result. The top three teams will progress to the finals and test on the **finalist track**. You will not have access to either track before the challenge. You can expect the following:

1. Each track will have a single **stop sign**. The stop sign will be placed in the middle of the track (picture below). The stop sign can be encountered on both a rural or urban track. When your robot is within 10cm of the stop sign it must come to a complete stop, before continuing to drive. 
2. The **qualifier track** can contain any of the driving track tiles provided. It will not have consecutive (in a row) 90-degree corners. It will have a single stop sign. 
3. The **finalist track** can contain any of the driving track tiles provided, in any order or configuration. It can have multiple stop signs, though these will always be at least four driving track tiles apart.
4. You will complete a single lap of each track.

**Scoring Rules:**
Your final score will be based on your delivery time (time to complete a lap), as well as any penalties or rewards you ear. It will be calculated as:

     Score = Delivery time + penalties - rewards
     
Penalties include:
- Popped tyre: if your entire tyre leaves the road surface, you blow the tyre! It will add **+1 seconds** to your time to change it.
- Bogged: if your entire robot leaves the road surface, your robot gets bogged and you'll have to help it get back on track. You can place your robot back on the road where it left, but it will add **+5 seconds** to your time.
- Run a stop sign: if you fail to come to a complete stop at a stop sign, you will be pulled over and fined by the local police. **+10 seconds** will be added to your time.

Rewards include:
- City's Safest Driver: You didn't get any penalties! Your robot is the city's safest driver. **-5 seconds** will be removed from your time.

## You will be provided with:
A range of sample track tiles, a stick-on stop sign, a robot, this repository, and occasional guidance from Tobi, Dimity and Jack (the workshop organisers). The rest is up to you!

## On the Day
The order will be randomly chosen and shared here on the evening before the challenge. 

