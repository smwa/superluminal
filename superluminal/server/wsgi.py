from enum import Enum
import multiprocessing
import json

from flask import Flask, redirect, url_for, Response

from .Engine import Engine
from .Vector3 import Vector3
from .Body import Body
from .Photon import Photon
from .Ship import Ship
from .Player import Player
from .Command_Module import Command_Module

class Request_Type(Enum):
    GET = 'get'

def start_engine(engine_pipe):
    e = Engine()

    # TODO rm
    player_one = Player(1)
    e.add_player(player_one)

    player_two = Player(2)
    e.add_player(player_two)

    a = Body()
    a.mass = 10000000000
    a.position.x = 10
    e.add_body(a)

    b = Ship(player_one)
    b.mass = 10
    b.radius = 100
    b.velocity.z = 3
    command_module = Command_Module()
    b.add_module(command_module)
    e.add_body(b)

    direction = Vector3()
    direction.x = 1
    photon = Photon(direction, 100000)
    photon.position = Vector3()
    photon.position.x = b.position.x + 0.000001
    photon.position.y = b.position.y
    photon.position.z = b.position.z
    e.add_body(photon)
    # TODO end rm

    while True:
        if engine_pipe.poll():
            request = engine_pipe.recv()
            request_type = request[0]
            player_id = request[1]
            if request_type == Request_Type.GET:
                owner = list(filter(lambda player: player.id == player_id, e.players))
                if len(owner) > 0:
                    owner = owner[0]
                    commanded_bodies = filter(lambda body: hasattr(body, 'owner') and body.owner == owner, e.bodies)
                    commanded_bodies_jsons = map(lambda body: body.__json__(), commanded_bodies)
                    engine_pipe.send(json.dumps(list(commanded_bodies_jsons)))
        e.tick()

pipe_in_use = multiprocessing.Lock()
endpoint_pipe, engine_pipe = multiprocessing.Pipe()

engine_process = multiprocessing.Process(target=start_engine, args=(engine_pipe,))
engine_process.start()

app = Flask(__name__)

@app.route("/")
def root():
    return redirect(url_for("get_state", user_id=1))

@app.route("/<int:user_id>")
def get_state(user_id):
    pipe_in_use.acquire()
    endpoint_pipe.send([Request_Type.GET, user_id])
    response = endpoint_pipe.recv()
    pipe_in_use.release()
    return Response(response, content_type='application/json')
