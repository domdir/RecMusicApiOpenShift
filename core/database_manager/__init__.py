from flask_sqlalchemy import SQLAlchemy
import os

from core import mes_core

mes_core.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.getcwd()+'\db\MesProject_OpenShift_DB.db'
mes_core.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(mes_core)

from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_seen import TrailerSeen
from core.database_manager.questionnaire import Questionnaire
from core.database_manager.dem_questionnaire import DemQuestionnaire
from core.database_manager.personality import Personality
from core.database_manager.load_page import TimeLog

if not os.path.isfile(os.getcwd()+'\db\MesProject_OpenShift_DB.db'):
	db.drop_all()
	db.create_all()