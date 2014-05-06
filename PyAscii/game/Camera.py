import sys
sys.path.pop()
sys.path.append("util")
from Vector import *
sys.path.pop()
sys.path.append("game")

class Camera(object):
    """Camera is the dimensions and location of the view window"""

    def __init__(self, position, dimension)
        self.position = position
        self.dimension = dimension

    def view(self, entity)
        self.position = entity.pos
    
    def follow(self, entity)
        self.isFollowing = true
        self.followedEntity = entity

    def update(self, world)
        if (self.isFollowing):
            self.view(self.followedEntity)

    def render(self, pixelArray, world)
        for ent in world.entities:
            if(not ((ent.pos.x < self.position.x - self.dimension.x or ent.pos.x > self.position.x + self.dimension.x)
               or (ent.pos.y < self.position.y - self.dimension.y or self.position.y + self.dimension.y))):
                pixelArray[int(ent.pos.x - self.position.x + self.dimension.x)][int(ent.pos.y - self.position.y + self.dimension.y)] = ent

        if (len(pixelArray) <= self.dimension.x and len(pixelArray[0]) <= self.dimension.y):
            return pixelArray

            #TODO: Enable camera size and make a camera object
            #This would return self.camera.render(buffer)
            #camera would then take the buffer and snip the size.

        

isFollowing = false
