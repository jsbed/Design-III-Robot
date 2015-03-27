from PySide import QtCore, QtGui
from PySide.QtCore import QPoint
from PySide.QtGui import QLabel, QBrush


class DrawingLabel(QLabel):

    def __init__(self, items_displayer, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self._items_displayer = items_displayer

        self.setGeometry(QtCore.QRect(120, 20, 260, 540))
        self.setText("")

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        pen = self._items_displayer.set_pen()
        brush = QBrush()

        painter.begin(self)
        painter.setPen(pen)
        painter.setBrush(brush)

        path = self._items_displayer.draw_path()
        robot_position, robot_rotation, robot_image = \
            self._items_displayer.draw_robot()
        cube_position, cube_image = self._items_displayer.draw_cube()

        painter.translate(robot_position.x() + robot_image.width() / 2,
                          robot_position.y() + robot_image.height() / 2)
        painter.rotate(robot_rotation)

        painter.drawImage(QPoint(-robot_image.width() / 2,
                                 -robot_image.height() / 2), robot_image)
        painter.resetTransform()
        painter.drawImage(cube_position, cube_image)
        painter.drawPath(path)
        painter.end()

        self.update()
