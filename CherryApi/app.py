import os
import cherrypy
from router import Router

if __name__ == '__main__':
    cherrypy.quickstart(Router(), '/', 'app.conf')