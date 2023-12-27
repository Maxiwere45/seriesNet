# SerieNet API

## Sommaire

- [Description](#description)
- [Installation](#installation)
  - [Prérequis](#prérequis)
  - [Installation (Linux)](#installation-linux)
  - [Utilisation](#utilisation)
- [Auteurs](#auteurs)
- [Crédits](#crédits)

## Description

SerieNet API est un serveur FLASK permettant de réaliser des recherches de séries TV des années 90 via
leurs sous-titres. Il utilise l'algorithme de recherche de similarité de textes TF-IDF.

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip
- virtualenv
- git

### Installation (Linux)

1. Cloner le projet
> `git clone [url du projet]`

2. Créer un environnement virtuel dans le dossier du projet
> `python3 -m venv .venv`

3. Activer l'environnement virtuel
> `source .venv/bin/activate`

4. Installer les dépendances avec la commande 
> `pip install -r data/requirements.txt`

5. Télécharger les données nécessaires au fonctionnement de l'API depuis le lien suivant : `en cours de création`

6. Décompresser l'archive dans le dossier `data`


## Utilisation

* Exécuter la commande suivante pour lancer le serveur :

> `gunicorn --bind`

## Auteurs

* **Anrifou Amdjad** _alias_ [@Maxiwere45](https://github.com/Maxiwere45)
* **PREMI CARL** _alias_ [@otsubyo](https://github.com/otsubyo)

* Professeurs encadrants :
  * **M. BROISIN JULIEN** _alias_ [@bretonJulien](https://www.linkedin.com/in/jln-brtn/)
  * **M. BRETON JULIEN** _alias_ [@broisinJulien](https://www.linkedin.com/in/jbroisin/)

## Crédits

Ce projet a été réalisé dans le cadre d'un projet scolaire à l'[IUT PAUL SABATIER de Toulouse](https://iut.univ-tlse3.fr/) pour l'année 2023-2024 dans le
parcour [Administration, gestion et exploitation des bases de données](https://iut.univ-tlse3.fr/but-informatique-parcours-administration-gestion-et-exploitation-des-donnees-toulouse) (AGED).