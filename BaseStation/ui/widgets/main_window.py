import json

from PySide import QtGui
from PySide.QtCore import Qt

from BaseStation.communication.tcp_server import TcpServer
from BaseStation.ui.QtProject.GeneratedFiles.mainwindow import Ui_MainWindow
from BaseStation.ui.utilities.Chronometer import Chronometer, NEW_TIME_UPDATE
from BaseStation.ui.utilities.Outputer import Outputer
from BaseStation.ui.widgets.drawing_label import DrawingLabel
from BaseStation.ui.widgets.flag_displayer import FlagDisplayer
from BaseStation.ui.widgets.items_displayer import ItemsDisplayer
from BaseStation.workers.robot_locator_worker import RobotLocatorWorker
from Robot.communication.localization.localization_dto import create_localization_from_localization_dto
from Robot.communication.localization.localization_request import ROBOT_LOCALIZATION_REQUEST
from Robot.utilities.observer import Observer


class Main(QtGui.QMainWindow, Observer):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowState.WindowFullScreen)

        self._outputer = Outputer(self.ui.consoleBrowser)
        self._chronometer = Chronometer()
        self._flag_displayer = FlagDisplayer(self.ui)
        self._robot_locator_worker = RobotLocatorWorker()
        self._items_displayer = ItemsDisplayer(self.ui.table_label.geometry())
        self._drawing_label = DrawingLabel(self._items_displayer, self)
        self._tcp_server = TcpServer()
        self._setup_ui()
        self._setup_tcp_servers()

    def _setup_ui(self):
        self.ui.clearConsole.clicked.connect(self._outputer.clearOutput)
        self.ui.startCycle.clicked.connect(self._start_cycle)
        self.ui.startChrono.clicked.connect(self._start_chrono)
        self.ui.pauseChrono.clicked.connect(self._pause_chrono)
        self.ui.restartChrono.clicked.connect(self._restart_chrono)
        self.ui.question_ok_button.clicked.connect(self._question_is_ok)
        self.ui.new_question_button.clicked.connect(self._ask_new_question)
        self.ui.restart_cycle.clicked.connect(self._restart_cycle)
        self.ui.chronometerLabel.setText(self._chronometer.get_time())
        self._robot_locator_worker.signal.custom_signal.connect(
            self._new_robot_localization)
        self._chronometer.attach(NEW_TIME_UPDATE, self)

        self._set_question_buttons_enabled(False)
        self._robot_locator_worker.start()

    # When closing Window
    def closeEvent(self, event):
        self._robot_locator_worker.stop()

    def _setup_tcp_servers(self):
        self._tcp_server.signal.custom_signal.connect(
            self._handle_tcp_signal)
        self._tcp_server.start()

    def observer_update(self, event, value):
        if (event == NEW_TIME_UPDATE):
            self._update_chronometer_label()

    def _handle_tcp_signal(self, event):
        signal_data = json.loads(event)

        if ("message" in signal_data):
            self._outputer.output(signal_data["message"])
        if ("path" in signal_data):
            self._items_displayer.display_path(signal_data["path"])
        if ("cubePosition" in signal_data):
            self._items_displayer.display_cube(signal_data["cubePosition"])
        if ("question" in signal_data and "country" in signal_data):
            self.ui.questionLabel.setText(signal_data["question"])
            self._flag_displayer.display_country(signal_data["country"])
            self._set_question_buttons_enabled(True)
        if ("request" in signal_data):
            if signal_data["request"] == ROBOT_LOCALIZATION_REQUEST:
                localization = self._robot_locator_worker.get_localization()
                self._tcp_server.send_localization_response(localization)

    def _start_cycle(self):
        self._tcp_server.send_start_cycle_signal()
        self._chronometer.start()
        self.ui.startCycle.setEnabled(False)

    def _new_robot_localization(self, localization_dto):
        localization = create_localization_from_localization_dto(
            localization_dto)

        self._items_displayer.display_robot(localization.position,
                                            localization.orientation)

    def _start_chrono(self):
        self._chronometer.start()

    def _pause_chrono(self):
        self._chronometer.pause()

    def _restart_chrono(self):
        self._chronometer.restart()

    def _restart_cycle(self):
        self._chronometer.restart()
        self._set_question_buttons_enabled(False)
        self.ui.startCycle.setEnabled(True)
        self._clear_question_and_country()

    def _question_is_ok(self):
        self._tcp_server.send_question_ok_signal()
        self._set_question_buttons_enabled(False)

    def _ask_new_question(self):
        self._tcp_server.send_new_question_signal()
        self._set_question_buttons_enabled(False)
        self._clear_question_and_country()

    def _update_chronometer_label(self):
        self.ui.chronometerLabel.setText(self._chronometer.get_time())

    def _clear_question_and_country(self):
        self.ui.questionLabel.setText("-")
        self.ui.countryLabel.setText("-")
        self._flag_displayer.remove_country()

    def _set_question_buttons_enabled(self, state):
        self.ui.question_ok_button.setEnabled(state)
        self.ui.new_question_button.setEnabled(state)
