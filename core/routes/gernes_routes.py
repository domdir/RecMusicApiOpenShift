from core import mes_core
from flask import request, jsonify

from core.database_manager import UserFavoriteGenre
from core.database_manager import db


@mes_core.route('/save_genres_liked', methods=['POST'])
def save_genres_liked():
    json_data = request.get_json(force=True)

    try:
        genre_0 = json_data["genres_liked"][0]
    except:
        genre_0 = "NONE"

    try:
        genre_1 = json_data["genres_liked"][1]
    except:
        genre_1 = "NONE"

    try:
        genre_2 = json_data["genres_liked"][2]
    except:
        genre_2 = "NONE"

    try:
        genre_3 = json_data["genres_liked"][3]
    except:
        genre_3 = "NONE"

    genres = UserFavoriteGenre(json_data["user_id"], genre_0,
                               genre_1, genre_2, genre_3)
    db.session.add(genres)
    db.session.commit()
    return jsonify({})


"""


@mes_core.route('/save_genres_liked', methods=['POST'])
def save_genres_liked():
    "save_genres_liked"
    json_data = request.get_json(force=True)
    json_data
    json_data["genres_liked"]
    json_data["genres_liked"][0]
    genres = UserFavoriteGenre(json_data["user_id"], json_data["genres_liked"][0], json_data["genres_liked"][1],
                               json_data["genres_liked"][2], json_data["genres_liked"][3])
    db.session.add(genres)
    db.session.commit()
    return jsonify({})
"""
