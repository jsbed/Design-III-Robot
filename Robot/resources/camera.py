from threading import Thread
import cv2
import numpy

from Robot.utilities.singleton import Singleton


CAMERA_INDEX = 1


class Camera(metaclass=Singleton):

    def __init__(self):
        self._capturing = False
        self._img = numpy.zeros((480, 640))

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
                self._img = numpy.zeros((480, 640))
                break

        self._capture.release()

    def get_data(self):
        return self._img
