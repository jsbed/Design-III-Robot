from threading import Thread
import cv2
import numpy

from Robot.configuration.config import Config
from Robot.utilities.singleton import Singleton


class Camera(metaclass=Singleton):

    def __init__(self):
        self._capturing = False
        self._img = numpy.zeros((480, 640))

    def start(self):
        Thread(target=self._video_capture).start()

    def stop(self):
        self._capturing = False

    def _video_capture(self):
        self._capture = cv2.VideoCapture(Config().get_camera_index())
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
