import logging

import sys

from flaskapp import api,db,app
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
        db.songs.remove()
        db.rates.remove()
        songs = db.songs
        songs.insert_many(songsList)

        #logger=logging.getLogger(__name__)
        logging.basicConfig()
        logging.debug('This message should go to the log file')
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
        app.logger.setLevel(logging.ERROR)

        return "db_erased"
api.add_resource(ResetServer, '/reset')