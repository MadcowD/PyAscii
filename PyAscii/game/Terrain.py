import sys
sys.path.pop()
sys.path.append("util")
from Pixel import *

class Terrain(Pixel):
    """The terrain class"""
    def __init__(self, body, color):
        super(Terrain, self).__init__(body, color)

Terrain.Grass = Terrain(body="^", color=(0x33CC33, 0x663300))




