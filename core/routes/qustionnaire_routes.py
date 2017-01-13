from core.database_manager import db
from core.database_manager.questionnaire import Questionnaire
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_quest',methods=["POST"])
def save_quest():
    json_data = request.get_json(force=True)

    questions = Questionnaire(json_data["user_id"],
                              json_data["questions"][0],
                              json_data["questions"][1],
                              json_data["questions"][2],
                              json_data["questions"][3],
                              json_data["questions"][4],
                              json_data["questions"][5],
                              json_data["questions"][6],
                              json_data["questions"][7],
                              json_data["questions"][8],
                              json_data["questions"][9],
                              json_data["questions"][10],
                              json_data["questions"][11],
                              json_data["questions"][12],
                              json_data["questions"][13])
    db.session.add(questions)
    db.session.commit()
    return jsonify({})
