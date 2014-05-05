import webapp2
import time
from Vector import *
from Entity import Entity

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

world = World(size=12, Entity(Vector(1,1)), None)
