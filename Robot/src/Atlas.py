import requests


server_address = "https://132.203.14.228/"  # TODO: Create config file for URL


def get_question():
    return requests.get(server_address, verify=False).json()["question"]
