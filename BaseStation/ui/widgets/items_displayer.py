from PySide import QtCore
from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QPen, QPainterPath, QImage

from Robot.configuration.config import Config


class ItemsDisplayer():

    def __init__(self, widget):
        self._widget = widget
        self._robot_position = QtCore.QPoint(0, 0)
        self._half_way = QtCore.QPoint(0, 0)
        self._destination = QtCore.QPoint(0, 0)
        self._cube_position = QtCore.QPoint(0, 0)
        self._robot_image = QImage()
        self._cube_image = QImage()
        self._config = Config()
        self._table_area = QtCore.QRect(self._widget.table_label.geometry())

    def display_robot(self, position):
        x, y = position
        self._robot_position = QtCore.QPoint(self._table_area.left() + x
                                             * self._table_area.width()
                                             / self._config.get_table_width(),
                                             self._table_area.top() +
                                             self._table_area.height()
                                             - y
                                             * self._table_area.height()
                                             / self._config.get_table_height())
        self._robot_image = QImage(":/resources/robot.png")

    def display_path(self, destination):
        self._destination = QtCore.QPoint(self._table_area.left() +
                                          destination[0]
                                          * self._table_area.width()
                                          / self._config.get_table_width(),
                                          self._table_area.top() +
                                          self._table_area.height()
                                          - destination[1]
                                          * self._table_area.height()
                                          / self._config.get_table_height())

    def display_cube(self, cube_position):
        self._cube_position = QtCore.QPoint(self._table_area.left() +
                                            cube_position[0]
                                            * self._table_area.width()
                                            / self._config.get_table_width(),
                                            self._table_area.top() +
                                            self._table_area.height()
                                            - cube_position[1]
                                            * self._table_area.height()
                                            / self._config.get_table_height())
        self._cube_image = QImage(":/resources/cube.png")

    def set_pen(self):
        pen = QPen()
        pen.setStyle(Qt.DotLine)
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setWidth(3)
        pen.setColor(Qt.red)
        return pen

    def draw_path(self):
        path = QPainterPath()
        if not (self._destination == QtCore.QPoint(0, 0)):
            path.moveTo(self._robot_position.x(), self._robot_position.y())
            path.lineTo(self._destination.x(), self._destination.y())
        return path

    def draw_robot(self):
        position = QPoint(0, 0)
        if not(self._robot_image.isNull()):
            position = QPoint(self._robot_position.x() -
                              (self._robot_image.width() / 2),
                              self._robot_position.y() -
                              (self._robot_image.height() / 2))
        return position, self._robot_image

    def draw_cube(self):
        position = QPoint(0, 0)
        if not(self._cube_image.isNull()):
            position = QPoint(self._cube_position.x() -
                              (self._cube_image.width() / 2),
                              self._cube_position.y() -
                              (self._cube_image.height() / 2))
        return position, self._cube_image
