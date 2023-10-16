from flask import Flask, jsonify, Response
from libs.tfidf import tfIDF
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


procVF = tfIDF('./data/data_VF.json', './data/seriesInfos.json', 'VF')
procVO = tfIDF('./data/data_VO.json', './data/seriesInfos.json', 'VO')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<string:lang>/<string:id>', methods=['GET'])
def search(id: str, lang="VF") -> Response:
    if lang == "VO":
        series_similaires = procVO.get_series_similaires(id)
    else:
        series_similaires = procVF.get_series_similaires(id)
    return jsonify(series_similaires)


if __name__ == '__main__':
    app.run()
