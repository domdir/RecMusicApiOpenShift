from core.database_manager import db


class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    question_1 = db.Column(db.String(10))
    question_2 = db.Column(db.String(10))
    question_3 = db.Column(db.String(10))
    question_4 = db.Column(db.String(10))
    question_5 = db.Column(db.String(10))
    question_6 = db.Column(db.String(10))
    question_7 = db.Column(db.String(10))
    question_8 = db.Column(db.String(10))
    question_9 = db.Column(db.String(10))
    question_10 = db.Column(db.String(10))
    question_11 = db.Column(db.String(10))
    question_12 = db.Column(db.String(10))
    question_13 = db.Column(db.String(10))
    question_14 = db.Column(db.String(10))
    question_15 = db.Column(db.String(10))
    question_16 = db.Column(db.String(10))
    question_17 = db.Column(db.String(10))
    question_18 = db.Column(db.String(10))
    question_19 = db.Column(db.String(10))
    question_20 = db.Column(db.String(10))
    question_21 = db.Column(db.String(10))
    question_22 = db.Column(db.String(10))
    question_23 = db.Column(db.String(10))

    def __init__(self, rated_by,
                 question_1,
                 question_2,
                 question_3,
                 question_4,
                 question_5,
                 question_6,
                 question_7,
                 question_8,
                 question_9,
                 question_10,
                 question_11,
                 question_12,
                 question_13,
                 question_14,
                 question_15,
                 question_16,
                 question_17,
                 question_18,
                 question_19,
                 question_20,
                 question_21,
                 question_22,
                 question_23,):

        self.user_id = rated_by
        self.question_1 = question_1
        self.question_2 = question_2
        self.question_3 = question_3
        self.question_4 = question_4
        self.question_5 = question_5
        self.question_6 = question_6
        self.question_7 = question_7
        self.question_8 = question_8
        self.question_9 = question_9
        self.question_10 = question_10
        self.question_11 = question_11
        self.question_12 = question_12
        self.question_13 = question_13
        self.question_14 = question_14
        self.question_15 = question_15
        self.question_16 = question_16
        self.question_17 = question_17
        self.question_18 = question_18
        self.question_19 = question_19
        self.question_20 = question_20
        self.question_21 = question_21
        self.question_22 = question_22
        self.question_23 = question_23
