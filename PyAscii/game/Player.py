from Entity import Entity
import sys
sys.path.pop()
sys.path.append("util")
from Vector import Vector

class Player(Entity):
    """The basic player class"""
    def __init__(self, *args): 
        #TODO: ADD ARGUMENTS APPROPRIATE TO THE PLAYER CLASS :#
        super(Player, self).__init__(pos = Vector(0,0), body="@", color=(0xFF0000, 0x000000))


    def handleInput(self, world, input):
        if input is not None:
            if input == "UP":
                if self.pos.y > 0:
                    self.pos -= Vector(0,1)
            if input == "DOWN":
                if self.pos.y < world.size:
                    self.pos += Vector(0,1)
            if input == "LEFT":
                if self.pos.x > 0:
                    self.pos -= Vector(1,0)
            if input == "RIGHT":
                if self.pos.x < world.size:
                    self.pos += Vector(1,0)
        pass

    def update(self, world):
        pass




