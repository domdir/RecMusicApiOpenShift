
from core.database_manager import db

class TrailerRate(db.Model):
    __tablename__ = 'trailer_rates'
    id = db.Column(db.Integer, primary_key=True)
    rated_by = db.Column(db.String(50))
    movie_id = db.Column(db.String(20))
    rate = db.Column(db.String(10))

    def __init__(self, rated_by,imdb_id,rate):
        self.rated_by = rated_by
        self.movie_id = imdb_id
        self.rate=rate

    def get_imdb_id(self):
        return self.movie_id

    def __repr__(self):
        return 'rated_by: {0} , imdb_id: {1}, rate: {2}'.format(self.rated_by,self.movie_id,self.rate)