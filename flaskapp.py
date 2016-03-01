from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from pymongo import MongoClient

import os

app = Flask(__name__)
api=Api(app)


class ResetServer(Resource):
    def get(self):
        client = MongoClient('localhost', 27017)
        return "test"

api.add_resource(ResetServer, '/')

if __name__ == '__main__':
    app.run(debug=True)