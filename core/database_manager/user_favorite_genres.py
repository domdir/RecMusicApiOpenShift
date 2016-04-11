from core.database_manager import db


class UserFavoriteGenre(db.Model):
    __tablename__ = 'user_favorite_genre'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    genre_1 = db.Column(db.String(20))
    genre_2 = db.Column(db.String(20))
    genre_3 = db.Column(db.String(20))
    genre_4 = db.Column(db.String(20))

    def __init__(self, rated_by, genre1, genre2, genre3, genre4):
        self.user_id = rated_by
        self.genre_1 = genre1
        self.genre_2 = genre2
        self.genre_3 = genre3
        self.genre_4 = genre4

    def __repr__(self):
        return 'user_id: {0} , genre1: {1}, genre2: {2} genre3: {3}, genre4: {4}' \
            .format(self.user_id, self.genre_1, self.genre_2, self.genre_3,self.genre_4)
