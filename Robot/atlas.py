import requests

from Robot.configuration.Config import Config


def get_question():
    response = requests.get(Config().get_atlas_url(), verify=False)
    return response.json()["question"]
