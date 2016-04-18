from pandas import Series
from core import mes_core, get_table
from flask import request, jsonify

from core.database_manager import TrailerSeen
from core.rec_engine import random_rec, rec_types

from core.rec_engine import tag_rec
from core.rec_engine import genre_rec
from core.rec_engine import feature_rec

rec_router = {
    0: random_rec.random_rec,
    2: genre_rec.genre_rec,
    3: tag_rec.tag_rec,
    4: feature_rec.feature_rec
}


@mes_core.route('/get_rec', methods=["GET"])
def get_rec():
    print "get_rec"
    rec_request_list = request.args.get('rec_request_list')
    for_who = request.args.get('for_who')

    if not for_who:
        return jsonify({})

    print rec_request_list

    try:
        rec_request_list = rec_request_list.split(",")
    except:
        return jsonify({})

    print rec_request_list
    resp = {}
    i = 0
    movie_to_exclude = TrailerSeen.query.filter_by(seen_by=for_who)
    imdb_to_exclude=[]
    for m in movie_to_exclude:
        imdb_to_exclude.append(m.imdb_id)


    for req in rec_request_list:
        rec_type = rec_types.get(req, "RANDOM")

        table_to_use = get_table('all_table')()

        table_to_use = table_to_use[~table_to_use["IMDB_ID"].isin(Series(imdb_to_exclude))]

        t = rec_router.get(rec_type, random_rec.random_rec)(table_to_use)
        print t

        i += 1
        resp.update({i: t})

    return jsonify(resp)


##############

@mes_core.route('/get_tag_rec', methods=["GET"])
def get_tag_rec():
    print "get_rec"
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    num_of_rec = int(num_of_rec)

    print num_of_rec
    resp = {}
    i = 0
    table_to_use = get_table('all_table')()
    for req in range(0, num_of_rec):
        t = tag_rec.tag_rec(table_to_use)
        resp.update({i: t})
        i += 1
    return jsonify(resp)


@mes_core.route('/get_genre_rec', methods=["GET"])
def get_genre_rec():
    print "get_rec"
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    num_of_rec = int(num_of_rec)

    print num_of_rec
    resp = {}
    i = 0
    table_to_use = get_table('all_table')()
    for req in range(0, num_of_rec):
        t = genre_rec.genre_rec(table_to_use)
        resp.update({i: t})
        i += 1
    return jsonify(resp)


@mes_core.route('/get_feature_rec', methods=["GET"])
def get_feature_rec():
    print "get_rec"
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    num_of_rec = int(num_of_rec)

    print num_of_rec
    resp = {}
    i = 0
    table_to_use = get_table('all_table')()
    t = feature_rec.feature_rec(table_to_use,for_who)

    return jsonify(t)
