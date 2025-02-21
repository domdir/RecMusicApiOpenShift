from core.database_manager import db
from core.database_manager.questionnaire import Questionnaire
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_quest',methods=["POST"])
def save_quest():
    json_data = request.get_json(force=True)
    print(json_data["timestamps"])
    questions = Questionnaire(json_data["user_id"],
                              json_data["recs"][0],
                              json_data["recs"][1],
                              json_data["recs"][2],
                              json_data["timestamps"][0],
                              json_data["timestamps"][1],
                              json_data["timestamps"][2],
                              json_data["timestamps"][3],
                              json_data["timestamps"][4],
                              json_data["timestamps"][5],
                              json_data["timestamps"][6],
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
                              json_data["questions"][13],
                              json_data["questions"][14],
                              json_data["questions"][15],
                              json_data["questions"][16],
                              json_data["questions"][17],
                              json_data["questions"][18],
                              json_data["questions"][19],
                              json_data["questions"][20],
                              json_data["questions"][21],
                              json_data["questions"][22],
                              json_data["questions"][23],
                              json_data["questions"][24],
                              json_data["questions"][25],
                              json_data["questions"][26],
                              json_data["questions"][27])
    db.session.add(questions)
    db.session.commit()
    return jsonify({})
