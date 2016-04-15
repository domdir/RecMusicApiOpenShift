
def feature_rec(table_to_use):
    print "genre rec"
    movies_to_rec = {}
    tmp = []
    safe_iter = 0
    movie = table_to_use.iloc[3]
    movie["REC_TYPE"]="GENRE"
    movie = movie.to_json()
    return movie