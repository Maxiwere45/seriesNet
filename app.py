from flask import Flask
from libs import tfidf

app = Flask(__name__)
proc = tfidf.tfIDF('./data/data.json', './data/series_names.json', 'json')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
