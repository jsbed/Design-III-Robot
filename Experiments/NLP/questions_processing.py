import nltk
import requests

#server_address = "http://localhost:5000/"
server_address = "https://132.203.14.228/"
r = requests.get(server_address, verify=False)
sentence = r.json()["question"]
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)
print(sentence, tokens, tagged, entities, sep="\n")