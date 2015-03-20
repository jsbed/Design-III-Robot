import requests

from Robot.configuration import config


def get_question():
    response = requests.get(config.Config().get_atlas_url(), verify=False)
    return response.json()["question"]
