from core.database_manager import db
from core.database_manager.trailer_seen import TrailerSeen
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_rate',methods=["POST"])
def save_rec_rate():
    print "save_rec_rate"
    json_data = request.get_json(force=True)
    print json_data
    is_skipped=0
    if json_data["rate"]==-1:
        is_skipped=1
    rate = TrailerSeen(json_data["rated_by"], json_data["imdb_id"], json_data["rate"],is_skipped,json_data["rec_type"])
    print rate
    db.session.add(rate)
    db.session.commit()
    return jsonify({})
