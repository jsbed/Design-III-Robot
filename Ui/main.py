import os
import sys

from PySide import QtGui

from Robot.filler import country_repository_filler
from Ui.main_window import Main


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
    init_ui()
