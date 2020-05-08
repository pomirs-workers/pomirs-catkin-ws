#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from lib.catch_bot.motor import Motor
from math import atan, sqrt, pi, fabs
import time

Motor.apply_requirements()
Motor.unlock_all()

config_1 = {
  'log': True,
  'm_a': 37,
  'm_b': 35,
  'en_a': 24,
  'en_b': 26,
  'pin_pwm': 4,
  'deg_per_tick': 37.5
}

config_2 = {
  'log': True,
  'm_a': 38,
  'm_b': 36,
  'en_a': 31,
  'en_b': 33,
  'pin_pwm': 27,
  'deg_per_tick': 37.5
}

left = Motor(config_1)
right = Motor(config_2)

x0 = 20
y0 = 20
rk = 6
deg2rad = 0.0174533

def get_arc(angle):
  return (2 * rk * pi) * (angle / (2 * pi))

def handle(value):
  while fabs(get_arc(left.get_angle() * deg2rad)) < value:
    left.update()
    right.update()
    time.sleep(0.05)
  left.stop()
  right.stop()
  left.reset()
  right.reset()

def get_point_handler(point):
  x = point.x
  y = point.y
  angle = atan((y - y0) / (x - x0))
  dist = sqrt((x - x0) ** 2 + (y - y0) ** 2)
  arc = get_arc(angle)
  coef = 1
  if angle < 0:
    coef = -1
  left.go(0.3 * coef)
  right.go(0.3 * -coef)
  handle(arc)
  left.go(1)
  right.go(1)
  handle(dist)


def listen():
  rospy.init_node('runner')
  rospy.Subscriber('points', Point, get_point_handler)
  rospy.spin()


if __name__ == '__main__':
  listen()
