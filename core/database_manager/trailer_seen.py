from core.database_manager import db

class TrailerSeen(db.Model):
    __tablename__ = 'trailer_seen'
    id = db.Column(db.Integer, primary_key=True)
    time_stamp=db.Column(db.String(50))
    seen_by = db.Column(db.String(50))
    imdb_id = db.Column(db.String(20))
    rate = db.Column(db.String(10))
    is_skipped = db.Column(db.String(10))
    reported = db.Column(db.String(10))
    time_watched= db.Column(db.String(20))
    predicted_rate=db.Column(db.String(20))
    type_of_rec = db.Column(db.String(10))

    def __init__(self, timestamp,seen_by, imdb_id, rate, is_skipped,reported,time_watched, predicted_rate,type_of_rec):
        self.time_stamp=timestamp
        self.seen_by = seen_by
        self.imdb_id = imdb_id
        self.rate = rate
        self.is_skipped = is_skipped
        self.reported = reported
        self.time_watched=time_watched
        self.predicted_rate=predicted_rate
        self.type_of_rec = type_of_rec

    def __repr__(self):
        return 'seen_by: {0} , imdb_id: {1}, rate: {2},' \
               ' is_skipped: {3}, type_of_rec: {4}'.format(self.seen_by, self.imdb_id,
                                                           self.rate, self.is_skipped, self.type_of_rec)
