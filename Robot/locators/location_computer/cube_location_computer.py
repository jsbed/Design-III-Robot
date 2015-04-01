from statistics import mean

from Robot.configuration.config import Config


def compute(corners):
    try:
        print(_find_position_and_size(corners))
    except:  # NO CORNERS
        pass


def _find_position_and_size(corners):
    all_x = [coord[0] for coord in corners]

    mean_x = mean(all_x)
    size = max(all_x) - min(all_x)

    return Config().get_camera_width() / 2 - mean_x, size
