from flask_sqlalchemy import SQLAlchemy
import os

from core import mes_core

mes_core.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.environ["OPENSHIFT_DATA_DIR"]+'/db/MesProject_OpenShift_DB.db'
mes_core.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(mes_core)

print "sql create"
from core.database_manager.user_favorite_genres import UserFavoriteGenre
from core.database_manager.trailer_rates import TrailerRate

db.drop_all()
db.create_all()
