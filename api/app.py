from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from pymongo import MongoClient

import os

app = Flask(__name__)
api=Api(app)
client = MongoClient('localhost', 27017)
db = client.recmusicapiopenshift


class ResetServer(Resource):
    def get(self):
        collections_names=db.collection_names()
        print collections_names
        return "test"

api.add_resource(ResetServer, '/')

from api import routes