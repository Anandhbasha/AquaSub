import os
import cherrypy
from api import SensorAPI

current_dir = os.path.dirname(os.path.abspath(__file__))

conf = {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': current_dir,
        'tools.staticdir.index': 'index.html'
    }
}

api_conf = {
    '/': {
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'application/json')]
    }
}

if __name__ == '__main__':
    cherrypy.tree.mount(None, '/', conf)  # For serving index.html
    cherrypy.tree.mount(SensorAPI(), '/api', api_conf)
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
