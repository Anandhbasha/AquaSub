import os
import cherrypy
from router import Router

current_dir = os.path.dirname(os.path.abspath(__file__))

config = {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(current_dir, ''),
        'tools.staticdir.index': 'index.html',
    }
}

if __name__ == '__main__':
    cherrypy.tree.mount(Router(), '/', config)
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
