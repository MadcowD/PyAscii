import sys
sys.path.pop()
sys.path.append("util")
from Pixel import *

class Entity(Pixel):
    """The basic entity class"""
    def __init__(self, position=None, body="", color=None):
        self.position = position
        super(Entity, self).__init__(body, color)

    def update(self, world):
        """Updates the entity based on the world around it"""

        pass
