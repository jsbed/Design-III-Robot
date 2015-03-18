from threading import Thread
import cv2
import numpy
import time


CAMERA_INDEX = 0


class Camera():

    def __init__(self):
        self._capturing = False
        self._img = []

    def start(self):
        Thread(target=self._video_capture).start()

    def stop(self):
        self._capturing = False

    def _video_capture(self):
        self._capture = cv2.VideoCapture(CAMERA_INDEX)
        self._capturing = True

        while(1):
            if (self._capturing):
                captured, frame = self._capture.read()

                if captured:
                    self._img = frame
            else:
                break

        self._capture.release()

    def get_data(self):
        return self._img

c = Camera()
c.start()

while(1):
    img = c.get_data()
    if len(img) > 0:
        cv2.imshow("test", img)
    cc = cv2.waitKey(10)

    if cc == 10:  # Touche Enter
        c.stop()
        break

print("sleeping 2 sec")
time.sleep(2)
print("finished sleep")
c.start()

while(1):
    img = c.get_data()
    if len(img) > 0:
        cv2.imshow("test", img)
    cc = cv2.waitKey(10)

    if cc == 10:  # Touche Enter
        c.stop()
        break

print("finished")
