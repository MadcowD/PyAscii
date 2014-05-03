import Vector

class Rectangle(object):
    """The rectangle class"""

    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __init__(self, v1,v2):
        self.__init__(v1.components[0], v1.components[1],
            v2.components[0], v2.components[1])


    def __init__(self, width, height):
        self.__init__(0,0,width, height)

    def area(self):
        return self.width*self.height
    
    def position(self):
        return Vector(x,y)

    def bounds(self):
        return Vector(width,height)