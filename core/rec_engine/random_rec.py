import random
from core import get_table


def random_rec(table_to_use, num_of_rec):
    print "random rec"
    movies_to_rec = {}
    tmp = []
    safe_iter = 0

    while (len(movies_to_rec) <= num_of_rec) and (safe_iter < 20):
        j = random.randrange(1, len(table_to_use.index))
        safe_iter += 1
        if j not in tmp:
            movie = table_to_use.iloc[j]
            movie = movie.to_json()
            movies_to_rec.update({len(movies_to_rec): movie})
            tmp.append(j)
    return movies_to_rec
