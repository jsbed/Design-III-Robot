from PySide.QtCore import QThread
import time

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication.localization.localization_dto import create_localization_dto
from Robot.locators import robot_locator


class RobotLocatorWorker(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signal = Signal()
        self._running = False

    def run(self):
        self._running = True

        while self._running:
            localization = robot_locator.localize()

            if not localization.unknown:
                localization_dto = create_localization_dto(localization)
                self.signal.custom_signal.emit(localization_dto)
                time.sleep(0.5)

    def stop(self):
        self._running = False
