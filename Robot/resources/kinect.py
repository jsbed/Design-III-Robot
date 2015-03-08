from threading import Thread
import cv2
import time

from Robot.utilities.singleton import Singleton


class Kinect(metaclass=Singleton):

    def __init__(self):
        self._capturing = False
        self._img_bgr = []
        self._img_depth = []

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
                    self._img_bgr = img_bgr
                    self._img_depth = img_depth

            else:
                break

    def get_data(self):
        return self._img_bgr, self._img_depth
