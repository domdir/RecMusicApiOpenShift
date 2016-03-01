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
        file_path = os.getcwd() + "/app-deployments/current/repo/data/songs.json"
        songsList = json.load(open(file_path))
        db = client.recmusicapiopenshift
        #db.rates.remove()
        #db.songs.remove()
        songs = db.songs
        songs.insert_many(songsList)
        #collections_names=db.collection_names()
        return songsList
api.add_resource(ResetServer, '/reset')