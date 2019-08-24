import random
from core import audio_ivec_sim
from core.database_manager import trailer_seen, personality
from core import get_table
from pandas import Series
import numpy
import operator
import math


def pers_rec(user_id,num_of_rec,num_of_skip,pers_type):
    movies_seen=trailer_seen.TrailerSeen.query.filter_by(seen_by=user_id)
    movies_to_exclude = []
    for r in movies_seen:
        movies_to_exclude.append(r.imdb_id)

    pers_user = personality.Personality.query.get(user_id).TIPI_TO_OCEAN()
    final_array = []

    if pers_type == "users":
        pers_others = personality.Personality.query.filter(personality.Personality.user_id != user_id)

        for pers_other in pers_others:
            d = get_distance(pers_user, pers_other.TIPI_TO_OCEAN())
            movies_seen=trailer_seen.TrailerSeen.query.filter_by(seen_by=pers_other.user_id, is_skipped=0)
            for r in movies_seen:
                # problem when multiple users rated the same movie, it should prob aggregate the score
                final_array.append((r.imdb_id, float((1/d) * r.rate), r.rate))
    else:
        # TODO use real data source
        pers_others = {}

        # for other_id, pers_other in pers_others:
        #     d = get_distance(pers_user, pers_other)
        #     movies_seen=trailer_seen.TrailerSeen.query.filter_by(seen_by=other_id, is_skipped=0)
        #     for r in movies_seen:
        #         # problem when multiple users rated the same movie, it should prob aggregate the score
        #         final_array.append((r.imdb_id, float((1/d) * r.rate), r.rate))

    dtype = [('IMDB_ID', 'S10'), ('PREDICTED_VOTE', float), ('IMDB_VOTES', int)]

    numpy_final = numpy.array(final_array, dtype=dtype)
    numpy_final = numpy.sort(numpy_final, order=['PREDICTED_VOTE'])
    numpy_final = numpy_final[::-1]

    all_table = get_table("all_table")()
    all_table = all_table[~all_table["IMDB_ID"].isin(Series(movies_to_exclude))]
    all_table.reset_index(drop=True, inplace=True)

    final = {}

    safe_iter = 0

    while (len(final) < num_of_rec) and (safe_iter < 20) and len(numpy_final) > (safe_iter + num_of_skip):
        rec = numpy_final[safe_iter + num_of_skip]

        movie = all_table[all_table["IMDB_ID"] == rec[0]].copy()
        if len(movie.index):
            movie.reset_index(drop=True, inplace=True)
            movie = movie.iloc[0]
            movie["REC_TYPE"] = "PERS"
            movie["PREDICTED_VOTE"]=rec[1]

            z = movie.to_json()
            safe_iter += 1
            final.update({len(final): z})
        else:
            safe_iter += 1

    return final

def get_distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3])**2 + (a[4]-b[4])**2)
