
<img src="pics/FrontPage_Need4Speed.jpg" width="1000" height="500">

## Your task: A robot to revolutionize the delivery process across Australia

### Driving between cities and rural environments, you must create a robot that can safely and quickly navigate Australian roads. 


To achieve this, you will deploy a deep neural network on a mobile robot. You will go through all the stages of this process: data collection and labelling, network architecture design and implementation, training and testing, and deployment on the robot. Given an RGB image from the robot's camera, you will train a deep neural network to produce a steering command that safely drives the robot along the road. 

## Choose one of the following challenges:
1. *The well-trodden path*: Your robot will only drive on 'suburban' roads, and will not encounter any unexpected obstacles. While this path may be less challenging, it's also longer -- you will need to complete 2 laps before arriving at your destination.
2. *The scenic route*: Your robot will drive on 'suburban' and 'rural' roads, albeit fairly well-frequented rural roads. You do not expect to encounter any wildlife on the rural roads. This route will need 1.5 laps before you arrive at your destination.
3. *The off-road experience*: Your robot will drive on 'suburban' and 'rural' roads, with no concern for roadworks or unruly wildlife. You may encounter road signs or animals on the edge of the road, and will need to detour slightly off-road to avoid them. The bonus: you only need to complete 1 lap, and your 4WD tyres won't pop when you go off-road. The challenge: if you hit a road sign or animal, you'll have added time to assess the damage!

**Scoring Rules:**
Your delivery time will be the ultimate predictor of performance! It will be calculated as:

     Score = Driving time + penalties
     
Penalties include:
- Popped tyre (only relevant for the well-trodden path and the scenic route): if your entire tyre leaves the road surface, you blow the tyre! It will add **+3 seconds** to your time to change it.
- Bogged (relevant for all challenges): if your entire robot leaves the road surface, your robot gets bogged and you'll have to help it get back on track. You can place your robot back on the road where it left, but it will add **+7 seconds** to your time.
- Roadkill (only relevant for the off-road experience): if you hit any wildlife or road signs, your robot will have to assess itself for damage and report the incident to the road-cleanup crew. **+5 seconds** will be added to your time.
