from pandas import Series
from core import mes_core, get_table
from flask import request, jsonify

from core.database_manager import TrailerSeen
from core.rec_engine import random_rec, rec_types

from core.rec_engine import tag_rec
from core.rec_engine import audio_ivec_rec
from core.rec_engine import audio_blf_rec
from core.rec_engine import genre_rec
from core.rec_engine import feature_rec
from core.rec_engine import audio_rec
from core.rec_engine import video_avf_rec
from core.rec_engine import video_deep_rec
from core.rec_engine import pers_rec

rec_router = {
    0: tag_rec.tag_rec,
    1: genre_rec.genre_rec,
    2: audio_ivec_rec.audio_ivec_rec,
    3: audio_blf_rec.audio_blf_rec,
    4: video_avf_rec.video_avf_rec,
    5: video_deep_rec.video_deep_rec
}


@mes_core.route('/get_rec', methods=["GET"])
def get_rec():
    "get_rec"
    rec_request_list = request.args.get('rec_request_list')
    for_who = request.args.get('for_who')

    if not for_who:
        return jsonify({})


    try:
        rec_request_list = rec_request_list.split(",")
    except:
        return jsonify({})

    resp = {}
    i = 0
    movie_to_exclude = TrailerSeen.query.filter_by(seen_by=for_who)
    imdb_to_exclude = []
    for m in movie_to_exclude:
        imdb_to_exclude.append(m.imdb_id)

    for req in rec_request_list:
        rec_type = rec_types.get(req, "RANDOM")

        table_to_use = get_table('all_table')()

        table_to_use = table_to_use[~table_to_use["IMDB_ID"].isin(Series(imdb_to_exclude))]

        t = rec_router.get(rec_type, random_rec.random_rec)(table_to_use)
        t

        i += 1
        resp.update({i: t})

    return jsonify(resp)


##############

@mes_core.route('/get_tag_rec', methods=["GET"])
def get_tag_rec():

    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = tag_rec.tag_rec(for_who, int(num_of_rec))

    return jsonify(t)


@mes_core.route('/get_audio_ivec_rec', methods=["GET"])
def get_audio_ivec_rec():

    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = audio_ivec_rec.audio_ivec_rec(for_who, int(num_of_rec))

    return jsonify(t)


@mes_core.route('/get_audio_blf_rec', methods=["GET"])
def get_audio_blf_rec():

    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = audio_blf_rec.audio_blf_rec(for_who, int(num_of_rec))

    return jsonify(t)


@mes_core.route('/get_genre_rec', methods=["GET"])
def get_genre_rec():
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    t = genre_rec.genre_rec(for_who, int(num_of_rec))

    return jsonify(t)


@mes_core.route('/get_feature_rec', methods=["GET"])
def get_feature_rec():
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')

    t = feature_rec.feature_rec(for_who, int(num_of_rec))

    return jsonify(t)

@mes_core.route('/get_audio_rec', methods=["GET"])
def get_audio_rec():
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = audio_rec.audio_rec(for_who, int(num_of_rec))

    return jsonify(t)

@mes_core.route('/get_video_avf_rec', methods=["GET"])
def get_video_avf_rec():
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = video_avf_rec.video_avf_rec(for_who, int(num_of_rec))

    return jsonify(t)

@mes_core.route('/get_video_deep_rec', methods=["GET"])
def get_video_deep_rec():
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    t = video_deep_rec.video_deep_rec(for_who, int(num_of_rec))

    return jsonify(t)

@mes_core.route('/get_pers_rec', methods=["GET"])
def get_pers_rec():

    num_of_rec = request.args.get('num_of_rec')
    num_of_skip = request.args.get('num_of_skip')
    for_who = request.args.get('for_who')
    pers_type = request.args.get('type')
    t = pers_rec.pers_rec(for_who, int(num_of_rec), int(num_of_skip), pers_type)

    return jsonify(t)