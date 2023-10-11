import os
import chardet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import json
import time
import numpy as np


class tfIDF:
    VECTORIZER = TfidfVectorizer()
    TF_IDF_MATRIX = None
    SERIES_NAMES = None

    def __init__(self, data, series_names, type):
        st = time.time()
        with open(series_names, 'r') as f:
            self.SERIES_NAMES = list(json.load(f))
            f.close()

        with open(data, 'r') as f:
            try:
                self.TF_IDF_MATRIX = self.VECTORIZER.fit_transform(json.load(f))
                f.close()
            except Exception as e:
                f.close()
                print(e)
        self.type = type
        end = time.time()
        print('Temps de chargement des données: ', end - st)

    @staticmethod
    def detect_encoding(file_path) -> str:
        """
        Renvoie l'encodage du fichier passé en paramètre
        :param file_path: chemin du fichier
        :return: encodage du fichier
        """
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        return str(result['encoding'])

    # Réinitialiser les données en cas de modifications
    def reinitialize(self, folder_path, save=False):
        DATA = []
        SERIES_NAMES = []
        for nom_fichier in os.listdir(folder_path):
            if nom_fichier.endswith('.txt'):
                chemin_fichier = os.path.join(folder_path, nom_fichier)

                with open(chemin_fichier, 'r', encoding=self.detect_encoding(chemin_fichier)) as fichier:
                    sous_titres_serie = fichier.read()
                    DATA.append(sous_titres_serie)
                    SERIES_NAMES.append(nom_fichier.replace('.txt', ''))
                    fichier.close()
        self.VECTORIZER.fit_transform(DATA)
        self.SERIES_NAMES = SERIES_NAMES

        if save:
            self.save_data('data.json')
            self.save_data('series_names.json')

    @staticmethod
    def save_data(file_name):
        """
        Sauvegarde les données
        :param data: données à sauvegarder
        :param series_names: nom des séries
        :param type: type de données
        """
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(tfIDF.TF_IDF_MATRIX, f)
            f.close()

    def compute_cosine_similarity(self, query: str) -> np.ndarray:
        """
        Calcule la similarité cosinus entre la requête et les sous-titres
        :param query: requête de l'utilisateur
        :return: liste des similarités cosinus
        """
        try:
            query_vector = self.VECTORIZER.transform([query])
            return cosine_similarity(query_vector, self.TF_IDF_MATRIX)
        except Exception as e:
            print(e)

    def get_series_similaires(self, query: str):
        """
        Retourne les série similaires à la requête
        """
        similarities = self.compute_cosine_similarity(query)
        series_indices = similarities.argsort()[0][::-1]
        series = []

        for idx in series_indices:
            series.append(self.SERIES_NAMES[idx])

        return series


if __name__ == '__main__':
    # Création d'un objet tf_idf
    tiIDF = tfIDF('../data/data.json', '../data/series_names.json', 'VF')

    # Requête de l'utilisateur
    query = input('Requête: ')

    # Récupération des séries similaires
    series_similaires = tiIDF.get_series_similaires(query)

    # Affichage des séries similaires
    for i in range(5):
        print(series_similaires[i])
