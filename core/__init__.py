print "1"
from flask import Flask
import pandas as pd
import logging

import os

LOGFILE = "recmusic.log"

logPath = os.path.join(os.environ["OPENSHIFT_LOG_DIR"], LOGFILE)
logging.basicConfig(filename=logPath, level=logging.DEBUG)
logging.debug('test new app')

print "2"
mes_core = Flask(__name__)
mes_core.config['PROPAGATE_EXCEPTIONS'] = True


path = os.getcwd()+ "/app-root/repo/csv/movies_info.csv"
print path

movie_table = pd.read_csv(path, ",")
movie_table = movie_table.drop("Unnamed: 0", 1)

print "3"

import routes
import database_manager
