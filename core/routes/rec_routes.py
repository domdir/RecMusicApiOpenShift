"""""
import random
from core import movie_table, mes_core
from flask import request, jsonify, send_file
import time

movie_table_sorted_by_pop = movie_table.sort_values(by=['IMDB_VOTES'], ascending=[0])


@mes_core.route('/get_rec', methods=["GET"])
def get_rec():
    # time.sleep(5)
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    print "num of rec"+num_of_rec
    if num_of_rec:
        num_movies = int(num_of_rec)
        if num_movies > 20:
            num_movies = 1
    else:
        num_movies = 1
    movies = {}

    for i in range(0, num_movies):
        print i
        j = random.randrange(1, 100)
        movie = movie_table_sorted_by_pop.iloc[j]
        movie = movie.to_json()
        movies.update({i: movie})
        # json_string = json.dumps(movies)
        # print json_string

    print len(movies)
    return jsonify(movies)
"""""