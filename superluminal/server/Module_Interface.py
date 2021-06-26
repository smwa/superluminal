import json
from typing import TYPE_CHECKING

class Module_Interface(object):
    def __init__(self) -> None:
        super().__init__()

    def on_tick(self, ship, engine, seconds_passed: float):
        pass

    def on_collide(self, ship, engine, affecting_body):
        # If modifying velocity or other values, destroy this body and create a new one
        pass

    def __repr__(self) -> str:
        return json.dumps(self.__json__())

    def __json__(self):
        return {'type': type(self).__name__}
