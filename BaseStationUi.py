from PySide import QtGui
import sys

from BaseStation.ui.widgets.main_window import Main
from Robot.configuration.config import Config
from Robot.filler import country_repository_filler
from Robot.resources.kinect import Kinect


def init_ui():
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    country_repository_filler.fill_repository()
    Config().load_config()
    Kinect().start()
    init_ui()
