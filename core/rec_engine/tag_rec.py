
def tag_rec(table_to_use):
    print "tag rec"
    movies_to_rec = {}
    tmp = []
    safe_iter = 0
    movie = table_to_use.iloc[1]
    movie["REC_TYPE"]="TAG"
    movie = movie.to_json()
    return movie
