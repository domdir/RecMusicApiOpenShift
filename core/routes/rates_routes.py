from core.database_manager import db
from core.database_manager.trailer_ini_rates import TrailerIniRate
from core.database_manager.trailer_rates import TrailerRate
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_ini_rate',methods=["POST"])
def save_ini_rate():
    json_data = request.get_json(force=True)
    print json_data
    rate = TrailerIniRate(json_data["rated_by"], json_data["movie_id"], json_data["rate"])
    print json_data["movie_id"]
    db.session.add(rate)
    db.session.commit()
    return jsonify({})


@mes_core.route('/save_rec_rate',methods=["POST"])
def save_rec_rate():
    json_data = request.get_json(force=True)
    print json_data
    rate = TrailerRate(json_data["rated_by"], json_data["movie_id"], json_data["rate"])
    print json_data["movie_id"]
    db.session.add(rate)
    db.session.commit()
    return jsonify({})
