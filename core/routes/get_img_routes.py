from core import mes_core
from flask import request, jsonify
from flask import send_file
import os


@mes_core.route('/get_img', methods=['GET'])
def get_img():
    imdb_id = request.args.get('imdb_id')
    print imdb_id
    print os.getcwd() + "/images/" + imdb_id + '.jpg'
    return send_file(os.getcwd() + "/images/" + imdb_id + '.jpg')
