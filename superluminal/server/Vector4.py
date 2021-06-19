class Vector4(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0

    def __repr__(self) -> str:
        return "({}, {}, {}, {})".format(self.x, self.y, self.z, self.w)
