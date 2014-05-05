import time
import sys
from Terrain import *
sys.path.pop()
sys.path.append("util")
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.terrain = [[Terrain(body="^", color=(0x33CC33, 0x663300))]*size for x in xrange(size)]

    def input(self, char):
        pass

    def update(self):
        pass

    def render(self):
        #TODO: Combine list of entities with terrain using entity position.


        #TODO:  Render in HTML and return
        html = "TODO: PUT DAH HTML HERE"
        return html



world = World(100, None)



