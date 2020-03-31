#! /usr/bin/env python

import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('Host connected ', sid)


@sio.event
def disconnect(sid):
    print('Host disconnected ', sid)


@sio.on('point')
def get_point(sid, data):
    print(sid, data)


print('CatchBot listens on 8765 port :)')
eventlet.wsgi.server(eventlet.listen(('', 8765)), app)
