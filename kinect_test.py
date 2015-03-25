import cv2

from Robot.configuration.config import Config
from Robot.locators import robot_locator
from Robot.resources.kinect import Kinect


Config().load_config()

Kinect().start()

while(1):
    cc = cv2.waitKey(1)
    bgr, depth = Kinect().get_data()
    cv2.imshow("img", bgr)
    #cv2.imshow("cloud", depth)

    localization = robot_locator.localize()

    if (localization.unknown):
        print("robot location unknown")
    else:
        print(localization.position,
              localization.orientation,
              localization.orientation % 45)

    if cc == 10:  # Enter to stop
        Kinect().stop()
        break

cv2.destroyAllWindows()
