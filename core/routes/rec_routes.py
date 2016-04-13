from core import mes_core, get_table
from flask import request, jsonify
from core.rec_engine import random_rec, rec_types

rec_router = {
    0: random_rec.random_rec,
}


@mes_core.route('/get_rec', methods=["GET"])
def get_rec():
    print "get_rec"
    rec_request_list = request.args.get('rec_request_list')
    for_who = request.args.get('for_who')

    if not for_who:
        return jsonify({})

    print rec_request_list

    try:
        rec_request_list = rec_request_list.split(",")
    except:
        return jsonify({})

    print rec_request_list
    resp = {}

    for req in rec_request_list:
        print req
        rec_type = rec_types.get(req, "RANDOM")
        print rec_type
        table_to_use = get_table('all_table')()
        t = rec_router.get(rec_type)(table_to_use, 1)
        resp.update(t)

    return jsonify(resp)
