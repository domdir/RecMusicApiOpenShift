print "init"
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

path = os.getcwd() + "/app-root/repo/csv/movie_info_reduced_with_genre.csv"
movie_table_all = pd.read_csv(path, ",", dtype=object)
movie_table_all = movie_table_all.drop("Unnamed: 0", 1)

col_to_keep = ["IMDB_ID", "TITLE", "GENRES", "YEAR",
               "LENGTH", "POSTER", "YOU_TUBE_ID", "IMDB_RATING", "IMDB_VOTES",
               "f1", "f2", "f4", "f6"]

movie_table_all_ordered=movie_table_all[col_to_keep].sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()

empty_df=movie_table_all[movie_table_all["IMDB_ID"]=="kkkkkkkkk"][col_to_keep]

# path = os.getcwd()+ "/app-root/repo/csv/movie_info_reduced.csv"
# movie_table_sorted_by_pop = movie_table.sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()



import routes
import database_manager


"""
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
"""
