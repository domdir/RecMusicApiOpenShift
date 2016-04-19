# coding=utf-8
#
# Created with ♥ by Gianluca Chiap (@forgiangi)
#

import os
import pandas as pd

COL_MAPPING = [
    'IMDB_ID',
    'MOVIELENS_ID',
    'TITLE',
    'GENRES',
    'Action',
    'Adventure',
    'Animation',
    'Children',
    'Comedy',
    'Crime',
    'Documentary',
    'Drama',
    'Fantasy',
    'FilmNoir',
    'Horror',
    'IMAX',
    'Musical',
    'Mystery',
    'Romance',
    'SciFi',
    'Thriller',
    'War',
    'Western',
    'YEAR',
    'PLOT',
    'LENGTH',
    'POSTER',
    'YOU_TUBE_ID',
    'IMDB_RATING',
    'IMDB_VOTES',
    'TOMATO_METER',
    'TOMATO_RATING',
    'TOMATO_USER_METER',
    'TOMATO_USER_RATING',
    'f1',
    'f2',
    'f3',
    'f4',
    'f5',
    'f6',
    'f7',
]

movie_table = pd.read_csv(os.getcwd() + "/movies_info.csv", ",")


class DF_Manipulator:
    """Data frame manipulator class"""
    router = {}

    def __init__(self, data_frame):
        self.df = data_frame.copy()
        for col in self.df.columns:
            self.router.update({col: self.df.columns.get_loc(col)})

    def recompute_router(self):
        self.router.clear()
        for col in self.df.columns:
            self.router.update({col: self.df.columns.get_loc(col)})

    def delete_column(self, *args):
        col_index = []
        #args
        for arg in args:
            arg
            col_index.append(self.router.get(arg))
        col_index
        self.df = self.df.drop(self.df.columns[col_index], axis=1)
        self.recompute_router()
        self.router

    def filert(self, column, condition):
        "filter"

    def order_by(self, col_names, ascending):
        self.df.sort_values(by=col_names, ascending=[ascending])

    def get_sf(self):
        return self.df

    #def __repr__(self):
        #return '<router: {0} >'.format(self.router)


t = DF_Manipulator(movie_table.copy())

#t

t.delete_column("f1")
t.delete_column("f2")
