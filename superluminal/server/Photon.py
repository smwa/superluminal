from Body import Body
from Vector3 import Vector3
from speed_of_light import SPEED_OF_LIGHT

class Photon(Body):
    def __init__(self, initial_direction: Vector3, frequency_in_hertz: float):
        super().__init__()
        self.radius = 0.000000000001
        self.set_velocity_by_direction(initial_direction)
        self.set_mass_by_electromagnetic_frequency(frequency_in_hertz)
    
    def set_velocity_by_direction(self, direction: Vector3):
        self.velocity = direction.normalize() * SPEED_OF_LIGHT
    
    def set_mass_by_electromagnetic_frequency(self, frequency_in_hertz: float):
        electron_volts = frequency_in_hertz * 4.1356655385381 * 10**-15
        energy = electron_volts * 1.602177 * 10**-19
        self.mass = energy / SPEED_OF_LIGHT**2
