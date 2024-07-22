from codecs import xmlcharrefreplace_errors
import numpy as np
from random import random
import matplotlib.pyplot as plt


#transformação linar -> y = a+(b-a)*x

def transformada(x):
    y = 1/x - 1
    return y

def distribuicao(y):
    p_y = 1/(1+y)**2
    return p_y

y = np.arange(0,10,0.01)
N = 101 ; dist_100 = []
Nb = 1001 ; dist_1000 = []
Nc = 10001 ;dist_10000 = []

for i in range(N):
    x = random()
    dist_100.append(transformada(x))

for i in range(Nb):
    x = random()
    dist_1000.append(transformada(x))

for i in range(Nc):
    x = random()
    dist_10000.append(transformada(x))

plt.plot(y,distribuicao(y), label = '$P(y)$', color = 'black')
plt.hist([dist_100, dist_1000, dist_10000], label = ['N = 100', 'N = 1000', 'N = 10000'], density='true', bins = [0,1,2,3,4,5,6,7,8,9,10])
plt.legend()
plt.xlabel("$P(y)$")
plt.ylabel("y")
plt.show()

plt.plot(y,distribuicao(y), label = '$P(y)$', color = 'black')
plt.hist([dist_100, dist_1000, dist_10000], label = ['N = 100', 'N = 1000', 'N = 10000'], density='true', bins = np.logspace(np.log10(0.01),np.log10(10.0)))
plt.legend()
plt.xlabel("$P(y)$")
plt.ylabel("y")
plt.title("Gráfico log - log")
plt.xscale('log')
plt.yscale('log')
plt.savefig('fig6.jpg')
plt.show()
