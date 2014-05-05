import time
import sys
import copy
from Terrain import *
from Entity import *

sys.path.pop()
sys.path.append("util")
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.terrain = [[Terrain.Grass]*size]*size 
        self.entities = [player]

    def input(self, input):
        #this takes in the input from self.request.get('input')
        pass

    def update(self):
        pass

    def render(self):
        #TODO: Combine list of entities with terrain using entity position.
        camera = copy.deepcopy(self.terrain) #COMPOSED OF PIXELS

        for ent in self.entities:
            if(not ((ent.pos.x < 0 or ent.pos.x > self.size)
               or (ent.pos.y < 0 or ent.pos.y > self.size))):
                camera[int(ent.pos.x)][int(ent.pos.y)] = ent


        #TODO:  Render in HTML and return
        html = "TODO: PUT DAH HTML HERE"
        return html



world = World(100, Entity(pos = Vector(0,0), body="@", color=None))
