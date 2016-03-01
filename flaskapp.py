from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

import os

app = Flask(__name__)
api=Api(app)

@app.route('/')
def hello_world():

    client = MongoClient('localhost', 27017)
    return 'test World!'

if __name__ == '__main__':
    app.run()