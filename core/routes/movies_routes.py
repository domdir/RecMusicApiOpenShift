import random
from core import movie_table_all, col_to_keep, movie_table_all_ordered, empty_df
from core import mes_core, get_table, get_table_by_genre
from flask import request, jsonify, send_file
import json
import os
from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_seen import TrailerSeen
from core.database_manager import db

from pandas import Series


@mes_core.route('/movies_seen_by')
def movies_rated_by():
    user_id = request.args.get('user_id')
    limit = request.args.get('limit')
    show_skipped = request.args.get('show_skipped')

    try:
        limit=int(limit)
    except:
        limit=5

    try:
        show_skipped=int(show_skipped)
    except:
        show_skipped=0



    if show_skipped:
        rated_by_user = TrailerSeen.query.filter_by(seen_by=user_id).limit(int(limit))
    else:
        rated_by_user = TrailerSeen.query.filter_by(seen_by=user_id, is_skipped=0).limit(int(limit))

    resp = {}
    for rate in rated_by_user:
        imdb_id = rate.imdb_id
        rate = rate.rate
        all_movie = get_table("all_table")()
        movie = all_movie[all_movie["IMDB_ID"] == imdb_id]
        print movie
        print imdb_id
        movie.loc["user_rate"] = rate
        movie.reset_index(drop=True, inplace=True)
        t = movie.iloc[0]
        m_j = t.to_json()
        resp.update({len(resp): m_j})

    return jsonify(resp)


@mes_core.route('/get_ini_movies', methods=['GET'])
def get_ini_movies():
    num_of_movies = request.args.get('num_of_movies')
    genre = request.args.get('genre')
    years = request.args.get('years')
    except_movies = request.args.get('except_movies')

    if not genre or not years:
        return jsonify({})

    if not num_of_movies:
        num_of_movies = 5
    else:
        num_of_movies = int(num_of_movies)

    tmp_table = get_table_by_genre(genre)()


    if not len(except_movies):
        movie_to_exclude = None
    else:
        movie_to_exclude = except_movies.split(",")

    if movie_to_exclude:
        tmp_table = tmp_table[~tmp_table["IMDB_ID"].isin(Series(movie_to_exclude))]
        tmp_table.reset_index(drop=True, inplace=True)

    try:
        int(years)
    except:
        years = None

    if years:
        years_complete = []
        for i in range(0, 10):
            years_complete.append(int(years) + i)
        years_series = Series(years_complete)
        tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
        tmp_table.reset_index(drop=True, inplace=True)

    movies_selected = {}
    tmp = []
    safe_iter = 0

    if len(tmp_table):
        while (len(movies_selected) <= num_of_movies - 1) and (safe_iter < 20):
            #print movies_selected
            if len(tmp_table.index) < 200:
                j = random.randrange(1, len(tmp_table.index))
            else:
                j = random.randrange(1, 200)
            safe_iter += 1
            if j not in tmp:
                movie = tmp_table.iloc[j]
                movie = movie.to_json()
                movies_selected.update({len(movies_selected): movie})
                tmp.append(j)
        return jsonify(movies_selected)
    else:
        return jsonify({})


genres_list = [

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



feature_converter = {
    "VERY_LOW": [0, 0.2],
    "LOW": [0.2, 0.4],
    "MEDIUM": [0.4, 0.6],
    "HIGH": [0.6, 0.8],
    "VERY_HIGH": [0.8, 1],
}


@mes_core.route('/get_movies', methods=['GET'])
def get_movies():
    num_movies = request.args.get('num_of_movies')
    genre = request.args.get('genre')
    order_by = request.args.get('order_by')
    years = request.args.get('years')
    requested_by = request.args.get('requested_by')

    f1 = request.args.get('f1')
    f2 = request.args.get('f2')
    f4 = request.args.get('f4')
    f6 = request.args.get('f6')

    f1_c = feature_converter.get(f1)
    f2_c = feature_converter.get(f2)
    f4_c = feature_converter.get(f4)
    f6_c = feature_converter.get(f6)

    # filter by genre
    if genre in genres_list:
        tmp_table = get_table_by_genre(genre)()
    else:
        tmp_table = get_table("all_table")()

    # years
    if not years:
        return jsonify({})

    # filter by years

    try:
        int(years)
    except:

        years = None

    if years:
        years_complete = []
        for i in range(0, 10):
            years_complete.append(int(years) + i)
        years_series = Series(years_complete)
        tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
        tmp_table.reset_index(drop=True, inplace=True)
    len(tmp_table.index)

    # filter by features

    if f1 != "ALL":
        tmp_table = tmp_table[(tmp_table["f1"] > f1_c[0]) & (tmp_table["f1"] < f1_c[1])]
    if f2 != "ALL":
        tmp_table = tmp_table[(tmp_table["f2"] > f2_c[0]) & (tmp_table["f2"] < f2_c[1])]
    if f4 != "ALL":
        tmp_table = tmp_table[(tmp_table["f4"] > f4_c[0]) & (tmp_table["f4"] < f4_c[1])]
    if f6 != "ALL":
        tmp_table = tmp_table[(tmp_table["f6"] > f6_c[0]) & (tmp_table["f6"] < f6_c[1])]

    movies = {}
    try:
        num_movies = int(num_movies)
    except:
        num_movies = 10

    tmp_table = tmp_table.sort_values(by=["IMDB_VOTES"], ascending=[0])

    # len(tmp_table.index)
    # tmp_table.head()
    movies_selected = tmp_table.iloc[:num_movies]

    movies_selected.reset_index(drop=True, inplace=True)

    # movies_selected.head()

    rated_by_user = TrailerSeen.query.filter_by(seen_by=requested_by, is_skipped=0)
    rated_by_user_imdbid = []

    for rate in rated_by_user:
        rated_by_user_imdbid.append(rate.imdb_id)

    # "LEN!!!"
    # len(movies_selected.index)

    for i, r in movies_selected.iterrows():
        if r["IMDB_ID"] in rated_by_user_imdbid:
            r["IS_ALREADY_VOTED"] = True
            # "already voted"
        else:
            r["IS_ALREADY_VOTED"] = False
            # "NOT already voted"

        m_j = r.to_json()
        # m_j
        movies.update({len(movies): m_j})

    return jsonify(movies)
