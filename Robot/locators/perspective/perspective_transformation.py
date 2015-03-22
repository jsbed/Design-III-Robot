from math import radians, cos, sin
import cv2
import numpy
import os

from Robot.configuration.config import Config


def get_rotation_matrix(angle):
    return numpy.array([[cos(radians(angle)), 0, sin(radians(angle))],
                        [0, 1, 0],
                        [-sin(radians(angle)), 0, cos(radians(angle))]])


def transform(point):
    perspective_matrix = numpy.load(os.path.join(
        "Robot", "resources", Config().get_perspective_matrix_path()))

    invert_x_matrix = numpy.array([[-1, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]])

    translation_matrix = numpy.array([Config().
                                      get_perspective_translation_matrix()])

    rotation_matrix = get_rotation_matrix(Config().
                                          get_perspective_rotation_y())

    #  Apply transformation
    after_invert = numpy.dot(invert_x_matrix, point)
    after_rotation = numpy.dot(rotation_matrix, after_invert)
    after_translation = numpy.squeeze(after_rotation + translation_matrix)

    after_transform = cv2.perspectiveTransform(
        numpy.float32([[[after_translation[0], after_translation[2]]]]),
        perspective_matrix)

    return numpy.squeeze(after_transform)
