from core.database_manager import db


class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    list1 = db.Column(db.String(10))
    list2 = db.Column(db.String(10))
    list3 = db.Column(db.String(10))
    timestamp1= db.Column(db.String(20))
    timestamp2= db.Column(db.String(20))
    timestamp3= db.Column(db.String(20))
    timestamp4= db.Column(db.String(20))
    timestamp5= db.Column(db.String(20))
    timestamp6= db.Column(db.String(20))
    timestamp7= db.Column(db.String(20))
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
    question_24 = db.Column(db.String(10))
    question_25 = db.Column(db.String(10))
    question_26 = db.Column(db.String(10))
    question_27 = db.Column(db.String(10))
    question_28 = db.Column(db.String(10))

    def __init__(self, rated_by,
                 list1,
                 list2,
                 list3,
                 timestamp1,
                 timestamp2,
                 timestamp3,
                 timestamp4,
                 timestamp5,
                 timestamp6,
                 timestamp7,
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
                 question_23,
                 question_24,
                 question_25,
                 question_26,
                 question_27,
                 question_28,):

        self.user_id = rated_by
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.timestamp1=timestamp1
        self.timestamp2=timestamp2
        self.timestamp3=timestamp3
        self.timestamp4=timestamp4
        self.timestamp5=timestamp5
        self.timestamp6=timestamp6
        self.timestamp7=timestamp7
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
        self.question_24 = question_24
        self.question_25 = question_25
        self.question_26 = question_26
        self.question_27 = question_27
        self.question_28 = question_28
