from core import mes_core, get_table
from flask import request, jsonify
from core.rec_engine import random_rec, rec_types

rec_router = {
    0: random_rec,
}


@mes_core.route('/get_rec', methods=["GET"])
def get_rec():
    print "get_rec"
    # time.sleep(5)
    num_of_rec = request.args.get('num_of_rec')
    for_who = request.args.get('for_who')
    type = request.args.get('type')

    if not for_who:
        return jsonify({})

    if not num_of_rec:
        num_of_rec = 1
    else:
        num_of_rec = int(num_of_rec)

    if not type:
        type = "RANDOM"

    print num_of_rec
    print for_who
    print type

    rec_type = rec_types.get(type, "RANDOM")
    print rec_type
    table_to_use=get_table('all_table')

    t=rec_router.get(rec_type)(table_to_use,5)

    return jsonify({})
