from Vector3 import Vector3
from Vector4 import Vector4
from speed_of_light import SPEED_OF_LIGHT

class Body(object):
    PHOTON_RADIUS = 0.000000000001

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

    def set_photon_velocity_by_direction(self, direction):
        self.velocity = direction.normalize() * SPEED_OF_LIGHT
    
    def set_photon_mass_by_electromagnetic_frequency(self, frequency_in_hertz):
        electron_volts = frequency_in_hertz * 4.1356655385381 * 10**-15
        energy = electron_volts * 1.602177 * 10**-19
        self.mass = energy / SPEED_OF_LIGHT**2
