from flask import Flask
import flask
import random
app = Flask(__name__)

questions = ["22 September 1960 is the date of independence of this country.",
             "My death rate is greater than 13 death/1000 and my capital starts with Mos.",
             "What country has a total area of 390757 sq km?",
             "My independence was declared in August 1971.",
             "22 September 1960 is the date of independence of this country.",
             "My public debt is 7.9% of GDP.",
             "What country has an inflation rate between 0.3% and 0.5%?",
             "The lotus blossom is the national symbol of this country.",
             "What country has a population greater than 1 300 692 576?",
             "What country has declared its independence on 22 May 1990?",
             "My internet country code is .br.",
             "In 1923, we proclaimed our independence.",
             "My latitude is 16 00 S and my longitude is 167 00 E.",
             "My birth rate is approximately 16 births/1000 and my local short country name contains 2 words.",
             "My languages include german, french and romansch.",
             "My unemployment rate is 40.6%.",
             "My export partners are US, Germany, UK, France, Spain, Canada and Italy.",
             "The music of my national anthem was composed by Routhier, Weir and Lavallee.",
             "What country has 13.694 million internet users?",
             "What country has major urban areas of 5.068 million and 1.098 million?",
             "My electricity production is between 600 and 650 billion kWh.",
             "What country has a population growth rate of 1.46%?",
             "What country has Yaounde as its capital?",
             "My capital name starts with Ath and ends with ens.",
             "What country has religions including 51.3% of protestant and 0.7% of buddhist?",
             "What country has industries including the world's largest producer of platinum, gold and chromium?",
             "What country has illicit drugs activities including a transshipment point for cocaine from South America to North America and illicit cultivation of cannabis?",
             "The title of my national anthem is Advance Australia Fair.",
             "What country has religions including hindu, muslim, Christian, and sikh?",
             "My unemployment rate is greater than 25% and my industries include tourism and footwear.",
             "One national symbol of this country is the edelweiss.",
             "What country considers illicit drug trafficking as a serious offense and carry death penalty?",
             "What country has a latitude of 41.00 S?",
             "The major urban areas of this country are Santiago, Valparaiso and Concepcion.",
             "What country has a birth rate of 46.12 births/ 1000 population?",
             "What country has .dz as its internet country code?",
             "My national symbol is the elephant.",
             "My population is 32 742. ",
             "The death rate of this country is greater than 10.37 deaths/1000 population and less than 10.40 deaths/1000 population.",
             "What country has a tropical climate and has a capital that starts with the letters Phn?",
             "My capital name starts with Moga.",
             "My population growth rate is between 1.44% and 1.47%.",
             "My telephone lines in use are 1.217 million.",
             "My import partners include Netherlands, France, China, Belgium, Switzerland and Austria."]


@app.route('/')
def hello_world():
    return flask.jsonify({"question": random.choice(questions)})

if __name__ == '__main__':
    app.run(host="192.168.0.34", port=4000)
