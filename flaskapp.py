from flask import Flask
from flask_restful import Api
import pymongo
import os

app = Flask(__name__)
api=Api(app)

@app.route('/')
def hello_world():
    mongo_con = pymongo.Connection(os.environ['OPENSHIFT_MONGODB_DB_HOST'],
                               int(os.environ['OPENSHIFT_MONGODB_DB_PORT']))
    db = mongo_con[os.environ['OPENSHIFT_APP_NAME']]
    return 'test World!'

if __name__ == '__main__':
    app.run()