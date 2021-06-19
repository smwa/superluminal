from Vector3 import Vector3
from Engine import Engine
from Body import Body

e = Engine()
a = e.get_new_body()
a.mass = 10000000000
a.position.x = 10
b = e.get_new_body()
b.mass = 10
b.velocity.z = 3
c = e.get_new_body()
c.radius = Body.PHOTON_RADIUS
direction = Vector3()
direction.x = 1.0
c.set_photon_velocity_by_direction(direction)
c.set_photon_mass_by_electromagnetic_frequency(500*10**12) # Visible light
while True:
    e.tick()
    print(b.position)
