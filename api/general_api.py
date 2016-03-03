from flaskapp import api
import json
import os
from flask_restful import Resource
from pymongo import MongoClient

class Home(Resource):
    def get(self):
        return "home"

api.add_resource(Home, '/')

class ResetServer(Resource):
    def get(self):
        client = MongoClient("127.5.34.130", 27017)
        db = client.recmusicapiopenshift
        db.authenticate("admin","FeLZebfCiq_x")

        file_path = os.getcwd() + "/app-deployments/current/repo/data/songs.json"
        songsList = json.load(open(file_path))
        db.songs.remove()
        songs = db.songs
        songs.insert_many(songsList)

        #res=list(db.test.find({}))
        #db.rates.remove()
        #db.songs.remove()
        #songs = db.songs

        #songs.insert_many(songsList)
        #collections_names=db.collection_names()
        return "db_erased"
api.add_resource(ResetServer, '/reset')