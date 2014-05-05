import time
import sys
import copy
from Terrain import *
from Entity import *
from Player import *

sys.path.pop()
sys.path.append("util")
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.terrain\
            = [[Terrain.Grass for y in range(size.y)] for x in range(size.x)] 
        self.entities = [player]

    def input(self, input):
        #this takes in the input from self.request.get('input')
        self.player.handleInput(self, input)

        pass

    def update(self):
        for ent in self.entities:
            ent.update(self)

        pass

    def render(self):
        camera = copy.deepcopy(self.terrain) #COMPOSED OF PIXELS

        for ent in self.entities:
            if(not ((ent.pos.x < 0 or ent.pos.x > self.size.x)
               or (ent.pos.y < 0 or ent.pos.y > self.size.y))):
                camera[int(ent.pos.x)][int(ent.pos.y)] = ent

            #TODO: Enable camera size and make a camera object
            #This would return self.camera.render(buffer)
            #camera would then take the buffer and snip the size.

        return camera



world = World(Vector(79,23), Player())
