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
        self._cube_positions = []
        self._cube_images = []
        self._robot_image = QImage(":/resources/robot.png")
        self._config = Config()
        self._robot_displayed = False

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
            self._robot_displayed = True

    def display_path(self, destination):
        self._destination = []

        for point in destination:
            (virtual_x, virtual_y) = self._convert_real_to_virtual(
                point[0], point[1])
            self._destination.append(QtCore.QPoint(virtual_x, virtual_y))

    def display_cubes(self, cubes):
        self.remove_cubes()

        for cube in cubes:
            self._display_cube_color(cube["cube color"])
            self._display_cube_position(cube["cube position"])

    def _display_cube_position(self, cube_position):
        (virtual_x, virtual_y) = self._convert_real_to_virtual(
            cube_position[0], cube_position[1])

        cube_position = QtCore.QPoint(virtual_x, virtual_y)
        self._cube_positions.append(cube_position)

    def _display_cube_color(self, color):
        cube_image = QImage(":/resources/cube.png")

        if (color == 1):
            cube_image = QImage(":/resources/cube_red.png")
        elif (color == 2):
            cube_image = QImage(":/resources/cube_green.png")
        elif (color == 3):
            cube_image = QImage(":/resources/cube_blue.png")
        elif (color == 4):
            cube_image = QImage(":/resources/cube_yellow.png")
        elif (color == 5):
            cube_image = QImage(":/resources/cube_white.png")
        elif (color == 6):
            cube_image = QImage(":/resources/cube_black.png")

        self._cube_images.append(cube_image)

    def set_pen(self):
        pen = QPen()
        pen.setStyle(Qt.DotLine)
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setWidth(3)
        pen.setColor(Qt.red)
        return pen

    def draw_path(self):
        path = QPainterPath()

        if self._destination:
            path.moveTo(self._robot_position.x(), self._robot_position.y())

            for point in self._destination:
                path.lineTo(point.x(), point.y())

        return path

    def draw_robot(self):
        position = QPoint(0, 0)
        if not(self._robot_image.isNull()):
            position = QPoint(self._robot_position.x() -
                              (self._robot_image.width() / 2),
                              self._robot_position.y() -
                              (self._robot_image.height() / 2))
        return position, -self._robot_orientation, self._robot_image

    def draw_cube(self, cube_it):
        position = QPoint(0, 0)
        if not(self._cube_images[cube_it].isNull()):
            position = QPoint(self._cube_positions[cube_it].x() -
                              (self._cube_images[cube_it].width() / 2),
                              self._cube_positions[cube_it].y() -
                              (self._cube_images[cube_it].height() / 2))
        return position, self._cube_images[cube_it]

    def get_number_of_cube(self):
        return len(self._cube_positions)

    def hide_robot(self):
        self._robot_displayed = False

    def remove_path(self):
        self._destination = []

    def remove_cubes(self):
        self._cube_images.clear()
        self._cube_positions.clear()

    def robot_is_visible(self):
        return self._robot_displayed

    def _convert_real_to_virtual(self, real_x, real_y):
        virtual_x = self._table_area.width() - real_x * self._table_area.width() / \
            self._config.get_table_width()

        virtual_y = self._table_area.height() - real_y * self._table_area.height() / \
            self._config.get_table_height()

        return (virtual_x, virtual_y)
