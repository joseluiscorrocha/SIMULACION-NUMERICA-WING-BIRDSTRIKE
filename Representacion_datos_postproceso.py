# -*- coding: utf-8 -*-
"""
Created on April  1 11:47:16 2022

@author: josel
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


def string_to_int(s):
    try:
        temp = float(eval(str(s)))
        if type(temp) == float:
            return temp
    except:
        return
    
val = string_to_int('23e-15')
valores=[]
for j in range(0,1):
    archivo=[]
    f = open("job_definitivo"+str(j)+".sta", "r")
    for x in f:
      archivo.append(x)
    for i in archivo:
        if 'Total mass in model' in i:
            a=i
    df1sdeg = pd.read_fwf('abaqus_sdeg_job_definitivo'+str(j)+'.rpt',header=None)
    df1u = pd.read_fwf('abaqus_u_job_definitivo'+str(j)+'.rpt',header=None)
    df1s = pd.read_fwf('abaqus_s_job_definitivo'+str(j)+'.rpt',header=None)

    aux1=[]
    
    for i in range(2,len(df1sdeg.columns)):
        aux1.append(string_to_int(df1sdeg[i][len(df1sdeg)-2])) #el de s esta mal
    #valores.append(max(aux1))
    aux=[]
    for i in range(2,len(df1u.columns)):
        aux.append(string_to_int(df1u[i][len(df1u)-2])) #el de s esta mal
    
    aux2=[]
    
    for i in range(2,len(df1s.columns)):
        aux2.append(string_to_int(df1s[i][len(df1s)-2])) #el de s esta mal

    valores.append([max(aux1),max(aux),string_to_int(a[len(a)-7:len(a)-1]),max(aux2)])
muestra1=[]
muestra2=[]
muestra3=[]
muestra4=[]
for i in range(0,len(valores)):
    muestra1.append(valores[i][0])
    muestra2.append(valores[i][1])
    muestra3.append(valores[i][2])
    muestra4.append(valores[i][3])
muestra=np.array([muestra1,muestra2,muestra3,muestra4])
fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[1], muestra[2], "o")

axs.set_xlabel("Desplazamiento (m)")
axs.set_ylabel("Masa (kg)")



plt.show()


fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[0], muestra[2], "o")

axs.set_xlabel("Daño")
axs.set_ylabel("Masa (kg)")



plt.show()


fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[0], muestra[1], "o")

axs.set_xlabel("Daño")
axs.set_ylabel("Desplazamiento (m)")



plt.show()

fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[0], muestra[3], "o")

axs.set_xlabel("Daño")
axs.set_ylabel("Tensión de Von Mises (Pa)")



plt.show()

fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[1], muestra[3], "o")

axs.set_xlabel("Desplazamiento (m)")
axs.set_ylabel("Tensión de Von Mises (Pa)")



plt.show()

fig, axs = plt.subplots(1)

# add a plot with variance
axs.plot(muestra[2], muestra[3], "o")

axs.set_xlabel("Masa (kg)")
axs.set_ylabel("Tensión de Von Mises (Pa)")



plt.show()

import numpy as np
import matplotlib.pyplot as plt

from smt.surrogate_models import LS
from smt.utils import compute_rms_error
from smt.utils.sm_test_case import SMTestCase

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

xt = np.array(muestra1)
yt = np.array(muestra2)
zt= np.array(muestra3)
st= np.array(muestra4)



u=[]
t=[]
for i in range(2,44):
    t.append(string_to_int(df1u[1][i]))
for j in range(1,len(df1u.columns)):
    aux=[]
    for i in range(2,len(df1u[0])-5):
        aux.append(string_to_int(df1u[j][i]))
    u.append(aux)
fig, axs = plt.subplots(1)
for i in range(0,len(u)):
    #plt.xlim(0, 5e-3)
    
   
    axs.plot(t,u[i])


# add a plot with variance


axs.set_xlabel("Tiempo [s]")
axs.set_ylabel("Desplazamiento del borde de ataque (m)")



plt.show()
    



