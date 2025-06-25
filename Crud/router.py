import cherrypy
from controller import user_controller
import json

class Router:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_users(self):
        return json.loads(user_controller.get_all_users())

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add_user(self):
        input_data = cherrypy.request.json
        return json.loads(user_controller.add_user(input_data))

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_user(self, user_id):
        input_data = cherrypy.request.json
        return json.loads(user_controller.update_user(user_id, input_data))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete_user(self, user_id):
        return json.loads(user_controller.delete_user(user_id))

