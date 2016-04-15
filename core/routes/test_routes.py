from core import mes_core
from flask import request, jsonify, send_file
from core.database_manager import db
import requests
@mes_core.route('/', methods=["GET"])
def test():
    return jsonify({})


@mes_core.route('/reset', methods=["GET"])
def reset():
    db.drop_all()
    db.create_all()
    print "db erased"
    return jsonify({})


@mes_core.route('/test_aws', methods=["GET"])
def test_aws():
    r = requests.get("http://52.38.244.65:8888")
    return jsonify({})
