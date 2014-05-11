import sys
import numpy as np
sys.path.pop()
sys.path.append("util")
from Vector import *
from Pixel import *
sys.path.pop()
sys.path.append("game")

class Camera(object):
    """Camera is the dimensions and location of the view window"""

    def __init__(self, position, dimension, center):
        self.pos = position
        self.dimension = dimension
        self.center = center

    def view(self, entity):
        self.pos = entity.pos
    
    def follow(self, entity):
        self.isFollowing = true
        self.followedEntity = entity

    def update(self, world):
        if (self.isFollowing):
            self.view(self.followedEntity)

    def render(self, buffer, world):
        bufferVerts = (world.buffercoord(self.vertices[0]),world.buffercoord(self.vertices[1]))

        projection = np.array(buffer)[bufferVerts[0].x:bufferVerts[1].x,
                                      bufferVerts[0].y:bufferVerts[1].y].tolist()

        return projection

    @property
    def vertices(self):
        """Returns the vertex range (the rough dimensions of the camera relative to its center)"""
        return ((self.pos - self.dimension*.5),
                      (self.pos + self.dimension*.5 ))