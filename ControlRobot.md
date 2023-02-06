#### To connect to the robot with your laptop, follow these steps:
1. Turn the robot on with the switch on it's side.
2. Wait until the WMAC address appears on the robot's OLED screen. The final 6 characters of the WMAC address (xxxxxx) will complete the wireless hotspot name your robot is broadcasting. Connect your personal laptop to the appropriate WiFi hotspot, i.e. penguinpi:xx:xx:xx. The password for the wireless hotspot is egb439123
3. In a terminal window, SSH to the robot with the command below. Note: the -X command is important, please make sure you use this!
```ssh -X pi@192.168.50.5```
5. When prompted, enter password: PenguinPi 

#### Check the connection!
In the terminal where you have SSH'ed to the robot, navigate to ~/RVSS2019-WS/on_robot/ folder and get ready to run test_camera_motors.py

This will check that the camera can take an image (validate by looking for reasonable, non-zero image width and height), and will turn on each motor, one at a time. Make sure you're holding your robot so it doesn't drive off a table. 

``` python test_camera_motors.py ```

If your motor doesn't spin or no image shape prints, let one of the workshop organisers know as your robot may be faulty.

#### How to turn off the robot:
1. In the terminal that is connected to the robot, type 'sudo halt'.
2. On the front of the robot, there is a little green light, next to a red light. After you type in 'sudo halt', wait for the message 'Turn Raspberry Pi off safely' **AND** for this green light to be off. Note: after typing 'sudo halt', the LED will flash, then turn solid, then finally turn off after this this pattern. It is now safe to turn off the robot with the side switch.
