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
        print(size.x)
        self.terrain = [[Terrain.Grass for y in range(size.y)] for x in range(size.xd)] 
        print(len(self.terrain))
        self.entities = [player]

    def input(self, input):
        #this takes in the input from self.request.get('input')
        self.player.input(input)

        pass

    def update(self):
        pass

    def render(self):
        #TODO: Combine list of entities with terrain using entity position.
        camera = copy.deepcopy(self.terrain) #COMPOSED OF PIXELS

        for ent in self.entities:
            if(not ((ent.pos.x < 0 or ent.pos.x > self.size.x)
               or (ent.pos.y < 0 or ent.pos.y > self.size.y))):
                camera[int(ent.pos.x)][int(ent.pos.y)] = ent


        #TODO:  Render in HTML and return
        html = ""

        for y in range(self.size.y):
            for x in range(self.size.x):
                html += camera[x][y].body

            html+= "\n"

        return html



world = World(Vector(79,23), Entity(pos = Vector(0,0), body="@", color=None))
