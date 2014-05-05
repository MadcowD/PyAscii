import webapp2
import time

class World(object):
    """The world class which stores entities and value data."""



    def render(self):
        return "TODO: PUT THE SPAN GIRD HERE"



world = World()

class WorldHandler(webapp2.RequestHandler):
    def get(self):
        global world
        self.response.write("hi I am the world for this game I guess")
        self.response.write("<br/>here is world: " + world.render())

