import numpy as np
import math 
from pylab import *
g = 9.81
print('Unesite nagib brda u stepenima:') 
nagib = float(input())
t1 = 0
v1 = 0
r1 = 0
print('Unesite vreme koje je proslo u sekundama:') 
t2 = float(input())


a = g * math.sin(math.radians(nagib))
#a = (g*float(np.sin(nagib*(np.pi/180))))
dt = t2 - t1
v2 = a * dt
r2 = v2 * dt

x=-math.cos(math.radians(nagib))*r2
y=-math.sin(math.radians(nagib))*r2
print('Brzina: ', v2, 'Predjeni put: ', r2)

plot(0, 0, 'o')
axis('equal')
xlabel('x [m]')
ylabel('y [m]')
title('Polozaj automobila na brdu nakon %.2f skundi' % t2)
plot(x, y, 'o')
quiver(x, y, angles = 'xy', scale_units = 'xy', scale = 1)
plot([], [], ' ', label="Brzina: %fm/s" % v2)
plot([], [], ' ', label="Predjeni put: %fm" % r2)
legend()
show()
