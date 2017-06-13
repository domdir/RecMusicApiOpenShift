'''
Created on 13 mag 2017

@author: Antonio
'''
from core.database_manager import db

class TimeLog(db.Model):
    __tablename__ = 'timelog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    SignUpPage = db.Column(db.String(10))
    SignInPage = db.Column(db.String(10))
    DemographicPage = db.Column(db.String(10))
    PersonalityPage = db.Column(db.String(10))
    PreCatalogPage = db.Column(db.String(10))
    Ini0Page = db.Column(db.String(10))
    Ini1Page = db.Column(db.String(10))
    Ini2Page = db.Column(db.String(10))
    Ini3Page = db.Column(db.String(10))
    Ini4Page = db.Column(db.String(10))
    Ini5Page = db.Column(db.String(10))
    ProfilePage = db.Column(db.String(10))
    ExplorePage = db.Column(db.String(10))
    RecForYouPage = db.Column(db.String(10))
    
    

    def __init__(self, rated_by,
                  SignUpPage,
                  SignInPage,
                  DemographicPage,
                  PersonalityPage,
                  PreCatalogPage,
                  Ini0Page,
                  Ini1Page,
                  Ini2Page,
                  Ini3Page,
                  Ini4Page,
                  Ini5Page,
                  ProfilePage,
                  ExplorePage,
                  RecForYouPage
                ):

        self.user_id = rated_by
        self.SignUpPage=SignUpPage
        self.SignInPage=SignInPage
        self.DemographicPage=DemographicPage
        self.PersonalityPage=PersonalityPage
        self.PreCatalogPage=PreCatalogPage
        self.Ini0Page=Ini0Page
        self.Ini1Page=Ini1Page
        self.Ini2Page=Ini2Page
        self.Ini3Page=Ini3Page
        self.Ini4Page=Ini4Page
        self.Ini5Page=Ini5Page
        self.ProfilePage=ProfilePage
        self.ExplorePage=ExplorePage
        self.RecForYouPage=RecForYouPage
        