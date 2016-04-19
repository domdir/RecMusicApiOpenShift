from core import mes_core
from flask import request, jsonify, send_file
from core.database_manager import db

@mes_core.route('/', methods=["GET"])
def test():
    return jsonify({})


@mes_core.route('/reset', methods=["GET"])
def reset():
    db.drop_all()
    db.create_all()
    "db erased"
    return jsonify({})
