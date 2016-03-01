from flaskapp import api,client
import json
import os
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return "home"

api.add_resource(Home, '/')

class ResetServer(Resource):
    def get(self):
        file_path = os.getcwd() + "/data/songs.json"
        songsList = json.load(open(file_path))
        db = client.rec_music_core_db
        db.rates.remove()
        db.songs.remove()
        songs = db.songs
        songs.insert_many(songsList)
        collections_names=db.collection_names()
        return "db created"
api.add_resource(ResetServer, '/reset')