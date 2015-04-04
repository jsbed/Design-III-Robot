from PySide.QtCore import QThread

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication.dtos.localization_dto import create_localization_dto
from Robot.locators import robot_locator
from Robot.locators.filter.robot_localization_filter import RobotLocalizationFilter,\
    ROBOT_LOCALIZATION_UPDATED
from Robot.utilities.observer import Observer


class RobotLocatorWorker(Observer, QThread):

    def __init__(self):
        QThread.__init__(self)
        self.signal = Signal()
        self._robot_localization_filter = RobotLocalizationFilter()
        self._running = False

        self._robot_localization_filter.attach(
            ROBOT_LOCALIZATION_UPDATED, self)

    def run(self):
        self._running = True

        while self._running:
            localization = robot_locator.localize()
            self._robot_localization_filter.update_localization(localization)

    def observer_update(self, event, value):
        if (event == ROBOT_LOCALIZATION_UPDATED):
            localization_dto = create_localization_dto(value)
            self.signal.custom_signal.emit(localization_dto)

    def stop(self):
        self._running = False

    def get_localization(self):
        return self._robot_localization_filter.get_localization()
