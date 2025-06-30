import cherrypy
import json
from db import get_collection
from bson.json_util import dumps

class SensorAPI:
    @cherrypy.expose
    def get_all(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        collection = get_collection()
        data = collection.find().sort("timestamp", -1).limit(10)  # last 10
        return dumps(data)  # Handles ObjectId and datetime
