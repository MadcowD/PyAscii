import time
import sys
import copy
from Terrain import *
from Entity import *
from Player import *
from Camera import *

sys.path.pop()
sys.path.append("util")
from Vector import *

class World(object):
    """The world class which stores entities and value data."""

    def __init__(self, size, player, viewport):
        self.size = size
        self.center = size*.5
        self.player = player
        self.terrain\
            = [[Terrain.Grass if y%2 is 0 else Pixel.Black for y in range(size.y)] for x in range(size.x)] 
        self.entities = [player]
        self.camera = Camera(self.player.pos, viewport, self.center)


    def input(self, input):
        #this takes in the input from self.request.get('input')
        self.player.handleInput(self, input)

        pass

    def update(self):
        for ent in self.entities:
            ent.update(self)

        pass

    def render(self):
        buffer = copy.deepcopy(self.terrain) #COMPOSED OF PIXELS

        #PLACE ENTITIES
        for ent in world.entities:
            pos = self.buffercoord(ent.pos)
            if(not ((pos.x < 0 or pos.x > self.size.x)
               or (pos.y < 0 or pos.y > self.size.y))):
                buffer[pos.x][pos.y] = ent
        
        return self.camera.render(buffer, self)

    def buffercoord(self, vect):
        floatVect = vect + self.size*.5
        return Vector(int(floatVect.x), int(floatVect.y))

    def worldcoord(self, vect):
        return vect - self.size*.5


world = World(Vector(200,200), Player(), Vector(56,18))