from core.database_manager import db
from core.database_manager.dem_questionnaire import DemQuestionnaire
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_dem_quest',methods=["POST"])
def save_dem_quest():
    json_data = request.get_json(force=True)

    questions = DemQuestionnaire(json_data["user_id"],
                              json_data["questions"]["age"],
                              json_data["questions"]["gender"],
                              json_data["questions"]["nationality"],
                              json_data["questions"]["question1"][0],
                              json_data["questions"]["question1"][1],
                              json_data["questions"]["question1"][2],
                              json_data["questions"]["question1"][3],
                              json_data["questions"]["question1"][4],
                              json_data["questions"]["question1"][5],
                              json_data["questions"]["question1"][6],
                              json_data["questions"]["question1"][7],
                              json_data["questions"]["question1"][8],
                              json_data["questions"]["question1"][9],
                              json_data["questions"]["question1"][10],
                              json_data["questions"]["question2"],
                              json_data["questions"]["twitter"],
                              json_data["questions"]["fb"],
                              json_data["questions"]["instagram"],
                              json_data["questions"]["lastfm"],
                              json_data["questions"]["spotify"])
    db.session.add(questions)
    db.session.commit()
    return jsonify({})
