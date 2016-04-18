import random
from core import feature_sim
from core.database_manager import trailer_seen
from core import get_table
import numpy

def feature_rec(table_to_use, user_id):
    print "feature rec"

    final_array = []
    rated_by_user = trailer_seen.TrailerSeen.query.filter_by(seen_by=user_id,is_skipped=0)

    rated_imdb={}
    for r in rated_by_user:
        rated_imdb.update({r.imdb_id:r.rate})

    final_array = []
    i = 0
    for row in feature_sim.itertuples():
        num = 0
        den = 0
        i += 1
        print i
        # d={}
        values = []
        neigh_splitted = row[3].split(",")
        # print neigh_splitted
        for j in neigh_splitted:
            # print "inside first"
            imdb_sim = j.split(":")
            imdb = imdb_sim[0]
            # print imdb
            if rated_imdb.get(imdb, None):
                #   print "inside second"
                num += rated_imdb.get(imdb) * float(imdb_sim[1])
                den += float(imdb_sim[1])
        if den == 0:
            final_v = 0
        else:
            final_v = num / den

        final_array.append((row[1], final_v, row[2]))

    dtype = [('IMDB_ID', 'S10'), ('PREDICTED_VOTE', float), ('IMDB_VOTES', int)]

    numpy_final = numpy.array(final_array, dtype=dtype)
    numpy_final = numpy.sort(numpy_final, order=['PREDICTED_VOTE', "IMDB_VOTES"])
    numpy_final = numpy_final[::-1]

    rec_imdb=[]
    for rec in numpy_final:
        rec_imdb.append(rec[0])
    all_table=get_table("all_table")()

    res=all_table[all_table["IMDB_ID"].isin(rec_imdb)]
    final={}
    for r in res:
        z=r.to_json()
        final.update({len(final):z})
    return final
