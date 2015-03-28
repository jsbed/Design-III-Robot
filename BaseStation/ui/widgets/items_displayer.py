from PySide import QtCore
from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QPen, QPainterPath, QImage

from Robot.configuration.config import Config


class ItemsDisplayer():

    def __init__(self, table_geometry):
        self._table_area = table_geometry
        self._robot_position = QtCore.QPoint(0, 0)
        self._robot_orientation = 0
        self._destination = QtCore.QPoint(0, 0)
        self._cube_position = QtCore.QPoint(0, 0)
        self._robot_image = QImage(":/resources/robot.png")
        self._cube_image = QImage()
        self._config = Config()

    def display_robot(self, position, orientation):
        real_x, real_y = position
        virtual_x, virtual_y = self._convert_real_to_virtual(real_x, real_y)

        new_position = None

        try:
            new_position = QtCore.QPoint(virtual_x, virtual_y)
        except OverflowError as e:
            print(str(e))
        else:
            self._robot_position = new_position
            self._robot_orientation = orientation

    def display_path(self, destination):
        virtual_x, virtual_y = self._convert_real_to_virtual(destination[0],
                                                             destination[1])
        self._destination = QtCore.QPoint(virtual_x, virtual_y)

    def display_cube(self, cube_position):
        virtual_x, virtual_y = self._convert_real_to_virtual(cube_position[0],
                                                             cube_position[1])

        self._destination = QtCore.QPoint(virtual_x, virtual_y)
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
        return position, -self._robot_orientation, self._robot_image

    def draw_cube(self):
        position = QPoint(0, 0)
        if not(self._cube_image.isNull()):
            position = QPoint(self._cube_position.x() -
                              (self._cube_image.width() / 2),
                              self._cube_position.y() -
                              (self._cube_image.height() / 2))
        return position, self._cube_image

    def _convert_real_to_virtual(self, real_x, real_y):
        virtual_x = self._table_area.width() - real_x * self._table_area.width() / \
            self._config.get_table_width()

        virtual_y = self._table_area.height() - real_y * self._table_area.height() / \
            self._config.get_table_height()

        return virtual_x, virtual_y
