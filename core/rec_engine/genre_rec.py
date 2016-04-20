from core import genre_sim
from core.database_manager import trailer_seen
from core import get_table
from pandas import Series
import numpy


def genre_rec(user_id, num_of_rec):

    rated_by_user = trailer_seen.TrailerSeen.query.filter_by(seen_by=user_id, is_skipped=0)

    rated_imdb = {}
    movies_to_exclude = []
    for r in rated_by_user:
        rated_imdb.update({r.imdb_id: r.rate})
        movies_to_exclude.append(r.imdb_id)

    final_array = []
    i = 0
    for row in genre_sim.itertuples():
        num = float(0)
        den = float(0)
        i += 1
        neigh_splitted = row[3].split(",")
        for j in neigh_splitted:
            imdb_sim = j.split(":")
            imdb = imdb_sim[0]
            if rated_imdb.get(imdb, None):
                num += float(rated_imdb.get(imdb)) * float(imdb_sim[1])
                den += float(imdb_sim[1])
        try:
            final_v = float(num / den)
        except:
            final_v = float(0)

        if not final_v:
            final_v=float(0)

        final_array.append((row[1], final_v, row[2]))

    dtype = [('IMDB_ID', 'S10'), ('PREDICTED_VOTE', float), ('IMDB_VOTES', int)]

    numpy_final = numpy.array(final_array, dtype=dtype)
    numpy_final = numpy.sort(numpy_final, order=['PREDICTED_VOTE', "IMDB_VOTES"])
    numpy_final = numpy_final[::-1]

    all_table = get_table("all_table")()
    all_table = all_table[~all_table["IMDB_ID"].isin(Series(movies_to_exclude))]
    all_table.reset_index(drop=True, inplace=True)

    all_table.head()
    final = {}

    safe_iter = 0

    while (len(final) < num_of_rec) and (safe_iter < 20):
        rec = numpy_final[safe_iter]

        movie = all_table[all_table["IMDB_ID"] == rec[0]].copy()
        if len(movie.index):

            movie.reset_index(drop=True, inplace=True)
            movie = movie.iloc[0]
            movie["REC_TYPE"] = "GENRE"
            movie["PREDICTED_VOTE"]=rec[1]
            z = movie.to_json()
            safe_iter += 1
            final.update({len(final): z})
        else:
            safe_iter+=1

    return final
