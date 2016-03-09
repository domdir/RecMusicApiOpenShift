import logging

import sys

from flaskapp import api,db,app
import json
import os
from flask_restful import Resource

LOGFILE = "recmusic.log"

class Home(Resource):
    def get(self):
        return "home"
api.add_resource(Home, '/')

class ResetServer(Resource):
    def get(self):
        file_path = os.getcwd() + "/app-deployments/current/repo/data/songs.json"
        songsList = json.load(open(file_path))
        db.songs.remove()
        db.rates.remove()
        songs = db.songs
        songs.insert_many(songsList)
        logPath = os.path.join(os.environ["OPENSHIFT_LOG_DIR"],LOGFILE)
        logging.basicConfig(filename=logPath, level=logging.DEBUG)
        logging.debug('This message should go to the log file')


        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        app.logger.setLevel(logging.ERROR)
        return "db_erased_2"
api.add_resource(ResetServer, '/api/reset')


class Ping(Resource):
    def get(self):
        return "pong"
api.add_resource(Ping, '/api/ping')