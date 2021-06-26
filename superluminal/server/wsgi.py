from enum import Enum
import multiprocessing

from flask import Flask, redirect, url_for, Response

from .Engine import Engine
from .Vector3 import Vector3
from .Body import Body
from .Photon import Photon

class Request_Type(Enum):
    GET = 'get'

def start_engine(engine_pipe):
    e = Engine()

    # TODO rm
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
    # TODO end rm

    while True:
        if engine_pipe.poll():
            request = engine_pipe.recv()
            request_type = request[0]
            if request_type == Request_Type.GET:
                engine_pipe.send(str(e))
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
