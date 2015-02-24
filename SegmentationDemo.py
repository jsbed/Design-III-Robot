import cv2
import time

from Robot.configuration.config import Config
from Robot.locators.segmentation.blue_cube_segmentor import BlueCubeSegmentor
from Robot.locators.segmentation.green_cube_segmentor import GreenCubeSegmentor
from Robot.locators.segmentation.red_cube_segmentor import RedCubeSegmentor
from Robot.locators.segmentation.yellow_cube_segmentor import YellowCubeSegmentor


Config("Robot/config.ini").load_config()

captObj = cv2.VideoCapture(cv2.CAP_OPENNI)

# Necessaire pour assurer une initialisation correcte
flags, img = captObj.read()
time.sleep(1)
segmentor = BlueCubeSegmentor()

while True:
    # On recupere une nouvelle image
    captObj.grab()

    # On va chercher les infos
    flags_i, img_bgr = captObj.retrieve(None, cv2.CAP_OPENNI_BGR_IMAGE)

    if not flags_i:
        continue

    cc = cv2.waitKey(10)

    if cc == 1048625:
        segmentor = BlueCubeSegmentor()
    elif cc == 1048626:
        segmentor = GreenCubeSegmentor()
    elif cc == 1048627:
        segmentor = YellowCubeSegmentor()
    elif cc == 1048628:
        segmentor = RedCubeSegmentor()

    cv2.imshow("original", img_bgr)
    cv2.imshow("Segmentation", segmentor.extract_cube(img_bgr))


cv2.destroyAllWindows()