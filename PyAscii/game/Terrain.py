import sys
sys.path.pop()
sys.path.append("util")
from Pixel import *

class Terrain(object, Pixel):
    """The terrain class"""
    def __init__(self, body, color):
        super(Terrain, self).__init__(body, color)





