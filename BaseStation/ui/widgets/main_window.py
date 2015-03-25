import json

from PySide import QtGui
from PySide.QtCore import Qt
from PySide.QtGui import QBrush

from BaseStation.communication.tcp_server import TcpServer
from BaseStation.ui.QtProject.GeneratedFiles.mainwindow import Ui_MainWindow
from BaseStation.ui.utilities.Chronometer import Chronometer, NEW_TIME_UPDATE
from BaseStation.ui.utilities.Outputer import Outputer
from BaseStation.ui.widgets.flag_displayer import FlagDisplayer
from BaseStation.ui.widgets.items_displayer import ItemsDisplayer
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
        self._items_displayer = ItemsDisplayer(self.ui)
        self._tcp_server = TcpServer()
        self._setup_ui()
        self._setup_tcp_server()

    def _setup_ui(self):
        self.ui.clearConsole.clicked.connect(self._outputer.clearOutput)
        self.ui.startCycle.clicked.connect(self._start_cycle)
        self.ui.startChrono.clicked.connect(self._start_chrono)
        self.ui.pauseChrono.clicked.connect(self._pause_chrono)
        self.ui.restartChrono.clicked.connect(self._restart_chrono)
        self.ui.chronometerLabel.setText(self._chronometer.get_time())
        self._chronometer.attach(NEW_TIME_UPDATE, self)

    def _setup_tcp_server(self):
        self._tcp_server.signal.customSignal.connect(self._handle_tcp_signal)
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
        if ("question" in signal_data):
            self.ui.questionLabel.setText(signal_data["question"])
        if ("country" in signal_data):
            self.ui.countryLabel.setText(signal_data["country"])
            self._flag_displayer.display_country(signal_data["country"])

    def _start_cycle(self):
        self._outputer.output("Start Cycle")

    def _start_chrono(self):
        self._chronometer.start()

    def _pause_chrono(self):
        self._chronometer.pause()

    def _restart_chrono(self):
        self._chronometer.restart()

    def _update_chronometer_label(self):
        self.ui.chronometerLabel.setText(self._chronometer.get_time())

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        pen = self._items_displayer.set_pen()
        brush = QBrush()

        painter.begin(self)
        painter.setPen(pen)
        painter.setBrush(brush)

        path = self._items_displayer.draw_path()
        robot_position, robot_image = self._items_displayer.draw_robot()
        cube_position, cube_image = self._items_displayer.draw_cube()

        painter.drawImage(robot_position, robot_image)
        painter.drawImage(cube_position, cube_image)
        painter.drawPath(path)

        painter.end()
        self.update()
