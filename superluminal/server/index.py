from Vector3 import Vector3
from Engine import Engine
from Body import Body
from Photon import Photon

e = Engine()

a = Body()
a.mass = 10000000000
a.position.x = 10
e.add_body(a)

b = Body()
b.mass = 10
b.velocity.z = 3
e.add_body(b)

direction = Vector3()
direction.x = 1.0
c = Photon(direction, 500*10**12) # Visible light
e.add_body(c)

while True:
    e.tick()
    print(b.position)
