from __future__ import annotations
from time import time

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Engine import Engine

from .Body import Body
from .Vector3 import Vector3
from .speed_of_light import SPEED_OF_LIGHT
from .Ship import Ship

class Photon(Body):
    def __init__(self, initial_direction: Vector3, frequency_in_hertz: float):
        super().__init__()
        self.radius = 0.000000000001
        self.set_velocity_by_direction(initial_direction)
        self.set_mass_by_electromagnetic_frequency(frequency_in_hertz)
        # TODO Make sure location gets updated
        self.emission_location = Vector3()
        # TODO Replace with game clock time
        self.emission_time = time()
    
    def set_velocity_by_direction(self, direction: Vector3):
        self.velocity = direction.normalize() * SPEED_OF_LIGHT
    
    def set_mass_by_electromagnetic_frequency(self, frequency_in_hertz: float):
        electron_volts = frequency_in_hertz * 4.1356655385381 * 10**-15
        energy = electron_volts * 1.602177 * 10**-19
        self.mass = energy / SPEED_OF_LIGHT**2

    def on_collide(self, engine: Engine, affecting_body: 'Body'):
        if isinstance(affecting_body, Ship):
            engine.destroy_body(self)
