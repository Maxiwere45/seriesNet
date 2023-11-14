import requests

if __name__ == '__main__':
    # URL de l'application Flask
    base_url = "http://127.0.0.1:5000"  # Mettez l'URL correcte de votre application Flask

    # Exemple de test pour la route '/'
    response = requests.get(base_url)
    if response.status_code == 200:
        print("Test pour la route '/' réussi!")
    else:
        print("Test pour la route '/' a échoué!")

    lang = input("Entrez la langue de la série (VF ou VO) : ")
    if lang != "VF" and lang != "VO":
        lang = "VF"
        print("Langue par défaut : VF")

    while True:
        # Exemple de test pour la route '/search/id/lang'
        id = input("> Entrez un (ou des) mot clé : ")

        if id == "cmd change lang":
            lang = input("> Entrez la langue de la série (VF ou VO) : ")
            id = input("> Entrez un (ou des) mot clé : ")
        if id == "exit now":
            break

        search_url = f"{base_url}/search/{id}/{lang}"
        response = requests.get(search_url)

        if response.status_code == 200:
            series_similaires = response.json()
            print(f"Test pour la route '/search/{id}/{lang}' réussi!")
            print("Résultats :")
            for serie in series_similaires:
                print(f"  - {serie}")
        else:
            print(f"Test pour la route '/search/{id}/{lang}' a échoué!")

        # Assurez-vous que votre application Flask est en cours d'exécution avant d'exécuter ces tests.
        # Utilisez la bonne URL de l'application Flask (base_url) selon votre configuration.
