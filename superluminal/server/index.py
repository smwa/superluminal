from Engine import Engine

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
