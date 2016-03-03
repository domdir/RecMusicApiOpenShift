from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from pymongo import MongoClient

app = Flask(__name__)
api=Api(app)

from api import general_api

