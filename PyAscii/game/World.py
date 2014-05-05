import webapp2
import time
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.terrain = [[Terrain(body="^", color=(0x33CC33, 0x663300))]*n for x in xrange(n)]

    def input(self, char):
        pass

    def update(self):
        pass

    def render(self):
        return "TODO: PUT THE SPAN GIRD HERE"



world = World(Vector(100,100), None)



