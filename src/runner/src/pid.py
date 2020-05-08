#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from lib.catch_bot.motor import Motor
import numpy as np
from math import pow, sqrt, atan, fabs
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


kp = 0.6
ki = 1.2
iMin = -0.2
iMax = 0.2
iSum = 0
kd = 0.075
old_y = 0

def PIDctl(error, y):
  global iSum, old_y
  up = kp * error
  iSum = iSum + error
  if (iSum < iMin):
    iSum = iMin
  if (iSum > iMax):
    iSum = iMax
  ui = ki * iSum
  ud = kd * (y - old_y)
  old_y = y

  return up + ui + ud

def get_point_handler(point):
  Y = 200
  X = 200
  H = 22.5
  Rk = 3.25

  x1 = 10
  y1 = 10

  x2 = point.x
  y2 = point.y
  xn = X / 2
  yn = Y / 2

  x4 = ((x2 - x1) * (y2 - y1) * (yn - y1) + x1 * pow(y2 - y1, 2) + xn * pow(x2 - x1, 2)) / (
      pow(y2 - y1, 2) + pow(x2 - x1, 2))
  y4 = (y2 - y1) * (x4 - x1) / (x2 - x1) + y1

  Tx = x4 - xn
  Ty = y4 - yn

  D = sqrt(Tx ** 2 + Ty ** 2)

  A = atan(np.abs(Tx) / np.abs(Ty))
  if Ty < 0:
    A = np.pi - A
  if x4 > xn:
    A = A * (-1)

  Angle = A * H * 180 / (2 * Rk * np.pi)

  D_anglel = 0
  D_angler = 0

  er = Angle
  el = er

  if A > 0:
    el *= (-1)
  else:
    er *= (-1)

  mist = 15

  last_l = left.get_angle()
  last_r = right.get_angle()

  while (not (Angle - mist < D_angler < Angle + mist)) and (not (Angle - mist < D_anglel < Angle + mist)):

    ul = PIDctl(el, D_anglel)
    ur = PIDctl(er, D_angler)

    if fabs(ur) > 1:
      ur = np.sign(ur) * 1
    if fabs(ul) > 1:
      ul = np.sign(ul) * 1

    left.go(ul)
    right.go(ur)


    left.update()
    right.update()

    el -= left.get_angle() - last_l
    er -= right.get.angle() - last_r

    D_anglel += left.get_angle() - last_l
    D_angler += right.get.angle() - last_r

    last_l = left.get_angle()
    last_r = right.get.angle()

  Angle = 360 * D / (2 * np.pi * Rk)

  D_anglel = 0
  D_angler = 0

  er = Angle
  el = er

  mist = 15

  last_l = left.get_angle()
  last_r = right.get_angle()

  while (not (Angle - mist < D_angler < Angle + mist)) and (not (Angle - mist < D_anglel < Angle + mist)):

    ul = PIDctl(el, D_anglel)
    ur = PIDctl(er, D_angler)

    if fabs(ur) > 1:
      ur = np.sign(ur) * 1
    if fabs(ul) > 1:
      ul = np.sign(ul) * 1

    left.go(ul)
    right.go(ur)


    left.update()
    right.update()

    el -= left.get_angle() - last_l
    er -= right.get.angle() - last_r

    D_anglel += left.get_angle() - last_l
    D_angler += right.get.angle() - last_r

    last_l = left.get_angle()
    last_r = right.get.angle()

  if ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) > 0:
    A = 90
  elif ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) < 0:
    A = -90

  Angle = A * H * 180 / (2 * Rk * np.pi)

  D_anglel = 0
  D_angler = 0

  er = Angle
  el = er

  if A > 0:
    el *= (-1)
  else:
    er *= (-1)

  mist = 15

  last_l = left.get_angle()
  last_r = right.get_angle()

  while (not (Angle - mist < D_angler < Angle + mist)) and (not (Angle - mist < D_anglel < Angle + mist)):

    ul = PIDctl(el, D_anglel)
    ur = PIDctl(er, D_angler)

    if fabs(ur) > 1:
      ur = np.sign(ur) * 1
    if fabs(ul) > 1:
      ul = np.sign(ul) * 1

    left.go(ul)
    right.go(ur)

    left.update()
    right.update()

    el -= left.get_angle() - last_l
    er -= right.get.angle() - last_r

    D_anglel += left.get_angle() - last_l
    D_angler += right.get.angle() - last_r

    last_l = left.get_angle()
    last_r = right.get.angle()

  left.stop()
  right.stop()

# ТВОЙ КОД ЗДЕСЬ
# КОГДА Я ПРИШЛЮ ТОЧКУ ОНА БУДЕТ ЗДЕСЬ point
# ТЫ МОЖЕШЬ ПОЛУЧИТЬ КООРДИНАТЫ point.x, point.y and point.z (z ВСЕГДА 0)
# ХЕНДЛЕР АСИНХРОННЫЙ. ЭТО ЗНАЧИТ, ЧТО ЕСЛИ ТЫ ПОЛУЧИШЬ НОВУЮ ТОЧКУ
# ЭТА ФУНКЦИЯ ОПЯТЬ ВЫЗОВЕТСЯ И БУДЕТ РАБОТАТЬ УЖЕ С НОВОЙ ТОЧКОЙ


def listen():
  rospy.init_node('runner')
  rospy.Subscriber('points', Point, get_point_handler)
  while not rospy.is_shutdown():
    left.update()
    right.update()


if __name__ == '__main__':
  listen()
