import sys
sys.path.pop()
sys.path.append("util")
from Pixel import *
sys.path.pop()
sys.path.append("game")

class Entity(Pixel):
    """The basic entity class"""
    def __init__(self, pos=None, body="", color=None):
        self.pos = pos
        super(Entity, self).__init__(body, color)

    def update(self, world):
        """Updates the entity based on the world around it"""

        pass
