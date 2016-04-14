from core import mes_core
from flask import request, jsonify

from core.database_manager import UserFavoriteGenre
from core.database_manager import db


@mes_core.route('/save_fav_genre', methods=['POST'])
def save_genres_liked():
    print "save_genres_liked"
    json_data = request.get_json(force=True)
    print json_data
    genres = UserFavoriteGenre(json_data["user_id"], json_data["fav_genre"],None,None,None)
    db.session.add(genres)
    db.session.commit()
    return jsonify({})


@mes_core.route('/save_genres_liked', methods=['POST'])
def save_genres_liked():
    print "save_genres_liked"
    json_data = request.get_json(force=True)
    print json_data
    genres = UserFavoriteGenre(json_data["user_id"], json_data["genres_liked"],
                               json_data["genres_liked"], json_data["genres_liked"], json_data["genres_liked"])
    db.session.add(genres)
    db.session.commit()
    return jsonify({})


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
