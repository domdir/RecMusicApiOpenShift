import random
from core import movie_table_all, col_to_keep, movie_table_all_ordered, empty_df
from core import mes_core
from flask import request, jsonify, send_file
import json
import os
from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_seen import TrailerSeen
from core.database_manager import db

from pandas import Series

"""
create all the data frame divided by genre, it's much faster! already ordered by pop
"""

movie_table_action = movie_table_all[movie_table_all["Action"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_adventure = \
    movie_table_all[movie_table_all["Adventure"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_animation = \
    movie_table_all[movie_table_all["Animation"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_children = \
    movie_table_all[movie_table_all["Children"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_comedy = movie_table_all[movie_table_all["Comedy"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_crime = movie_table_all[movie_table_all["Crime"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_documentary = \
    movie_table_all[movie_table_all["Documentary"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_drama = movie_table_all[movie_table_all["Drama"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_fantasy = movie_table_all[movie_table_all["Fantasy"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_horror = movie_table_all[movie_table_all["Horror"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_musical = movie_table_all[movie_table_all["Musical"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_romance = movie_table_all[movie_table_all["Romance"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_scifi = movie_table_all[movie_table_all["SciFi"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_thriller = \
    movie_table_all[movie_table_all["Thriller"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
        col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

movie_table_western = movie_table_all[movie_table_all["Western"] == 1].sort_values(by=["IMDB_VOTES"], ascending=[0])[
    col_to_keep].copy()
movie_table_action.reset_index(drop=True, inplace=True)

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
        'all_table': lambda: movie_table_all.copy()
    }.get(table)


#########################################


"""

@mes_core.route('/save_genres_liked', methods=['POST'])
def save_genres_liked():
    print "save_genres_liked"
    json_data = request.get_json(force=True)
    print json_data
    print json_data["genres_liked"]
    print json_data["genres_liked"][0]
    genres = UserFavoriteGenre(json_data["user_id"], json_data["genres_liked"][0], json_data["genres_liked"][1],
                               json_data["genres_liked"][2], json_data["genres_liked"][3])
    db.session.add(genres)
    db.session.commit()
    return jsonify({})
"""

"""


@mes_core.route('/movies_seen_by')
def movies_rated_by():
    user_id = request.args.get('user_id')
    limit = request.args.get('limit')
    skipped = request.args.get('skipped')
    rec_type = request.args.get('rec_type')

    print "userId " + user_id
    print "limit " + limit
    print "skipped " + skipped
    print "rec_type " + rec_type

    if not limit:
        print "NOT LIMIT"
        limit = 5

    if not skipped:
        print "NOT SKIPPED"
        skipped = 0

    if skipped:
        rated_by_user = TrailerSeen.query.filter_by(rated_by=user_id).limit(int(limit))
    else:
        rated_by_user = TrailerSeen.query.filter_by(rated_by=user_id, skipped=0).limit(int(limit))

    resp = {}
    i = 0
    for rate in rated_by_user:
        imdb_id = rate.imdb_id
        rate = rate.rate
        movie = movie_table_sorted_by_pop[movie_table_sorted_by_pop["IMDB_ID"] == imdb_id].copy()
        movie["user_rate"] = rate

        movie.reset_index(drop=True)
        for j in range(0, len(movie)):
            m_j = movie.iloc[j]
            m_j = m_j.to_json()
            resp.update({i: m_j})
            i += 1
    return jsonify(resp)
"""


@mes_core.route('/get_ini_movies', methods=['GET'])
def get_ini_movies():
    print "get_ini_movies"

    genre = request.args.get('genre')
    years = request.args.get('years')

    if not genre or not years:
        print "return"
        return jsonify({})

    tmp_table = get_table_by_genre(genre)()

    print years

    years_split = years.split(",")
    print years_split
    years_complete = []
    for year in years_split:
        for i in range(0, 10):
            years_complete.append(int(year) + i)

    #print years_complete
    years_series = Series(years_complete)
    #print years_series
    tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
    #tmp_table.drop('IMDB_VOTES', axis=1, inplace=True)
    tmp_table.reset_index(drop=True, inplace=True)

   #print tmp_table.head()

    movies_selected = {}
    tmp = []
    safe_iter = 0
    print "before while"
    while (len(movies_selected) < 5) and (safe_iter < 100):
        print "inside while"
        print movies_selected
        if len(tmp_table.index) < 50:
            print "IF"
            j = random.randrange(1, len(tmp_table.index))
        else:
            print "ELSE"
            j = random.randrange(1, 50)
            print "AFTER RAND"
        safe_iter += 1
        if j not in tmp:
            print "IN J IF"
            movie = tmp_table.iloc[j]
            print "1"
            movie = movie.to_json()
            print "2"
            movies_selected.update({len(movies_selected): movie})
            print "3"
            tmp.append(j)
            print "4"
    return movies_selected


"""

@mes_core.route('/get_movies', methods=['GET'])
def get_movies():
    num_movies = request.args.get('num_movies')
    genres = request.args.get('genres')
    order_by = request.args.get('order_by')
    years = request.args.get('years')

    f1 = request.args.get('f1')
    f2 = request.args.get('f2')
    f4 = request.args.get('f4')
    f6 = request.args.get('f6')

    tmp_table = get_table("empty_table")

    if genres:
        genres_list = genres.split(",")
        for genre in genres_list:
            tmp_table.concat(tmp_table, get_table_by_genre(genre))
    else:
        tmp_table = tmp_table.concat(tmp_table, get_table("all_table"))
    print years
    if not years:
        return jsonify({})

    years_split = years.split(",")
    print years_split
    years_complete = []
    for year in years_split:
        for i in range(0, 10):
            years_complete.append(int(year) + i)

    years_series = Series(years_complete)

    tmp_table = tmp_table[tmp_table['YEAR'].isin(years_series)]
    tmp_table = tmp_table.sort_values(by=["IMDB_VOTES"], ascending=[0])
    tmp_table.reset_index(drop=True)

    if num_movies:
        num_movies = int(num_movies)
        if num_movies > 20:
            num_movies = 10
    else:
        num_movies = 10

    movies = {}
    tmp = []
    safe_iter = 0

    # ADD IF THE MOVIES IS ALREADY VOTED
    while (len(movies) < num_movies) and (safe_iter < 100):
        if len(tmp_table) < 100:
            j = random.randrange(1, len(tmp_table))
        else:
            j = random.randrange(1, 100)
        safe_iter += 1
        if j not in tmp:
            movie = tmp_table.iloc[j]
            movie = movie.to_json()
            movies.update({j: movie})
            tmp.append(j)
            # json_string = json.dumps(movies)
            # print json_string
    print len(movies)
    return jsonify(movies)


# @mes_core.route('/get_genres', methods=['GET'])
# def get_genres():
#    return jsonify(MAIN_GENRES)


# @mes_core.route('/get_img/<genre_img_name>', methods=['GET'])
# def get_img(genre_img_name):
#    img_id = request.args.get('num_movies')
#    if os.path.isfile(os.getcwd() + '/static/genre/' + genre_img_name):
#        return send_file(os.getcwd() + '/static/genre/' + genre_img_name, mimetype='image')
#    else:
#        return "not exist"
"""
