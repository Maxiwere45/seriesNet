from flask import Flask, render_template, jsonify
from libs.tfidf import tfIDF
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

app = Flask(__name__)

procVF = tfIDF('./data/data_VF.json', './data/series_names_VF.json', 'VF')
procVO = tfIDF('./data/data_VO.json', './data/series_names_VO.json', 'VO')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/VF/<string:id>', methods=['GET'])
def search(id):
    return jsonify(procVF.get_series_similaires(str(id)))


if __name__ == '__main__':
    app.run()
