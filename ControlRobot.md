#### To connect to the robot with your laptop, follow these steps:
1. Turn the robot on with the switch on it's side.
2. Wait until the WMAC address appears on the robot's OLED screen. The final 6 characters of the WMAC address (xxxxxx) will complete the wireless hotspot name your robot is broadcasting. Connect your WiFi to the appropriate hotspot, i.e. penguinpi:xx:xx:xx (see the image for an example). The password for the wireless hotspot is egb439123 
3. Ssh to the robot with the command: ssh -X pi@192.168.50.5
4. When prompted, enter password: PenguinPi 

#### Check the connection!
In the terminal connected to the robot, navigate to RVSS2019-WS/on_robot/ folder and run test_camera_motors.py
This script turns on both the motors and takes an image with the camera (so make sure you're holding the robot!). 
If there are any issues when running this script, or if your motors don't spin or no image shape prints, let one of the workshop organisers know as your robot may be faulty.

#### How to turn off the robot:
1. In the terminal that is connected to the robot, type 'sudo halt'.
2. On the front of the robot, there is a little green light (see picture below). After you type in 'sudo halt', wait for the message 'Turn Raspberry Pi off safely' AND for this green light to be off. Note: after typing 'sudo halt', the LED will flash, then turn solid, then finally turn off after this this pattern.
