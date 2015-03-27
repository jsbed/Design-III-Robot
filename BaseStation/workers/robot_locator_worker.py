from PySide.QtCore import QThread

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication.localization.localization_dto import create_localization_dto
from Robot.locators import robot_locator


class RobotLocatorWorker(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signal = Signal()

    def run(self):
        localization = robot_locator.localize()

        if not localization.unknown:
            localization_dto = create_localization_dto(localization)
            self.signal.custom_signal.emit(localization_dto)
