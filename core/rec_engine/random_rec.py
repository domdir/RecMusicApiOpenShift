import random
from core import get_table


def random_rec(table_to_use):
    print "random rec"
    movies_to_rec = {}
    tmp = []
    safe_iter = 0

    while (len(movies_to_rec) < 1) and (safe_iter < 20):
        j = random.randrange(1, len(table_to_use.index))
        safe_iter += 1
        if j not in tmp:
            movie = table_to_use.iloc[j]
            movie["REC_TYPE"]="RANDOM"
            movie = movie.to_json()
    return movie
