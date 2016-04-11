from core import mes_core

from flask import request, jsonify, send_file

@mes_core.route("/")
def home_route():
    return jsonify({"hello"})
