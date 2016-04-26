from core import mes_core
from flask import request, jsonify
from flask import send_file


@mes_core.route('/get_img', methods=['GET'])
def get_img():
    imdb_id = request.args.get('imdb_id')
    return send_file("/app-root/repo/images/"+"tt0115907.jpg")