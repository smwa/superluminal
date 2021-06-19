from time import time

from Body import Body

SPEED_OF_LIGHT = c = 299792458.0  # m/s
GRAVITATIONAL_CONSTANT = G = 0.00000000006673 # Nm^2/Kg^2

class Engine(object):
    def __init__(self):
        self.bodies = []
        self._unused_bodies = 0
        self.frame_rate = 24.0
        self._last_tick_time = time()
    
    def get_new_body(self) -> Body:
        for body in self.bodies:
            if not body.in_use:
                body.in_use = True
                self._unused_bodies -= 1
                return body
        body = Body()
        self.bodies.append(body)
        return body
    
    def destroy_body(self, body):
        body.in_use = False
        self._unused_bodies += 1
        # TODO Consider garbage collection if there are too many unused bodies
    
    def tick(self):
        if time() - self._last_tick_time < 1.0 / self.frame_rate:
            return
        seconds_passed = time() - self._last_tick_time
        self._last_tick_time = time()

        bodies = filter(lambda body: body.in_use, self.bodies)

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

e = Engine()
a = e.get_new_body()
a.mass = 10000000000
a.position.x = 10
b = e.get_new_body()
b.mass = 10
b.velocity.z = 3
while True:
    e.tick()
    print(b.position)
