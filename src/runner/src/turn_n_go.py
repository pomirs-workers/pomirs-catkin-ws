#!/usr/bin/env python
# coding: utf-8

import time
import numpy as np
from math import pow, sqrt, atan

Y = 200
X = 200
H = 25
Rk = 2.5

Tx = 20
Ty = 20

# handler

x1 = point.x
y1 = point.y
while x1 == point.x and y1 == point.y:
    time.sleep(0.1)
x2 = point.x
y2 = point.y
xn = X / 2
yn = Y / 2


# Поиск ближайшей к роботу точки на прямой

# In[6]:


x4=((x2-x1)*(y2-y1)*(yn-y1)+x1*pow(y2-y1, 2)+xn*pow(x2-x1, 2))/(pow(y2-y1, 2)+pow(x2-x1, 2))
y4=(y2-y1)*(x4-x1)/(x2-x1)+y1
#print(x4,y4)


# Поиск кратчайшего угла поворота и расстояния до точки (A, D)

# In[7]:


Tx = xn - x4
Ty = yn - y4
#Поиск длины пути до цели
D = sqrt(Tx**2 + Ty**2)
#Поиск кратчайшего угла поворота
A = atan(np.abs(Tx)/np.abs(Ty))
if Ty > 0:
    A = np.pi - A
if x4 > xn:
    A = A * (-1)
#print(math.degrees(A),D)


# In[8]:


#Read info about A, H, Rk, Distance(D) from file


# Angle - необходимый угол поворота колес в градусах, H - расстояние между колесами, Rk - радиус колеса

# In[9]:


Angle = A * H * 180 / (2 * Rk * np.pi)
D_angle = 0
#print(Angle)


# A > 0 - Влево (ul = -ur, ur > 0), A < 0 - Вправо (ur = -ul, ul > 0)

# Поворот робота в сторону движения к точке на прямой по кратчайшему пути (по перпендикуляру к этой прямой)

# In[19]:


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


# Движение робота к этой самой точке (то бишь на расстояни D)

# In[1]:


s = 0
u = 0.1
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


# Разворот робота по линии движения объекта. По сути формула та же, что и при повороте на высчитываемый угол, только мы точно знаем, что угол 90 градусов. Только необходим разворот по вектору движения объекта.

# In[17]:


if ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) > 0:
    A = 90
elif ((y2 - y1) * (x4 - xn) - (x2 - x1) * (y4 - yn)) < 0:
    A = -90
#print (A)


# In[18]:


Angle = A * H * 180 / (2 * Rk * np.pi)
e = Angle
mist = 15 #ошибка энкодера
while np.abs(e) > mist:
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
    e -= np.abs(D_right)
left.stop()
right.stop()


# In[ ]:




