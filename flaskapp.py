from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

import os

app = Flask(__name__)
api=Api(app)

@app.route('/')
def hello_world():
    print "test"
    #client = MongoClient("mongodb://$OPENSHIFT_MONGODB_DB_HOST:OPENSHIFT_MONGODB_DB_PORT/")
    #db = client.recmusicapiopenshift

    return 'test World!'

if __name__ == '__main__':
    app.run()