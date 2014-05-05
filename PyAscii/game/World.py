import webapp2
import time
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        

    def input(self, char):
        pass

    def update(self):
        pass

    def render(self):
        return "TODO: PUT THE SPAN GIRD HERE"



world = World()



