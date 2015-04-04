import json

from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


def create_localization_dto(localization):
    dto = {"unknown": True, "orientation": 0, "position": (0, 0)}

    if not localization.unknown:
        dto["unknown"] = False
        dto["orientation"] = localization.orientation
        dto["position"] = localization.position

    return json.dumps(dto, "utf-8")


def create_localization_from_localization_dto(dto):
    dto = json.loads(dto)

    if dto["unknown"]:
        return Localization(None, None, unknown=True)
    else:
        return Localization(Point._make(dto["position"]),
                            dto["orientation"])
