import icecream
import decimal
from math import *
from matplotlib.pyplot import plot, show, legend, xlim, ylim, xlabel, ylabel
import matplotlib.pyplot as plt
#GMm/d^2 = mac = mw^2d
#GM/d^2 = s*pi/T
G = 4.0 * pi**2
m = 10
n = 1
r = 1000

#Primeiro vamos fazer por Verlet

#condicao inicial
x = 1 ; vx = 0
y = 0 ; vy = 2 * pi


def a(x, y):
    d = sqrt(x**2 + y**2)
    acel = -G / d**3
    return acel

def energia(v):
    e = ((5.9722e24/1.989e30) * v**2)/2 - G*(5.9722e24/1.989e30) / r
    return e

v = sqrt(vx**2 + vy**2)
s = sqrt(x**2 + y**2)
tf = 1
dt = 0.001
dt2 = dt * dt
nt = int(tf / dt)


T = [] ; X = [] ; Y = [] ; VX = [] ; VY = [] ; E = []
T.append(0) ; X.append(x)  ; Y.append(y) ;VX.append(vx) ; VY.append(vy) ; E.append(energia(v))

xold = x
x = x + vx * dt

yold = y
y = y + vy * dt

sold = s
s = s + v *dt

for i in range(1, nt + 1):
    t = i * dt
    acel = a(x, y)  #aceleracao funcao de x e y

    xnew = 2 * x - xold + acel * x * dt2
    vx = (xnew - xold) / (2 * dt)


    ynew = 2 * y - yold + acel * y * dt2
    vy = (ynew - yold) / (2 * dt)

    e = energia(v)

    T.append(t)
    X.append(x)
    Y.append(y)
    VX.append(vx)
    VY.append(vy)
    E.append(energia(v))


    xold = x
    x = xnew

    yold = y
    y = ynew


xlabel("Tempo")
ylabel("Energia")
plot(T, E, color="orange")
#plot(W, T, label="Velocidade em y", color="blue")
#legend(loc="lower right", fontsize="small")
plt.yscale('log')
plt.show()
