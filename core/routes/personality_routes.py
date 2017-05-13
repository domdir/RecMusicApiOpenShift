from core.database_manager import db
from core.database_manager.personality import Personality
from flask import request,jsonify
from core import mes_core


@mes_core.route('/save_personality_questions',methods=["POST"])
def save_personality_questions():
    json_data = request.get_json(force=True)
    questions = Personality(json_data["user_id"],
                              json_data["questions"][0][1],
                              json_data["questions"][1][1],
                              json_data["questions"][2][1],
                              json_data["questions"][3][1],
                              json_data["questions"][4][1],
                              json_data["questions"][5][1],
                              json_data["questions"][6][1],
                              json_data["questions"][7][1],
                              json_data["questions"][8][1],
                              json_data["questions"][9][1]
                             )
    
    db.session.add(questions)
    db.session.commit()
    return jsonify({})
