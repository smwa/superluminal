from __future__ import annotations
from time import time
import json

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Body import Body

from .gravitational_constant import GRAVITATIONAL_CONSTANT

class Engine(object):
    def __init__(self):
        self.bodies = []
        self.frame_rate = 24.0
        self._last_tick_time = time()
    
    def add_body(self, body: Body):
        self.bodies.append(body)
    
    def destroy_body(self, body: Body):
        body.in_use = False
        self.bodies.remove(body)
    
    def tick(self):
        if time() - self._last_tick_time < 1.0 / self.frame_rate:
            return
        seconds_passed = time() - self._last_tick_time
        self._last_tick_time = time()

        bodies = list(filter(lambda body: body.in_use, self.bodies))

        # Apply velocity
        for body in bodies:
            body.position += body.velocity * seconds_passed

        for affected_body in bodies:
            for affecting_body in bodies:
                if affecting_body == affected_body:
                    continue
                vector_between_bodies = affecting_body.position - affected_body.position
                magnitude_squared = vector_between_bodies.magnitude_squared()

                # Add gravity to velocity: F = G*m1*m2/r^2, a = F/m1
                acceleration = GRAVITATIONAL_CONSTANT * affecting_body.mass / magnitude_squared # m/s^2
                velocity = acceleration * seconds_passed # m/s
                affected_body.velocity += vector_between_bodies.normalize() * velocity

                # Find collisions and let both objects handle it
                is_collided = ((affecting_body.radius + affected_body.radius)**2 - magnitude_squared) >= 0
                if is_collided:
                    affected_body.on_collide(self, affecting_body)

                # Let bodies run any object specific code, like launching missiles or applying engine force
                affected_body.on_tick(self, seconds_passed)

    def __repr__(self) -> str:
        return json.dumps(self.__json__(), indent=2)

    def __json__(self):
        jsons = list(map(lambda body: body.__json__(), self.bodies))
        return {'bodies': jsons}
