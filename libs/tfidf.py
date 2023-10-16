import chardet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import time


class tfIDF:
    """
    Classe permettant de calculer la similarité cosinus entre une requête et les sous-titres
    """

    def __init__(self, data, series_names, type_series):
        st = time.time()
        self.VECTORIZER = TfidfVectorizer()
        with open(series_names, 'r', encoding='utf-8') as f:
            self.SERIES_NAMES = json.load(f)
        with open(data, 'r') as f:
            try:
                self.TF_IDF_MATRIX = self.VECTORIZER.fit_transform(json.load(f))
            except Exception as e:
                print(e)
        self.type = type_series
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

    def save_data(self, file_name):
        """
        Sauvegarde les données
        :param file_name: nom du fichier
        """
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.TF_IDF_MATRIX, f)
            f.close()

    def compute_cosine_similarity(self, query: str):
        """
        Calcule la similarité cosinus entre la requête et les sous-titres
        :param query: requête de l'utilisateur
        :return: liste des similarités cosinus
        """
        query_vector = self.VECTORIZER.transform([query])
        result = cosine_similarity(query_vector, self.TF_IDF_MATRIX)
        return result

    def get_series_similaires(self, query: str):
        """
        Retourne les séries similaires à la requête
        :param query: requête de l'utilisateur
        """
        try:
            similarities = self.compute_cosine_similarity(query)
            series_indices = similarities.argsort()[0][::-1]
        except Exception as e:
            print(e)
            return []
        return [self.SERIES_NAMES[idx] for idx in series_indices[:3]]

    def getShapes(self):
        return self.TF_IDF_MATRIX.shape


if __name__ == '__main__':
    # Création d'un objet tf_idf
    tiIDF_VF = tfIDF('../data/data_VF.json', '../data/seriesInfos.json', 'VF')
    # tiIDF_VO = tfIDF('../data/data_VO.json', '../data/seriesInfos.json', 'VO')

    print("shape de la matrice VF: ", tiIDF_VF.getShapes())
    # print("shape de la matrice VO: ", tiIDF_VO.getShapes())

    # Requête de l'utilisateur
    queryUser = input('Requête: ')

    # Récupération des séries similaires
    series_similaires = tiIDF_VF.get_series_similaires(queryUser)

    # Affichage des séries similaires
    for i in range(5):
        print(series_similaires[i])
