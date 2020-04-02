#! /usr/bin/env python

from lib.catch_bot.motor import Motor
import rospy
import time


Motor.apply_requirements()

config = {

	'log': True,
	'm_a': 35,
	'm_b': 37,
	'en_a': 33,
	'en_b': 31,
	'pin_pwm': 27

}

test = Motor(config)

test.go(1)
time.sleep(2)
test.go(0.1)
time.sleep(2)
test.go(-1)

while not rospy.is_shutdown():
	test.update()
