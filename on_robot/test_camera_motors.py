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
    camera = ppi.CameraPiBot()
    print("capture image")
    image = camera.get_image()
    print("image size %d by %d" % (image.shape[0],image.shape[1]))
    start = time.time()
    for i in range(100):
        image = camera.get_image()
    end = time.time()
    print("frame rate is %.3f fps" % (100/(end-start)))
