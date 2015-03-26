import json

from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


def create_localization_dto(localization):
    response = {"unknown": True, "orientation": 0, "position": (0, 0)}

    if not localization.unknown:
        response["unknown"] = False
        response["orientation"] = localization.orientation
        response["position"] = localization.position

    return json.dumps(response, "utf-8")


def create_localization_from_localization_dto(response):
    response = json.loads(response)

    if response["unknown"]:
        return Localization(None, None, unknown=True)
    else:
        return Localization(Point._make(response["position"]),
                            response["orientation"])
