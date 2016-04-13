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

    if not limit:
        print "NOT LIMIT"
        limit = 5

    if not show_skipped:
        print "NOT SKIPPED"
        show_skipped = 0

    print "userId " + user_id
    print "limit " + limit
    print "show_skipped " + show_skipped

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
        movie["user_rate"] = rate
        movie.reset_index(drop=True, inplace=True)
        t = movie.iloc[0]
        m_j = t.to_json()
        resp.update({len(resp): m_j})

    return jsonify(resp)


@mes_core.route('/get_ini_movies', methods=['GET'])
def get_ini_movies():
    print "get_ini_movies"
    num_of_movies = request.args.get('num_of_movies')
    genre = request.args.get('genre')
    years = request.args.get('years')

    if not genre or not years:
        return jsonify({})

    if not num_of_movies:
        num_of_movies = 5
    else:
        num_of_movies = int(num_of_movies)

    tmp_table = get_table_by_genre(genre)()

    years_split = years.split(",")
    years_complete = []
    for year in years_split:
        for i in range(0, 10):
            years_complete.append(int(year) + i)

    years_series = Series(years_complete)
    tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
    tmp_table.reset_index(drop=True, inplace=True)

    movies_selected = {}
    tmp = []
    safe_iter = 0
    while (len(movies_selected) <= num_of_movies - 1) and (safe_iter < 20):
        if len(tmp_table.index) < 50:
            j = random.randrange(1, len(tmp_table.index))
        else:
            j = random.randrange(1, 50)
        safe_iter += 1
        if j not in tmp:
            movie = tmp_table.iloc[j]
            movie = movie.to_json()
            movies_selected.update({len(movies_selected): movie})
            tmp.append(j)
    return jsonify(movies_selected)


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


@mes_core.route('/get_movies', methods=['GET'])
def get_movies():
    num_movies = request.args.get('num_of_movies')
    genre = request.args.get('genre')
    order_by = request.args.get('order_by')
    years = request.args.get('years')
    requested_by = request.args.get('requested_by')


    features = request.args.get('features')

    f1 = request.args.get('f1')
    f2 = request.args.get('f2')
    f4 = request.args.get('f4')
    f6 = request.args.get('f6')

    if genre in genres_list:
        tmp_table = get_table_by_genre(genre)()
    else:
        tmp_table = get_table("all_table")()

    #print years
    if not years:
        return jsonify({})

    years_split = years.split(",")
    #print years_split
    years_complete = []
    for year in years_split:
        for i in range(0, 10):
            years_complete.append(int(year) + i)

    years_series = Series(years_complete)

    tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
    tmp_table = tmp_table.sort_values(by=["IMDB_VOTES"], ascending=[0])
    tmp_table.reset_index(drop=True)

    #print genre
    #print num_movies
    #print years

    movies = {}
    try:
        num_movies=int(num_movies)
    except:
        num_movies=10

    tmp_table = tmp_table.sort_values(by=["IMDB_VOTES"], ascending=[0])

    print len(tmp_table.index)
    print tmp_table.head()
    movies_selected = tmp_table.iloc[:num_movies]

    movies_selected.reset_index(drop=True, inplace=True)

    print movies_selected.head()

    rated_by_user = TrailerSeen.query.filter_by(seen_by=requested_by, is_skipped=0)
    rated_by_user_imdbid=[]

    for rate in rated_by_user:
        print rate
        rated_by_user_imdbid.append(rate.imdb_id)

    print rated_by_user_imdbid

    print "LEN!!!"
    print len(movies_selected.index)

    for i, r in movies_selected.iterrows():
        if r["IMDB_ID"] in rated_by_user_imdbid:
            r["IS_ALREADY_VOTED"]=True
            print "already voted"
        else:
            r["IS_ALREADY_VOTED"]=False
            print "NOT already voted"

        m_j = r.to_json()
        # print m_j
        movies.update({len(movies): m_j})

    return jsonify(movies)
