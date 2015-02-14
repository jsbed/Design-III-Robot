
SIZE = 8


class Cube:
    def __init__(self, color, target_zone_position, is_in_target_zone,
                 localization):
        self.size = SIZE
        self.color = color  # Color
        self.target_zone_position = target_zone_position  # int
        self.is_in_target_zone = is_in_target_zone  # bool
        self.localization = localization  # Localization
