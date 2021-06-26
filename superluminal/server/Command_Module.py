import copy

from .Photon import Photon
from .Module_Interface import Module_Interface

class Command_Module(Module_Interface):
    def __init__(self) -> None:
        super().__init__()
        self.information = {'bodies': []}
    
    def on_collide(self, ship, engine, affecting_body):
        # If modifying velocity or other values, destroy this body and create a new one
        if isinstance(affecting_body, Photon):
            # TODO Check "encryption"
            # TODO elaborate on information and remove stale data
            self.information['bodies'].append({'location': affecting_body.emission_location, 'time': affecting_body.emission_time})
    
    def __json__(self):
        json_data = super().__json__()
        print(self.information)
        json_data['information'] = copy.deepcopy(self.information)
        for body in json_data['information']['bodies']:
            body['location'] = body['location'].__json__()
        return json_data
