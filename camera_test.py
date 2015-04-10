import cv2

from Robot.configuration.config import Config
from Robot.resources.camera import Camera


Config().load_config()

Camera().start()

while(1):
    cc = cv2.waitKey(1)
    cv2.imshow("img", Camera().get_data())

    if cc == 10:  # Enter to stop
        Camera().stop()
        break

cv2.destroyAllWindows()
