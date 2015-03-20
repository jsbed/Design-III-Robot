from threading import Thread
import cv2
import os
import time

from Robot.configuration.config import Config
from Robot.utilities.singleton import Singleton


class Kinect(metaclass=Singleton):

    def __init__(self):
        self._capturing = False
        self._img_bgr = []
        self._img_depth = []

        mask_path = os.path.join(os.path.dirname(__file__),
                                 Config().get_kinect_mask_img_path())
        self._table_mask = cv2.imread(mask_path, 0)

    def start(self):
        Thread(target=self._start_video_capture).start()

    def stop(self):
        self._capturing = False

    def _start_video_capture(self):
        self._capturing = True
        self._capture = cv2.VideoCapture(cv2.CAP_OPENNI)

        # Necessary to assure a successful initialization
        self._capture.read()
        time.sleep(1)

        # Run the video capture
        self._video_capture()

        # Release when finished
        self._capture.release()

    def _video_capture(self):
        while(1):
            if (self._capturing):
                # Grab new img
                self._capture.grab()

                flags_bgr, img_bgr = self._capture.retrieve(
                    None, cv2.CAP_OPENNI_BGR_IMAGE)
                flags_depth, img_depth = self._capture.retrieve(
                    None, cv2.CAP_OPENNI_POINT_CLOUD_MAP)

                # Updates bgr and depth img
                if flags_bgr and flags_depth:
                    self._img_bgr = cv2.bitwise_and(img_bgr, img_bgr,
                                                    mask=self._table_mask)
                    self._img_depth = img_depth

            else:
                self._img_bgr = []
                self._img_depth = []
                break

    def get_data(self):
        return self._img_bgr, self._img_depth
