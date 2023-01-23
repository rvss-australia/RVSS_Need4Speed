import penguinPi as ppi
import time

if __name__ == "__main__":
    print("test left motor")
    ppi.set_velocity(10,0)
    time.sleep(2)
    print("test right motor")
    ppi.set_velocity(0,10)
    time.sleep(2)
    print("stop")
    ppi.set_velocity(0,0)

    print("initialise camera")
    camera = ppi.VideoStreamWidget('http://localhost:8080/camera/get')
    time.sleep(2)
    print("grab image")
    image = camera.frame
    print("image size %d by %d" % (image.shape[0],image.shape[1]))
    
    while True:
        image = camera.show_frame()
 
