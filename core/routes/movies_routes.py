import random
from core import movie_table_sorted_by_pop
from core import mes_core
from flask import request, jsonify, send_file
import json
import os
from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_seen import TrailerSeen
from core.database_manager import db

from pandas import Series


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



@mes_core.route('/movies_seen_by')
def movies_rated_by():
    user_id = request.args.get('user_id')
    limit = request.args.get('limit')
    skipped=request.args.get('skipped')
    rec_type=request.args.get('rec_type')

    print "userId "+user_id
    print "limit "+ limit
    print "skipped " + skipped
    print "rec_type "+ rec_type

    if not limit:
        print "NOT LIMIT"
        limit=5

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
        rate=rate.rate
        movie = movie_table_sorted_by_pop[movie_table_sorted_by_pop["IMDB_ID"] == imdb_id].copy()
        movie["user_rate"] = rate

        movie.reset_index(drop=True)
        for j in range(0,len(movie)):
            m_j = movie.iloc[j]
            m_j = m_j.to_json()
            resp.update({i: m_j})
            i += 1
    return jsonify(resp)


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

    tmp_table = movie_table_sorted_by_pop.copy()
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

    if genres:
        genres_list =genres.split(",")
        print genres
        #if (genres == "SciFi"):
        #    genres = "Sci-Fi"

        #tmp_table = tmp_table[tmp_table['GENRES'].str.contains(genres)]
        #tmp_table = tmp_table.sort_values(by=["IMDB_VOTES"], ascending=[0])
        #tmp_table.reset_index(drop=True)
    return jsonify({"test"})

    """

    if num_movies:
        num_movies = int(num_movies)
        if num_movies > 20:
            num_movies = 10
    else:
        num_movies = 10

    movies = {}
    tmp = []
    safe_iter = 0

    #ADD IF THE MOVIES IS ALREADY VOTED
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

