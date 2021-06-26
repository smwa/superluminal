from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Engine import Engine
    from .Player import Player

from .Body import Body

class Ship(Body):
    def __init__(self, owner: Player):
        super().__init__()
        self.modules = []
        self.owner = owner
    
    def add_module(self, module):
        self.modules.append(module)

    def on_collide(self, engine: Engine, affecting_body: 'Body'):
        # If modifying velocity or other values, destroy this body and create a new one
        for module in self.modules:
            module.on_collide(self, engine, affecting_body)

    def on_tick(self, engine: Engine, seconds_passed: float):
        for module in self.modules:
            module.on_tick(self, engine, seconds_passed)

    def __json__(self):
        parent = super().__json__()
        parent['modules'] = list(map(lambda module: module.__json__(), self.modules))
        return parent
