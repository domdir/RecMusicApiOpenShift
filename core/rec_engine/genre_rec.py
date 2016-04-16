import random
def genre_rec(table_to_use):
    print "genre rec"
    movies_to_rec = {}
    tmp = []
    safe_iter = 0

    j = random.randrange(1, len(table_to_use.index))

    movie = table_to_use.iloc[j]
    movie["REC_TYPE"]="GENRE"
    movie = movie.to_json()
    return movie