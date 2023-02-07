import penguinPi as ppi
import time

if __name__ == "__main__":
    enc_begin_left, enc_begin_right = ppi.get_encoders()
    print("get encoders state at beginning:", enc_begin_left, enc_begin_right)
    print("test left motor")
    ppi.set_velocity(10,0)
    time.sleep(2)
    print("test right motor")
    ppi.set_velocity(0,10)
    time.sleep(2)
    print("stop")
    ppi.set_velocity(0,0)
    print("get encoders state at beginning")
    enc_end_left, enc_end_right = ppi.get_encoders()
    print("get encoders state at end:", enc_end_left, enc_end_right)

    print("initialise camera")
    camera = ppi.VideoStreamWidget('http://localhost:8080/camera/get')
    time.sleep(2)
    print("grab image")
    image = camera.frame
    print("image size %d by %d" % (image.shape[0],image.shape[1]))
    try:
        while True:
            image = camera.show_frame()
    except KeyboardInterrupt:
        exit()


