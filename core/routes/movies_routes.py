import random
from core import movie_table
from core import mes_core
from flask import request, jsonify, send_file
import json
import os
from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_rates import TrailerRate
from core.database_manager import db

from pandas import Series

movie_table_sorted_by_pop = movie_table.sort_values(by=["IMDB_VOTES"], ascending=[0]).copy()

ALL_GENRES = {
    'ACTION': 'Action',
    'ADVENTURE': 'Adventure',
    'ANIMATION': 'Animation',
    'CHILDREN': 'Children',
    'COMEDY': 'Comedy',
    'CRIME': 'Crime',
    'DOCUMENTARY': 'Documentary',
    'DRAMA': 'Drama',
    'FANTASY': 'Fantasy',
    'FILMNOIR': 'FilmNoir',
    'HORROR': 'Horror',
    'IMAX': 'IMAX',
    'MUSICAL': 'Musical',
    'MISTERY': 'Mystery',
    'ROMANCE ': 'Romance',
    'SCIFI': 'SciFi',
    'THRILLER': 'Thriller',
    'WAR': 'War',
    'WESTERN': 'Western',
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



@mes_core.route('/')
def home_route():
    return jsonify({"test"})

@mes_core.route('/movies_rated_by')
def movies_rated_by():
    user_id = request.args.get('user_id')
    limit = request.args.get('limit')

    rated_by_user = TrailerRate.query.filter_by(rated_by=user_id).all()
    resp = {}
    i = 0
    for rate in rated_by_user:
        print rate.get_imdb_id()
        imdb_id = rate.get_imdb_id()
        movie = movie_table_sorted_by_pop[movie_table_sorted_by_pop["IMDB_ID"] == imdb_id]
        movie = movie.to_json()
        resp.update({i: movie})
        i += 1
    return jsonify(resp)


@mes_core.route('/get_movies', methods=['GET'])
def get_movies():
    num_movies = request.args.get('num_movies')
    genres = request.args.get('genres')
    query_type = request.args.get('type')
    years = request.args.get('years')

    Corner_Motion = request.args.get('Corner_Motion')
    Color_variance = request.args.get('Color_variance')
    Object_Motion = request.args.get('Object_Motion')
    Lightening_Key = request.args.get('Lightening_Key')

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
        if (genres == "SciFi"):
            genres = "Sci-Fi"
        tmp_table = tmp_table[tmp_table['GENRES'].str.contains(genres)]
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
