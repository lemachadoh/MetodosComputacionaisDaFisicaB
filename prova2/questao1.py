from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import random

# QUESTÃO 1 A 
N0 = 100 ; lam = 1.1
tau = np.log(2)/lam
tf = 4*lam
delta_T = 0.25 ; delta_T2 = 0.1 ; delta_T3 = 0.05
Nt_1 = int(tf/delta_T) ; Nt_2 = int(tf/delta_T2) ; Nt_3 = int(tf/delta_T3)

#analitica 
t = np.arange(0, tf , delta_T3)
Na = N0*np.exp(-lam*t)
plt.plot(t, Na, label = "Sol. Analítica")

#numerica

def num (Nt_1):
  cx=N0*[1]                    #Definindo todos os núcleos em uma lista        
  total=[sum(cx)]              #Computando os núcleos que não decaíram
  p= lam/Nt_1                       #Probabilidade de decair a cada passo
  tt=np.arange(0,tf,1/Nt_1)      #Tempo
  for i in tt:                 #Percorrer o tempo
    for j in range(N0):        #Percorrer todas as partículas
      if(cx[j]==1):            #Se ainda não decaiu
        a=random.random()<p    #Checamos se decai
        cx[j] = (0) if (a) else (1)
    total.append(sum(cx))      #Computamos quantas restam
  plt.plot(tt,total[:-1], label = "$\Delta(t) = 0.25$")
num(1000)

def num2 (Nt_2):
  cx=N0*[1]                    #Definindo todos os núcleos em uma lista        
  total2=[sum(cx)]              #Computando os núcleos que não decaíram
  p= lam/Nt_2                      #Probabilidade de decair a cada passo
  tt2=np.arange(0,tf,1/Nt_2)      #Tempo
  for i in tt2:                 #Percorrer o tempo
    for j in range(N0):        #Percorrer todas as partículas
      if(cx[j]==1):            #Se ainda não decaiu
        a=random.random()<p    #Checamos se decai
        cx[j] = (0) if (a) else (1)
    total2.append(sum(cx))      #Computamos quantas restam
  plt.plot(tt2,total2[:-1], label = "$\Delta(t) = 0.1$")
num2(1000)

def num3 (Nt_3):
  cx=N0*[1]                    #Definindo todos os núcleos em uma lista        
  total3=[sum(cx)]              #Computando os núcleos que não decaíram
  p= lam/Nt_3                      #Probabilidade de decair a cada passo
  tt3=np.arange(0,tf,1/Nt_3)      #Tempo
  for i in tt3:                 #Percorrer o tempo
    for j in range(N0):        #Percorrer todas as partículas
      if(cx[j]==1):            #Se ainda não decaiu
        a=random.random()<p    #Checamos se decai
        cx[j] = (0) if (a) else (cx[j])
    total3.append(sum(cx))      #Computamos quantas restam
  plt.plot(tt3,total3[:-1], label = "$\Delta(t) = 0.05$")
num3(1000)


plt.legend()   
plt.title('Decaimento Radioativo')
plt.xlabel('Tempo  [s]')               
plt.ylabel('Núcleos [N]')
plt.savefig('fig1.jpg')
plt.show()

#QUESTÃO 1 B:

def num3 (Nt_3):
  cx=N0*[1]                    #Definindo todos os núcleos em uma lista        
  total3=[sum(cx)]              #Computando os núcleos que não decaíram
  p= lam/Nt_3                      #Probabilidade de decair a cada passo
  tt3=np.arange(0,tf,1/Nt_3)      #Tempo
  for i in tt3:                 #Percorrer o tempo
    for j in range(N0):        #Percorrer todas as partículas
      if(cx[j]==1):            #Se ainda não decaiu
        a=random.random()<p    #Checamos se decai
        cx[j] = (0) if (a) else (cx[j])
    total3.append(sum(cx))      #Computamos quantas restam
  plt.plot(tt3,total3[:-1], label = "$\Delta(t) = 0.05$")
num3(1000)
plt.plot(t, Na, label = "Sol. Analítica")
plt.title("Menor $\Delta(t)$ e Sol. Analítica")
plt.xlabel('Tempo  [s]')               
plt.ylabel('Núcleos [N]')
plt.legend()
plt.savefig('fig2.jpg')
plt.show()