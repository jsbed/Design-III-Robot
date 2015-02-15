import sys

from PySide import QtGui
from PySide.QtCore import Qt

from Robot.utilities.observer import Observer
from Ui.Chronometer import Chronometer, NEW_TIME_UPDATE
from Ui.Outputer import Outputer
from Ui.QtProject.GeneratedFiles.mainwindow import Ui_MainWindow


class Main(QtGui.QMainWindow, Observer):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowState(Qt.WindowState.WindowFullScreen)

        self._outputer = Outputer(self.ui.consoleBrowser)
        self._chronometer = Chronometer()
        self._setup_ui()

    def _setup_ui(self):
        self.ui.clearConsole.clicked.connect(self._outputer.clearOutput)
        self.ui.startCycle.clicked.connect(self._start_cycle)
        self.ui.startChrono.clicked.connect(self._start_chrono)
        self.ui.pauseChrono.clicked.connect(self._pause_chrono)
        self.ui.restartChrono.clicked.connect(self._restart_chrono)
        self.ui.chronometerLabel.setText(self._chronometer.get_time())
        self._chronometer.attach(NEW_TIME_UPDATE, self)

    def update(self, event, value):
        if (event == NEW_TIME_UPDATE):
            self._update_chronometer_label()

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

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())
