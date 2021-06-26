from __future__ import annotations
import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Engine import Engine

from .Vector3 import Vector3
from .Vector4 import Vector4

class Body(object):
    def __init__(self):
        self.in_use = True # Used for object pooling
        self.mass = 0.0 # Kg
        self.position = Vector3()
        self.velocity = Vector3()
        self.rotation = Vector4()
        self.radius = 0.0
    
    def on_collide(self, engine: Engine, affecting_body: 'Body'):
        # If modifying velocity or other values, destroy this body and create a new one
        pass

    def on_tick(self, engine: Engine, seconds_passed: float):
        pass

    def __repr__(self) -> str:
        return json.dumps(self.__json__(), indent=2)

    def __json__(self):
        return {'in_use': self.in_use, 'mass': self.mass, 'radius': self.radius, 'position': self.position.__json__(), 'velocity': self.velocity.__json__(), 'rotation': self.rotation.__json__()}
