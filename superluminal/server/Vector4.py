import json

class Vector4(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0

    def __repr__(self) -> str:
        return json.dumps(self.__json__())

    def __json__(self):
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}
