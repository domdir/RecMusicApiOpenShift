'''
Created on 13 mag 2017

@author: Antonio
'''
from core.database_manager import db
from core.database_manager.load_page import TimeLog
from flask import request, jsonify
from core import mes_core

@mes_core.route('/load_page', methods=["POST"])
def load_page():
    json_data = request.get_json(force=True)
    print(json_data)
    fields = ["SignInPage", "SignUpPage", "DemographicPage", "PersonalityPage", "PreCatalogPage",
            "Ini0Page", "Ini1Page", "Ini1Page", "Ini2Page", "Ini3Page", "Ini4Page", "Ini5Page",
            "ProfilePage", "ExplorePage", "RecForYouPage"]
    fullfields = []
    for i in range(len(fields)):
        field = fields[i]
        found = False
        jdata = json_data["pageTime"]
        for key in jdata.iterkeys():
            if key == field:
                fullfields.append(field) 
    for field in fields:
        if(field not in fullfields):
            json_data["pageTime"][field] = ""
    print(json_data)
    time = TimeLog(
        json_data["user_id"],
                              json_data["pageTime"]["SignUpPage"],
                              json_data["pageTime"]["SignInPage"],
                              json_data["pageTime"]["DemographicPage"],
                              json_data["pageTime"]["PersonalityPage"],
                              json_data["pageTime"]["PreCatalogPage"],
                              json_data["pageTime"]["Ini0Page"],
                              json_data["pageTime"]["Ini1Page"],
                              json_data["pageTime"]["Ini2Page"],
                              json_data["pageTime"]["Ini3Page"],
                              json_data["pageTime"]["Ini4Page"],
                              json_data["pageTime"]["Ini5Page"],
                              json_data["pageTime"]["ProfilePage"],
                              json_data["pageTime"]["ExplorePage"],
                              json_data["pageTime"]["RecForYouPage"]
                             )
    db.session.add(time)
    db.session.commit()
    return jsonify({})
    
