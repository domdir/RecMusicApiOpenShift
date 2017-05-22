'''
Created on 13 mag 2017

@author: Antonio
'''
from core.database_manager import db
from core.database_manager.load_page import TimeLog
from flask import request,jsonify
from core import mes_core

@mes_core.route('/load_page',methods=["POST"])
def load_page():
    json_data = request.get_json(force=True)
    for key, value in json_data.iteritems():
        print (key, value)
    
    #time=TimeLog(
        #(json_data["user_id"],
                             # json_data["pageTime"]
                             #))
    return jsonify({})
    