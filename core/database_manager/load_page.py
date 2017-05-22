'''
Created on 13 mag 2017

@author: Antonio
'''
from core.database_manager import db

class TimeLog(db.Model):
    __tablename__ = 'timelog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    PresentationPage = db.Column(db.String(10))
    SignUpPage = db.Column(db.String(10))
    SignInPage = db.Column(db.String(10))
    DemographicPage = db.Column(db.String(10))
    PersonalityPage = db.Column(db.String(10))
    PreCatalogPage = db.Column(db.String(10))
    Ini0Page= db.Column(db.String(10))
    Ini1Page = db.Column(db.String(10))
    Ini2Page = db.Column(db.String(10))
    PreWebcamPage = db.Column(db.String(10))
    WebcamPage = db.Column(db.String(10))
    Ini3Page = db.Column(db.String(10))
    Ini4Page = db.Column(db.String(10))
    Ini5Page = db.Column(db.String(10))
    ProfilePage=db.Column(db.String(10))
    ExplorePage=db.Column(db.String(10))
    RecForYouPage=db.Column(db.String(10))
    
    

    def __init__(self, rated_by,
                  PresentationPage,
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
                  PreWebcamPage,
                  WebcamPage,
                  ProfilePage,
                  ExplorePage,
                  RecForYouPage
                ):

        self.user_id = rated_by
        self.PresentationPage=PresentationPage
        self.SignUpPage=SignUpPage
        self.SignInPage=SignInPage
        self.DemographicPage=DemographicPage
        self.PersonalityPage=PersonalityPage
        self.PreCatalogPage=PreCatalogPage
        self.Ini0Page=self.Ini0Page
        self.Ini1Page=self.Ini1Page
        self.Ini2Pgea=self.Ini2Pgea
        self.Ini3Page=self.Ini3Page
        self.Ini4Page=self.Ini4Page
        self.Ini5Page=self.Ini5Page
        self.PreWebcamPage=self.PreWebcamPage
        self.WebcamPage=self.WebcamPage
        self.ProfilePage=self.ProfilePage
        self.ExplorePage=self.ExplorePage
        self.RecForYouPage=self.RecForYouPage
        