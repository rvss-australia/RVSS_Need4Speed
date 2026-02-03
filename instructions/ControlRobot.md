## Connect your robot to the wifi:

*Before attempting to control the robot, make sure your computer is connected to the `RVSS_Starlink` network using the password "RVSS2026".*

The robots support two external network modes:
1. **Primary mode:** The robot attempts to connect to RVSS_Starlink.
2. **Fallback mode:** If `RVSS_Starlink` is out of range, the robot creates its own local Wi-Fi network named
`PenguinPi:xx.xx.xx`, where the suffix corresponds to the last 6 characters of the robot’s WMAC, which is shown on the OLED screen.

This order can be changed; please refer to the [FAQ](#faq) section.

### Steps

1. Turn the robot on using the power switch on its side.
2. The robot will attempt to connect to Wi-Fi and display its WLAN IP address on the OLED screen.
Take note of this address (e.g. xxx.xxx.xx.x).
3. If the displayed IP address is 10.42.0.1, the robot is operating in hotspot mode.
In this mode, you will not have internet access while connected to the robot. You can then either:
    - Power-cycle the robot (see How to turn off the robot) and try again, or
    - Connect directly to the robot’s local Wi-Fi network (PenguinPi:xx.xx.xx) using the password PenguinPi.

## Check the connection!
Navigate to the `RVSS_Need4Speed` repository on your local machine and get ready to test the camera and motors on the PiBot. You will run a script that will check that the camera can take an image, and will turn on each motor, one at a time. Make sure you're holding your robot so it doesn't drive off a table. Make sure to enter the correct wlan IP address.

``` python PenguinPi-robot/software/python/client/test_camera_motors.py --ip xxx.xxx.xxx.xxx```

If your robot is working, both the wheels should spin, a non-zero image shape should print in the terminal, and you should see a window with a continuous feed from the robot camera. If this does not happen, let one of the workshop organisers know as your robot may be faulty.

You can end the script by `ctrl+c` in the terminal.

**Note: if you want to get some initial insight into how control the robot camera and motors, read through this script to see how it works.**

## How to turn off the robot:
1. On the back of the robot, there is a 'SDN' button. Press this button for 3 seconds.
2. On the front of the robot, there is a little green light, next to a red light. After you press the 'SDN' button, wait for the message 'Turn Raspberry Pi off safely' to show on the OLED screen **AND** for this green light to be off. Note: after pressing the button, the LED will flash, then turn solid, then finally turn off after this pattern. It is now safe to turn off the robot with the side switch.

## FAQ
**My PenguinPi-robot folder is empty?**

This can occur is the sub-module (PenguinPi-robot) is not correctly initialised. You can do this in two ways:
1. ```git clone --recursive https://github.com/rvss-australia/RVSS_Need4Speed.git```

or if you have already cloned the repo without the ` --recursive` argument:

2. ```git submodule init``` followed by ```git submodule update```

**I'm getting a "ModuleNotFound" error?**
Check that you have activated your pixi environment that contains the packages required for the workshop. Refer to the [preparation instructions](https://github.com/rvss-australia/RVSS_Need4Speed/blob/main/instructions/Preparation.md)

**I want to ssh onto the robot!**
You should not need to do this at any point. Please check with one of the workshop organisers before changing code directly on the PiBot. If they give you the go ahead, you can:
1. Check the robot's OLED screen to see its wlan address (xxx.xxx.xx.x).
2. In a terminal window, SSH to the robot with the command below. Note: the -X command is important, please make sure you use this!
```ssh -X pi@xxx.xxx.xx.x```
3. When prompted, enter password: PenguinPi 

**Change default connection**

In some cases the robot connection migth be laggy and unstable while using the `RVSS_Starlink` connection. you can modify the default behaviour of your robot by running the following:

- Use the command `pixi run set_hotspot ROBOT_IP`. Replace ROBOT_IP with the robot’s WLAN IP address (e.g., 192.168.1.10) to ensure the command is run in the robot.
    - you will be asked to add the host so please enter `yes` in the console.
    - When prompted, enter password: `PenguinPi`
- `pixi run set_wifi` to recover the default `RVSS_Starlink` connection.
