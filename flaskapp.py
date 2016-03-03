from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from pymongo import MongoClient

app = Flask(__name__)
api=Api(app)
client = MongoClient("127.5.34.130", 27017)
db = client.recmusicapiopenshift
db.authenticate("admin","FeLZebfCiq_x")

from api import general_api

