class Vector(object):
    def __init__(self, *components):
        self.components = components

    def magnitude(self):
        return sum(component**2 for component in self.components)**0.5
    
    def __add__(self, other):
        return Vector(*map(sum, zip(self.components, other.components)))

    def __mul__(self, scalar):
        return Vector(*[x*scalar for x in self.components])

    def __sub__(self, other):
        return self + other*-1

    def __rmul__(self, scalar):
        return self*scalar

    def __rdiv__(self, scalar):
        return self/scalar

    def dot(self, other):
        return sum(map(lambda tup: tup[0]*tup[1], zip(self.components, other.components)))

    def __str__(self):
        return str(self.components) + "|" + str(self.magnitude())
    
    @property
    def x(self):
        return self.components[0]



    @property
    def y(self):
        return self.components[1]



    @property
    def z(self):
        return self.components[2]
