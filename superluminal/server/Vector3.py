from math import sqrt, pow

class Vector3(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
    
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def magnitude_squared(self):
        return self.x**2 + self.y**2 + self.z**2
    
    def normalize(self):
        return self * (1.0 / self.magnitude())

    def __add__(self, other):
        if isinstance(other, Vector3):
            new = Vector3()
            new.x = self.x + other.x
            new.y = self.y + other.y
            new.z = self.z + other.z
            return new
        raise NotImplementedError()
    
    def __sub__(self, other):
        if isinstance(other, Vector3):
            new = Vector3()
            new.x = self.x - other.x
            new.y = self.y - other.y
            new.z = self.z - other.z
            return new
        raise NotImplementedError()
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            new = Vector3()
            new.x = self.x * other
            new.y = self.y * other
            new.z = self.z * other
            return new
        raise NotImplementedError()

    def __repr__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)
