#Questao de hit or miss
from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import random

x1 = linspace(0, 2 * math.pi, 400)

y1 = (x1 - 2)**4 + 12

y2 = (10 * np.sin(5 * x1))*((x1 - 4)**2) + 7

y3 = sqrt(2) * sqrt(201**2 - (x1 + 196)**2)


def func_azul(x,y):
  y_teste = ((x-2)**4)+12
  if y <= y_teste:
    return True
  return False

def func_laranja(x,y):
  y_teste = 10*sin(5*x)*((x-4)**2)+7
  if y >= y_teste:
    return True
  return False

def func_verde(x,y):
  y_teste = sqrt (2) * sqrt(201**2 - (x+196)**2)
  if y <= y_teste:
    return True
  return False


#aplicamos hit and miss
N = 200
hit = 0
hit_list_x = []
hit_list_y = []
miss_list_x = []
miss_list_y = []

for _ in range(N):
  x = random.uniform(2.99, 4.95)
  y = random.uniform(1.5,30)

  if (func_azul(x,y) and func_laranja(x,y) and  func_verde(x,y)):
    hit+=1
    hit_list_x.append(x)
    hit_list_y.append(y)

    continue
  
  miss_list_x.append(x)
  miss_list_y.append(y)



#plotar as curvas
plt.plot(x1, y1, 'black')  # plotando x, a separadamente
plt.plot(x1, y2, 'black')  # plotando x, b separadamente
plt.plot(x1, y3, 'black')  # plotando c, d separadamente 

#plotar o hit and miss
plt.scatter(hit_list_x, hit_list_y, color = "red") #area
plt.scatter(miss_list_x, miss_list_y, color = "dodgerblue")
plt.xlim((3,5))
plt.ylim((0,30))
plt.show()

#B

def cal_area(N):
  hit = 0; hit_list_x = []; hit_list_y = []; miss_list_x = []; miss_list_y = []

  for i in range(int(N)): 
    x = random.uniform(2.99, 4.95)
    y = random.uniform(1.5,30)
    if (func_azul(x,y) and func_laranja(x,y) and  func_verde(x,y)):
     hit+=1
     hit_list_x.append(x)
     hit_list_y.append(y)
    else:
      miss_list_x.append(x)
      miss_list_y.append(y) 
    area_ret = ((4.95 - 2.99 )* (30 - 1.5) )
    area = area_ret * len(hit_list_x) / N
  return area 

areas=[]
N = [10.0, 100.0, 1000.0, 10000.0, 100000.0, 1000000.0, 10000000.0]

for i in N: 
  areas.append(cal_area(i))


#C

def randi():
    global seed
    a = 1029; c = 221591; b = 1048576
    seed = (seed*a + c) % b
    return float(seed)/b
seed = 15

def cal_area_rand(N):
  hit = 0; hit_list_x = []; hit_list_y = []; miss_list_x = []; miss_list_y = []

  for i in range(int(N)): 
    xr = randi()*(4.95-2.99)+2.99
    yr = randi()*(30-1.5)+1.5
    if (func_azul(xr,yr) and func_laranja(xr,yr) and  func_verde(xr,yr)):
     hit+=1
     hit_list_x.append(xr)
     hit_list_y.append(yr)
    else:
      miss_list_x.append(xr)
      miss_list_y.append(yr) 
    area_ret = ((4.95 - 2.99 )* (30 - 1.5) )
    arear = area_ret * len(hit_list_x) / N
  return arear

areasr=[]
Nr = [10.0, 100.0, 1000.0, 10000.0, 100000.0, 1000000.0, 10000000.0]

for j in Nr: 
  areasr.append(cal_area_rand(j))


plt.scatter(N, areas, label = 'Random Python')
plt.scatter(N, areasr, label = 'Gerador de congruência')
plt.legend()
plt.title('Area estimada')
plt.xscale('log')
plt.savefig('fig4.jpg')
plt.show()

xr = randi()*(5-3)+3
yr = randi()*(30-1.5)+1.5
