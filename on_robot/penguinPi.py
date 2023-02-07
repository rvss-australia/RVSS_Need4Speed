import numpy as np
import requests
import cv2
import time
from threading import Thread

def set_velocity(vel0, vel1):
    r = requests.get("http://localhost:8080/robot/set/velocity?value="+str(vel0)+","+str(vel1))


def get_encoders():
    encs = requests.get("http://localhost:8080/robot/get/encoder")
    left_enc, right_enc = encs.text.split(",")
    return int(left_enc), int(right_enc)


class VideoStreamWidget(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        print('Opened capture, start thread')
        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(.01)

    def show_frame(self):
        # Display frames in main program
        cv2.imshow('frame', self.frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

