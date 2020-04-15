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
	#константы
	Y = 200
	X = 200
	H = 22.5
	Rk = 3.25
	#получение траектории 
	x1 = point.x
	y1 = point.y
	while x1 == point.x and y1 == point.y:
		time.sleep(0.1)
	x2 = point.x
	y2 = point.y
	xn = X / 2
	yn = Y / 2
	#получение точки перпендикуляра
	x4=((x2-x1)*(y2-y1)*(yn-y1)+x1*pow(y2-y1, 2)+xn*pow(x2-x1, 2))/(pow(y2-y1, 2)+pow(x2-x1, 2))
	y4=(y2-y1)*(x4-x1)/(x2-x1)+y1

	Tx = xn - x4
	Ty = yn - y4
#Поиск длины пути до цели
	D = math.sqrt(Tx**2 + Ty**2)
#Поиск кратчайшего угла поворота
	A = math.atan(np.abs(Tx)/np.abs(Ty))
	if Ty > 0:
		A = np.pi - A
	if x4 > xn:
		A = A * (-1)

	Angle = A * H * 180 / (2 * Rk * np.pi)
	D_angle = 0

	e = Angle
	mist = 15 #ошибка энкодера
	while np.abs(e) > mist :
		u = e / Angle
		if A > 0:
			ur = u
			ul = -1 * u
		else:
			ur = u
			ul = -1 * u
		lel = left.get_angle
		rel = right.get.angle
		left.go(ul)
		right.go(ur)
		left.update()
		right.update()
		le = left.get_angle
		re = right.get.angle
		D_right = rel - re
		D_left = lel - le
		e -= np.abs(D_right) #Или D_right, если они равны. Должны быть равны, иначе пока хз как это считать
	left.stop()
	right.stop()

	s = 0
	while D - s > 0:
		u = (D - s) / D
		lel = left.get_angle
		rel = right.get.angle
		left.go(u)
		right.go(u)
		left.update()
		right.update()
		le = left.get_angle
		re = right.get.angle
		D_right = rel - re
		D_left = lel - le
		s = 2 * np.pi * Rk * D_right/360
	left.stop()
	right.stop()

	if ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) > 0:
		A = 90
	elif ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) < 0:
		A = -90

	Angle = A * H * 180 / (2 * Rk * np.pi)
	e = Angle
	mist = 15 #ошибка энкодера
	while np.abs(e) > mist :
		u = e / Angle
		if A > 0:
			ur = u
			ul = -1 * u
		else:
			ur = u
			ul = -1 * u
		lel = left.get_angle
		rel = right.get.angle
		left.go(ul)
		right.go(ur)
		left.update()
		right.update()
		le = left.get_angle
		re = right.get.angle
		D_right = rel - re
		D_left = lel - le
		e -= np.abs(D_right) #Или D_right, если они равны. Должны быть равны, иначе пока хз как это считать
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
