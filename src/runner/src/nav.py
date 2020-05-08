#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from lib.catch_bot.motor import Motor
import numpy as np
import time
from math import atan2, sqrt, cos

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


def navigate(xEND, yEND):
  radwheel = 0.03
  prevPath = 0
  course = np.pi / 2
  width = 0.3
  previousTime = 0
  angleL = left.get_angle()
  angleR = right.get_angle()
  deg2rad = 0.0174533
  K_I = 50


  left = Motor(config_1)
  right = Motor(config_2)
  xCoord = 100
  yCoord = 100

  intLength = 0

  while True:
    currentTime = time.time
    dt = currentTime - previousTime
    gyroSpeed = (left.get_angle() - angleL + right.get_angle() - angleR) * radwheel / dt / width / 2
    path = (angleR + angleL) / 2 * radwheel
    delthaPath = path - prevPath
    prevPath = path
    course = course + gyroSpeed * deg2rad * dt
    xCoord = xCoord + delthaPath * np.cos(course)
    yCoord = yCoord + delthaPath * np.sin(course)
    delthaX = xEND - xCoord
    delthaY = yEND - yCoord
    bearing = atan2(delthaY, delthaX)
    courseAngle = bearing - course
    if np.abs(courseAngle) > np.pi:
      courseAngle = courseAngle - np.sign(courseAngle) * 2 * np.pi

    length = sqrt(delthaY * delthaY + delthaX * delthaX)
    intLength = intLength + length * dt

    baseSpeed = 100 * np.tanh(length) * cos(courseAngle) + K_I * intLength

    control = courseAngle + np.sin(courseAngle) * baseSpeed / length

    if np.abs(control) > 30:
      control = np.sign(control) * 30

    pwmLeft = baseSpeed + control
    pwmRight = baseSpeed - control

    if np.abs(pwmLeft) > 1:
      pwmLeft = np.sign(pwmLeft) * 1
    if np.abs(pwmRight) > 1:
      pwmLeft = np.sign(pwmRight) * 1

    left.go(pwmLeft)
    right.go(pwmRight)

    previousTime = currentTime
    angleL = left.get_angle()
    angleR = right.get_angle()

def get_point_handler(point):
  navigate(point.x, point.y)


def listen():
	rospy.init_node('runner')
	rospy.Subscriber('points', Point, get_point_handler)
	while not rospy.is_shutdown():
		left.update()
		right.update()



if __name__ == '__main__':
	listen()
