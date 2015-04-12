from threading import Thread
import cv2
import numpy
import os

from Robot.configuration.config import Config
from Robot.utilities.singleton import Singleton


class Camera(metaclass=Singleton):

    def __init__(self):
        self._capturing = False
        self._img = numpy.zeros((480, 640))

        mask_path = os.path.join(os.path.dirname(__file__), "masks",
                                 "camera.jpg")
        self._cam_mask = cv2.imread(mask_path, 0)

    def start(self):
        print("starting cam")
        Thread(target=self._video_capture).start()

    def stop(self):
        print("stoping cam")
        self._capturing = False

    def _video_capture(self):
        print("cam running")
        self._capture = cv2.VideoCapture(Config().get_camera_index())
        self._capturing = True

        while(1):
            if (self._capturing):
                captured, frame = self._capture.read()

                if captured:
                    # Apply mask
                    self._img = cv2.bitwise_and(frame, frame,
                                                mask=self._cam_mask)
            else:
                self._img = numpy.zeros((480, 640))
                break

        self._capture.release()
        print("cam released")

    def get_data(self):
        return self._img
