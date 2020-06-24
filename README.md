## Projet

Scrapping du site 'sens-critique.com' afin d'en extraire des données sur les films et d'entraîner une machine pour qu'elle prédise leurs notations

## Auteurs

Alexandre Das Neves
Julie Montagne
Emma Dollé Leczycki

## Pré-requis / Fabriqué avec

- Python
- Anaconda Jupyter

## Compilation

Code entier dans un fichier jupyter 'Projet final' pour qu'il soit exécuté étape par étape. Le code 'ProjetFinal.py' ne contient que les fonctions afin d'y appliquer les unit tests.

## Fonctionnalités

- Retourne le code html d'une page d'après une URL donnée
- Retourne les liens contenant le mot 'film' et les ajoute à une liste 'movie_links'
- Extrait des informations sur les films de chaque URL donnée
- Ajoute ces informations à une liste 'films'
- Crée des dataframe à partir de la liste 'films'
- Enregistre une dataframe dans un document Excel
- Compte les occurences de mots dans les dataframes avec CountVectorizer, Tf-idf, et get_dummies
- Machine learning: entraîne une machine avec des sets d'entraînement et teste le score sur des sets de test
- Unit tests testent les fonctions 'extract_movie_info' et 'get_links_to_movies'

## Running unit tests

Run `pytest test_extract_movie_info` to execute the unit test about the function 'extract_movie_info'
Run `pytest test_get_links_to_movies` to execute the unit test about the function 'get_links_to_movies'