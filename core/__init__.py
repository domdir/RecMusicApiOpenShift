from flask import Flask
import pandas as pd
import logging

import os

LOGFILE = "recmusic.log"

logPath = os.path.join(os.environ["OPENSHIFT_LOG_DIR"], LOGFILE)
logging.basicConfig(filename=logPath, level=logging.DEBUG)
logging.debug('test new app')

mes_core = Flask(__name__)
mes_core.config['PROPAGATE_EXCEPTIONS'] = True


path = os.getcwd()+ "/app-root/repo/csv/movie_info_reduced.csv"
movie_table = pd.read_csv(path, ",")
movie_table = movie_table.drop("Unnamed: 0", 1)
movie_table_sorted_by_pop = movie_table.sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()


import routes
import database_manager




ALL_GENRES = {
    'Action': '0',
    'Adventure': '1',
    'Animation': '2',
    'Children': '3',
    'Comedy': '4',
    'Crime': '5',
    'Documentary': '6',
    'Drama': '7',
    'Fantasy': '8',
    'FilmNoir': '9',
    'Horror': '10',
    'IMAX': '11',
    'Musical': '12',
    'Mystery': '13',
    'Romance ': '14',
    'SciFi': 'SciFi',
    'Thriller': '15',
    'War': '16',
    'Western': '17',
}

MAIN_GENRES = {
    'ACTION': {"name": 'Action', "img": 'action.png'},
    'ADVENTURE': {"name": 'Adventure', "img": 'adventure.png'},
    'ANIMATION': {"name": 'Animation', "img": 'animation.png'},
    'CHILDREN': {"name": 'Children', "img": 'children.png'},
    'COMEDY': {"name": 'Comedy', "img": 'comedy.png'},
    'CRIME': {"name": 'Crime', "img": 'crime.png'},
    'DOCUMENTARY': {"name": 'Documentary', "img": 'documentary.png'},
    'DRAMA': {"name": 'Drama', "img": 'drama.png'},
    'FANTASY': {"name": 'Fantasy', "img": 'fantasy.png'},
    'HORROR': {"name": 'Horror', "img": 'horror.png'},
    'MUSICAL': {"name": 'Musical', "img": 'musical.png'},
    'ROMANCE ': {"name": 'Romance', "img": 'romance.png'},
    'SCIFI': {"name": 'SciFi', "img": 'sciFi.png'},
    'THRILLER': {"name": 'Thriller', "img": 'thriller.png'},
    'WESTERN': {"name": 'Western', "img": 'western.png'},
}
