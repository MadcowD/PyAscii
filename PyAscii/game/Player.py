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
                self.pos -= Vector(0,1)
            if input == "DOWN":
                self.pos += Vector(0,1)
            if input == "LEFT":
                self.pos -= Vector(1,0)
            if input == "RIGHT":
                self.pos += Vector(1,0)
        pass

    def update(self, world):
        pass




