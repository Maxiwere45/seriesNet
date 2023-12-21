from flask import Flask, jsonify, abort, request
from libs.tfidf import tfIDF
from flask import render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
print("\nDémarrage du serveur SERIE.NET API...")
print("Chargement des données, veuillez patienter...")
procVF = tfIDF('./data/data_vf.json', './data/seriesInfos.json', 'VF')
procVO = tfIDF('./data/data_vo.json', './data/seriesInfos.json', 'VO')
print("Tout est bon :)")
print("Le serveur fonctionne normalement (CRTL + C pour quitter)")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    # Récupérer les paramètres de la requête
    id = request.args.get('id', '')
    lang = request.args.get('lang', '')

    # Vérifier si les paramètres nécessaires sont présents
    if not id:
        abort(400, "Le paramètre 'id' est requis.")

    # Appeler la fonction de recherche appropriée en fonction de la langue
    if lang == "VO":
        series_similaires = procVO.get_series_similaires(id)
    else:
        series_similaires = procVF.get_series_similaires(id)
    return jsonify(series_similaires)


if __name__ == '__main__':
    app.run()
