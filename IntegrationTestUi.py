import sys

from PySide import QtGui

from Experiments.RobotControl.ui.QtProject.GeneratedFiles.mainwindow import Ui_MainWindow
from Experiments.RobotControl.ui.deplacement import Deplacement
from Experiments.RobotControl.ui.leds import Leds
from Experiments.RobotControl.ui.prehenseur import Prehenseur
from Robot.communication.tcp_client import TCPClient


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._tcp_client = TCPClient(self.ui.ip_line_edit.text(),
                                     int(self.ui.port_line_edit.text()))
        self._deplacement = Deplacement(self.ui, self._tcp_client)
        self._leds = Leds(self.ui, self._tcp_client)
        self._prehenseur = Prehenseur(self.ui, self._tcp_client)
        self.setFixedSize(self.size())
        self._setup_ui()

    def _setup_ui(self):
        self.ui.connect_button.clicked.connect(self._connect_button)
        self.ui.question_request_button.clicked.connect(self._question_request)
        self.ui.ip_line_edit.textEdited.connect(self._ip_changed)
        self.ui.port_line_edit.textEdited.connect(self._port_changed)

    def _ip_changed(self):
        self._tcp_client.set_host(self.ui.ip_line_edit.text())

    def _port_changed(self):
        self._tcp_client.set_port(int(self.ui.port_line_edit.text()))

    def _question_request(self):
        self._tcp_client.send_data("ask-question")

    def _connect_button(self):
        self._tcp_client.disconnect_socket()

        if (self._tcp_client.connect_socket()):
            self.ui.connection_status.setText("Connected")
        else:
            self.ui.connection_status.setText("No connection")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())
