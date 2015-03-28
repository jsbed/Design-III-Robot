import cv2

from Robot.configuration.config import Config
from Robot.locators import robot_locator
from Robot.locators.extractors.robot_corner import robot_corner_extractor_factory,\
    blue_robot_corner_extractor
from Robot.locators.extractors.robot_corner.blue_robot_corner_extractor import BlueRobotCornerExtractor
from Robot.locators.extractors.robot_corner.orange_robot_corner_extractor import OrangeRobotCornerExtractor
from Robot.locators.extractors.robot_corner.pink_robot_corner_extractor import PinkRobotCornerExtractor
from Robot.resources.kinect import Kinect


Config().load_config()

Kinect().start()

while(1):
    cc = cv2.waitKey(1)
    bgr, depth = Kinect().get_data()
    # try:
    #blue = BlueRobotCornerExtractor().extract(bgr)
    #pink = PinkRobotCornerExtractor().extract(bgr)
    #orange = OrangeRobotCornerExtractor().extract(bgr)
    #median = cv2.medianBlur(bgr, 21)
    #bil = cv2.bilateralFilter(bgr, 10, 30, 30)
    #cv2.imshow("blue", blue)
    #cv2.imshow("pink", pink)
    #cv2.imshow("orange", orange)
    #cv2.imshow("median", median)
    #cv2.imshow("bil", bil)
    # except:
    #    pass

    cv2.imshow("img", bgr)

    #cv2.imshow("cloud", depth)

    localization = robot_locator.localize()

    if (localization.unknown):
        pass
        #print("robot location unknown")
    else:
        print(localization.position,
              localization.orientation,
              localization.orientation % 45)

    if cc == 10:  # Enter to stop
        Kinect().stop()
        break

cv2.destroyAllWindows()
