from Vector3 import Vector3
from Vector4 import Vector4

class Body(object):
    def __init__(self):
        self.in_use = True # Used for object pooling
        self.mass = 0.0 # Kg
        self.position = Vector3()
        self.velocity = Vector3()
        self.rotation = Vector4()
        self.radius = 0.0
    
    def on_collide(self, engine, affecting_body):
        # If modifying velocity or other values, destroy this body and create a new one
        pass

    def on_tick(self, engine, seconds_passed):
        pass

    def __repr__(self) -> str:
        return "In Use: {}\nMass: {}\nRadius: {}\nPosition: {}\nVelocity: {}\nRotation: {}".format(self.in_use, self.mass, self.radius, self.position, self.velocity, self.rotation)
