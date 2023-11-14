import json

import mysql.connector

# Connexion à la base de données (ajustez les paramètres selon votre configuration)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9dfe351b",
    database="serie_net"
)
cursor = conn.cursor()

# Données à insérer dans la table 'series'
with open("../data/seriesInfos.json", "r", encoding="utf-8") as f:
    series_data = json.load(f)



# Insertion des données dans la table 'series'
for serie in series_data:
    insert_series_query = "INSERT INTO serie (id, name, etoiles, synopsis) VALUES (%s, %s, %s, %s)"
    series_values = (serie['id'], serie["name"], serie["etoiles"], serie["synopsis"])
    cursor.execute(insert_series_query, series_values)
    print(f"Insertion de la série {serie['name']} ({serie['id']})")

    # Insertion des genres associés à la série dans la table 'series_genres'
    for genre in serie["genres"]:
        select_genre_name_query = "SELECT genre_name FROM genre WHERE genre_name = %s"
        genre_values = (genre,)
        cursor.execute(select_genre_name_query, genre_values)
        result = cursor.fetchone()
        if result is None:
            insert_genre_query = "INSERT INTO genre (genre_name) VALUES (%s)"
            genre_values = (genre,)
            cursor.execute(insert_genre_query, genre_values)

        select_genre_id_query = "SELECT id FROM genre WHERE genre_name = %s"
        genre_values = (genre,)
        cursor.execute(select_genre_id_query, genre_values)
        genre_id = cursor.fetchone()[0]
        insert_series_genre_query = "INSERT INTO serie_genre (serie_id, genre_id) VALUES (%s, %s)"
        series_genre_values = (serie['id'], genre_id)
        cursor.execute(insert_series_genre_query, series_genre_values)

# Validez les changements et fermez la connexion
conn.commit()
conn.close()
