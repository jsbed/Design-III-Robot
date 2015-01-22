import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return flask.jsonify({"question": "22 September 1960 is the date of independence of this country."})

if __name__ == '__main__':
    app.run()