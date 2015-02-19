
SIZE = 8


class Cube:
    def __init__(self, color, target_zone_position, is_in_target_zone,
                 localization):
        self._size = SIZE
        self._color = color  # Color
        self._target_zone_position = target_zone_position  # Point
        self._is_in_target_zone = is_in_target_zone  # bool
        self._localization = localization  # Localization

    def set_localization_position(self, value):
        self._localization.position = value

    def get_target_zone_position(self):
        return self._target_zone_position

    def get_localization(self):
        return self._localization
