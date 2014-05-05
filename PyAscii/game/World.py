import time
import sys
import copy
from Terrain import *
sys.path.pop()
sys.path.append("util")
from Vector import *
from Entity import Entity

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.terrain = [[Terrain.Grass]*size]*size 
        self.entities = [player]

    def input(self, char):
        pass

    def update(self):
        pass

    def render(self):
        #TODO: Combine list of entities with terrain using entity position.
        camera = copy.deepcopy(self.terrain) #COMPOSED OF PIXELS

<<<<<<< HEAD
world = World(size=12, Entity(Vector(1,1)), None)
=======
        for ent in self.entities:
            if(not ((ent.pos.x < 0 or ent.pos.x > size)
               or (ent.pos.y < 0 or ent.pos.y > size))):
                camera[int(ent.pos.x)][int(ent.pos.y)] = ent


        #TODO:  Render in HTML and return
        html = "TODO: PUT DAH HTML HERE"
        return html



world = World(100, None)



>>>>>>> 25e3c07acaf316364ba57a2d751d33cceedf98e2
