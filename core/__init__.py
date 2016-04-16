print "init"
from flask import Flask
import pandas as pd
import logging

import os

# LOGFILE = "recmusic.log"

# logPath = os.path.join(os.environ["OPENSHIFT_LOG_DIR"], LOGFILE)
# logging.basicConfig(filename=logPath, level=logging.DEBUG)
# logging.debug('test new app')

mes_core = Flask(__name__)
mes_core.config['PROPAGATE_EXCEPTIONS'] = True

path = os.getcwd() + "/app-root/repo/csv/movie_info_reduced_with_genre.csv"
movie_table_all = pd.read_csv(path, ",")  # dtype=object)

movie_table_all.drop("Unnamed: 0", 1, inplace=True)

col_to_keep = ["IMDB_ID", "TITLE", "GENRES", "YEAR",
               "LENGTH", "POSTER", "YOU_TUBE_ID", "IMDB_RATING", "IMDB_VOTES",
               "f1", "f2", "f4", "f6"]


col_to_drop = [

    'Action',
    'Adventure',
    'Animation',
    'Children',
    'Comedy',
    'Crime',
    'Documentary',
    'Drama',
    'Fantasy',
    'Horror',
    'Musical',
    'Romance',
    'SciFi',
    'Thriller',
    'Western',
]
movie_table_all_ordered = movie_table_all[col_to_keep].sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()

empty_df = movie_table_all[movie_table_all["IMDB_ID"] == "kkkkkkkkk"][col_to_keep]

# path = os.getcwd()+ "/app-root/repo/csv/movie_info_reduced.csv"
# movie_table_sorted_by_pop = movie_table.sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()



"""
create all the data frame divided by genre, it's much faster! already ordered by pop
"""

movie_table_action = movie_table_all[movie_table_all["Action"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
#print movie_table_action.head()
#movie_table_action.drop(col_to_drop, inplace=True)
movie_table_action.reset_index(drop=True, inplace=True)
#print movie_table_action.head()



movie_table_adventure = \
    movie_table_all[movie_table_all["Adventure"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[col_to_keep].copy()

#movie_table_adventure.drop(col_to_drop, inplace=True)
movie_table_adventure.reset_index(drop=True, inplace=True)

movie_table_animation = \
    movie_table_all[movie_table_all["Animation"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[col_to_keep].copy()
#movie_table_animation.drop(col_to_drop, inplace=True)
movie_table_animation.reset_index(drop=True, inplace=True)

movie_table_children = \
    movie_table_all[movie_table_all["Children"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[col_to_keep].copy()
movie_table_children.reset_index(drop=True, inplace=True)

movie_table_comedy = movie_table_all[movie_table_all["Comedy"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_comedy.reset_index(drop=True, inplace=True)

movie_table_crime = movie_table_all[movie_table_all["Crime"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_crime.reset_index(drop=True, inplace=True)

movie_table_documentary = \
    movie_table_all[movie_table_all["Documentary"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_documentary.reset_index(drop=True, inplace=True)

movie_table_drama = movie_table_all[movie_table_all["Drama"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_drama.reset_index(drop=True, inplace=True)

movie_table_fantasy = movie_table_all[movie_table_all["Fantasy"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_fantasy.reset_index(drop=True, inplace=True)

movie_table_horror = movie_table_all[movie_table_all["Horror"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_horror.reset_index(drop=True, inplace=True)

movie_table_musical = movie_table_all[movie_table_all["Musical"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_musical.reset_index(drop=True, inplace=True)

movie_table_romance = movie_table_all[movie_table_all["Romance"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_romance.reset_index(drop=True, inplace=True)

movie_table_scifi = movie_table_all[movie_table_all["SciFi"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_scifi.reset_index(drop=True, inplace=True)

movie_table_thriller = \
    movie_table_all[movie_table_all["Thriller"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[col_to_keep].copy()
movie_table_thriller.reset_index(drop=True, inplace=True)

movie_table_western = movie_table_all[movie_table_all["Western"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_western.reset_index(drop=True, inplace=True)

print "CREATED ALL THE TABLES"


def get_table_by_genre(genre):
    return {
        'Action': lambda: movie_table_action.copy(),
        'Adventure': lambda: movie_table_adventure.copy(),
        'Animation': lambda: movie_table_animation.copy(),
        'Children': lambda: movie_table_children.copy(),
        'Comedy': lambda: movie_table_comedy.copy(),
        'Crime': lambda: movie_table_crime.copy(),
        'Documentary': lambda: movie_table_documentary.copy(),
        'Drama': lambda: movie_table_drama.copy(),
        'Fantasy': lambda: movie_table_fantasy.copy(),
        'Horror': lambda: movie_table_horror.copy(),
        'Musical': lambda: movie_table_musical.copy(),
        'Romance ': lambda: movie_table_romance.copy(),
        'SciFi': lambda: movie_table_scifi.copy(),
        'Thriller': lambda: movie_table_thriller.copy(),
        'Western': lambda: movie_table_western.copy(),
    }.get(genre)


def get_table(table):
    """

    :rtype: DataFrame
    """
    return {
        'empty_table': lambda: empty_df.copy(),
        'all_table': lambda: movie_table_all.copy()[col_to_keep]
    }.get(table)


#########################################


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
