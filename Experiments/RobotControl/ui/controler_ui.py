import sys

from PySide import QtGui
from Experiments.RobotControl.ui.QtProject.GeneratedFiles.mainwindow import Ui_MainWindow
from Robot.communication.tcp_client import TCPClient


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._tcp_client = TCPClient(self.ui.ip_line_edit.text(),
                                     int(self.ui.port_line_edit.text()))
        self.setFixedSize(self.size())
        self._setup_ui()

    def _setup_ui(self):
        self.ui.up_button.clicked.connect(self._up_arrow)
        self.ui.down_button.clicked.connect(self._down_arrow)
        self.ui.left_button.clicked.connect(self._left_arrow)
        self.ui.right_button.clicked.connect(self._right_arrow)
        self.ui.rotate_right_button.clicked.connect(self._rotate_right_arrow)
        self.ui.rotate_left_button.clicked.connect(self._rotate_left_arrow)
        self.ui.connect_button.clicked.connect(self._connect_button)
        self.ui.ip_line_edit.textEdited.connect(self._ip_changed)
        self.ui.port_line_edit.textEdited.connect(self._port_changed)

    def _ip_changed(self):
        self._tcp_client.set_host(self.ui.ip_line_edit.text())

    def _port_changed(self):
        self._tcp_client.set_port(int(self.ui.port_line_edit.text()))

    def _up_arrow(self):
        self._tcp_client.send_data("up")

    def _down_arrow(self):
        self._tcp_client.send_data("down")

    def _left_arrow(self):
        self._tcp_client.send_data("left")

    def _right_arrow(self):
        self._tcp_client.send_data("right")

    def _rotate_right_arrow(self):
        self._tcp_client.send_data("rotate-right")

    def _rotate_left_arrow(self):
        self._tcp_client.send_data("rotate-left")

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
