from core.database_manager import db


class DemQuestionnaire(db.Model):
   
    __tablename__ = 'dem_questionnaire'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    dateOfBirth = db.Column(db.String(15))
    gender = db.Column(db.String(10))
    nationality = db.Column(db.String(60))
    question1_1 = db.Column(db.String(10))
    question1_2 = db.Column(db.String(10))
    question1_3 = db.Column(db.String(10))
    question1_4 = db.Column(db.String(10))
    question1_5 = db.Column(db.String(10))
    question1_6 = db.Column(db.String(50))
    question1_7 = db.Column(db.String(10))
    question1_8 = db.Column(db.String(10))
    question1_9 = db.Column(db.String(10))
    question1_10 = db.Column(db.String(10))
    question1_11 = db.Column(db.String(50))
    question_2 = db.Column(db.String(10))
    twitter = db.Column(db.String(20))
    fb = db.Column(db.String(20))
    instagram = db.Column(db.String(20))
    lastfm = db.Column(db.String(20))
    spotify = db.Column(db.String(20))
    

    def __init__(self, user_id,
                 dateOfBirth,
    gender,
    nationality,
    question1_1,
    question1_2,
    question1_3,
    question1_4,
    question1_5,
    question1_6,
    question1_7,
    question1_8,
    question1_9,
    question1_10,
    question1_11,
    question_2,
    twitter,
    fb,
    instagram,
    lastfm,
    spotify,
    ):

        self.user_id = user_id
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.nationality = nationality
        self.question1_1 = question1_1
        self.question1_2 = question1_2
        self.question1_3 = question1_3
        self.question1_4 = question1_4
        self.question1_5 = question1_5
        self.question1_6 = question1_6
        self.question1_7 = question1_7
        self.question1_8 = question1_8
        self.question1_9 = question1_9
        self.question1_10 = question1_10
        self.question1_11 = question1_11
        self.question_2 = question_2
        self.twitter = twitter
        self.fb = fb
        self.instagram = instagram
        self.lastfm = lastfm
        self.spotify = spotify

