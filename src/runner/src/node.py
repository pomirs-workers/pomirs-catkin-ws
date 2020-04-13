#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from lib.catch_bot.motor import Motor

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


def get_point_handler(point):
	print(point)
	left.go(point.y)
	right.go(point.x)


def listen():
	rospy.init_node('runner')
	rospy.Subscriber('points', Point, get_point_handler)
	while not rospy.is_shutdown():
		left.update()
		right.update()



if __name__ == '__main__':
	listen()
