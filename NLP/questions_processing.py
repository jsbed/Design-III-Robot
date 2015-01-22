import nltk
import requests

#server_address = "http://localhost:5000/"
server_address = "https://132.203.14.228/"
r = requests.get(server_address, verify=False)
print(r.json())