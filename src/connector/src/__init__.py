#! /usr/bin/env python

import eventlet
import socketio
import rospy
from geometry_msgs.msg import Point

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)
poi_pub = rospy.Publisher('points', Point)
rospy.init_node('connector')


@sio.event
def connect(sid, environ):
    print('Host connected ', sid)


@sio.event
def disconnect(sid):
    print('Host disconnected ', sid)


@sio.on('point')
def get_point(sid, data):
    print(sid, data)
    point_msg = Point()
    poi_pub.publish(point_msg)


print('CatchBot listens on 8765 port :)')
eventlet.wsgi.server(eventlet.listen(('', 8765)), app)
