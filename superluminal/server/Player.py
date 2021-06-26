import json

class Player(object):
    def __init__(self, id: int):
        self.id = id

    def __repr__(self) -> str:
        return json.dumps(self.__json__())

    def __json__(self):
        return {'id': self.id}
