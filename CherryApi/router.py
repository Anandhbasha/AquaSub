import cherrypy
from controller import MyController

class Router:
    def __init__(self): 
        self.ctrl = MyController()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def create(self, item_id=None, value=None):
        return self.ctrl.create_item(item_id, value)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def read(self, item_id=None):
        return self.ctrl.read_item(item_id)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def update(self, item_id=None, value=None):
        return self.ctrl.update_item(item_id, value)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete(self, item_id=None):
        return self.ctrl.delete_item(item_id)
