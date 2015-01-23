
import sys
from PySide import QtGui
from MainWindow_Ui import Ui_MainWindow
from PySide.QtCore import Qt

class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowState.WindowFullScreen)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())
