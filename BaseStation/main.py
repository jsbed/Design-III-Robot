import os
import sys

from PySide import QtGui

from BaseStation.ui.widgets.main_window import Main
from Robot.configuration.config import Config
from Robot.filler import country_repository_filler


def fill_country_repository():
    flags_file_path = os.path.join("..", "Robot", "resources", "flags.csv")
    country_repository_filler.fill_repository_from_file(flags_file_path)


def init_ui():
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    fill_country_repository()
    Config(os.path.join("..", "Robot", "config.ini")).load_config()
    init_ui()
