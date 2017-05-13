from core.database_manager import db


class Personality(db.Model):
    __tablename__ = 'personality'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    Extr_Enth = db.Column(db.String(10))
    Crit_Quar = db.Column(db.String(10))
    Depe_SeDi = db.Column(db.String(10))
    Anxi_EaUp = db.Column(db.String(10))
    OTNE_Comp = db.Column(db.String(10))
    Rese_Quie = db.Column(db.String(10))
    Symp_Warm = db.Column(db.String(10))
    Diso_Care = db.Column(db.String(10))
    Calm_EmSt = db.Column(db.String(10))
    Conv_Uncr = db.Column(db.String(10))

    def __init__(self, rated_by,
                 Extr_Enth,
                 Crit_Quar,
                 Depe_SeDi,
                 Anxi_EaUp,
                 OTNE_Comp,
                 Rese_Quie,
                 Symp_Warm,
                 Diso_Care,
                 Calm_EmSt,
                 Conv_Uncr,
                ):

        self.user_id = rated_by
        self.Extr_Enth = Extr_Enth
        self.Crit_Quar = Crit_Quar
        self.Depe_SeDi = Depe_SeDi
        self.Anxi_EaUp = Anxi_EaUp
        self.OTNE_Comp = OTNE_Comp
        self.Rese_Quie = Rese_Quie
        self.Symp_Warm = Symp_Warm
        self.Diso_Care = Diso_Care
        self.Calm_EmSt = Calm_EmSt
        self.Conv_Uncr = Conv_Uncr
        