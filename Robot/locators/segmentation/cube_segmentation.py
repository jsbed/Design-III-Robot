class CubeSegmentor():

    def __init__(self):
        self._lower_hsv_values = [0, 0, 0]
        self._upper_hsv_values = [0, 0, 0]

    def set_lower_hsv_values(self, value):
        self._lower_hsv_values = value

    def set_upper_hsv_values(self, value):
        self._upper_hsv_values = value

    def extract_cube(self, img):
        raise NotImplementedError
