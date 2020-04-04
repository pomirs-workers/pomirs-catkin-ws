#! /usr/bin/env python

from lib.catch_bot.motor import Motor
import rospy
import time
import sys

Motor.apply_requirements()
Motor.unlock_all()

config_1 = {
	'log': True,
	'm_a': 37,
	'm_b': 35,
	'en_a': 31,
	'en_b': 33,
	'pin_pwm': 27,
	'deg_per_tick': 37.5
}

config_2 = {
	'log': True,
	'm_a': 38,
	'm_b': 36,
	'en_a': 24,
	'en_b': 26,
	'pin_pwm': 4,
	'deg_per_tick': 37.5
}


left = Motor(config_1)
right = Motor(config_2)

right.stop()
left.stop()

right.go(1)
left.go(1)

_old_excepthook = sys.excepthook
def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print "Stopped"
	right.stop()
	left.stop()
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook


while not rospy.is_shutdown():
	right.update()
	left.update()
