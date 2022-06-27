# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:26:02 2022

@author: josel
"""

import numpy as np
import numpy as np
import matplotlib.pyplot as plt

from smt.surrogate_models import LS
from smt.utils import compute_rms_error
from smt.utils.sm_test_case import SMTestCase

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

condiciones= np.array([[0.00131, 0.00161],
       [0.00107, 0.00243],
       [0.00091, 0.00225],
       [0.00181, 0.00221],
       [0.00121, 0.00135],
       [0.00081, 0.00061],
       [0.00221, 0.00209],
       [0.00147, 0.00163],
       [0.00059, 0.00159],
       [0.00105, 0.00193],
       [0.00203, 0.00155],
       [0.00151, 0.00075],
       [0.00089, 0.00147],
       [0.00159, 0.00215],
       [0.00055, 0.00181],
       [0.00169, 0.00237],
       [0.00103, 0.00165],
       [0.00231, 0.00183],
       [0.00153, 0.00153],
       [0.00173, 0.00081],
       [0.00223, 0.00233],
       [0.00133, 0.00231],
       [0.00113, 0.00199],
       [0.00097, 0.00119],
       [0.00189, 0.00051],
       [0.00077, 0.00131],
       [0.00145, 0.00171],
       [0.00129, 0.00063],
       [0.00067, 0.00117],
       [0.00075, 0.00085],
       [0.00219, 0.00121],
       [0.00099, 0.00083],
       [0.00191, 0.00185],
       [0.00249, 0.00095],
       [0.00175, 0.00133],
       [0.00215, 0.00157],
       [0.00137, 0.00067],
       [0.00123, 0.00069],
       [0.00187, 0.00189],
       [0.00143, 0.00129],
       [0.00157, 0.00213],
       [0.00065, 0.00065],
       [0.00185, 0.00223],
       [0.00227, 0.00091],
       [0.00061, 0.00217],
       [0.00247, 0.00115],
       [0.00233, 0.00143],
       [0.00199, 0.00151],
       [0.00163, 0.00087],
       [0.00069, 0.00167],
       [0.00139, 0.00099],
       [0.00109, 0.00227],
       [0.00155, 0.00195],
       [0.00083, 0.00093],
       [0.00093, 0.00109],
       [0.00171, 0.00241],
       [0.00135, 0.00101],
       [0.00245, 0.00205],
       [0.00161, 0.00175],
       [0.00117, 0.00111],
       [0.00051, 0.00055],
       [0.00207, 0.00149],
       [0.00115, 0.00203],
       [0.00087, 0.00177],
       [0.00057, 0.00187],
       [0.00195, 0.00127],
       [0.00183, 0.00173],
       [0.00241, 0.00089],
       [0.00079, 0.00079],
       [0.00095, 0.00211],
       [0.00071, 0.00053],
       [0.00229, 0.00073],
       [0.00211, 0.00207],
       [0.00179, 0.00071],
       [0.00209, 0.00077],
       [0.00235, 0.00141],
       [0.00063, 0.00219],
       [0.00193, 0.00059],
       [0.00213, 0.00249],
       [0.00111, 0.00235],
       [0.00205, 0.00179],
       [0.00177, 0.00229],
       [0.00053, 0.00057],
       [0.00085, 0.00245],
       [0.00141, 0.00137],
       [0.00217, 0.00139],
       [0.00125, 0.00103],
       [0.00149, 0.00105],
       [0.00239, 0.00113],
       [0.00237, 0.00145],
       [0.00073, 0.00169],
       [0.00197, 0.00201],
       [0.00225, 0.00123],
       [0.00201, 0.00125],
       [0.00165, 0.00107],
       [0.00101, 0.00239],
       [0.00167, 0.00191],
       [0.00119, 0.00097],
       [0.00243, 0.00197],
       [0.00127, 0.00247]])
e1=[]
e2=[]
for i in range(0,len(condiciones)):
    e1.append(condiciones[i][0])
    e2.append(condiciones[i][1])
e=np.array([e1,e2])
e1=np.array(e1)
e2=np.array(e2)


xt=np.array([0.002608098833218943,
 0.003912148249828414,
 0.03879547014413186,
 0.0,
 0.002608098833218943,
 0.08639327385037707,
 0.0,
 0.0,
 0.11997254632807057,
 0.005216197666437885,
 0.0,
 0.0,
 0.044663692518874476,
 0.0,
 0.14116334934797423,
 0.0,
 0.006520247083047355,
 0.0,
 0.0,
 0.0,
 0.0,
 0.002608098833218943,
 0.002608098833218943,
 0.024776938915579996,
 0.0,
 0.10138984214138583,
 0.0,
 0.002608098833218943,
 0.1088881262868902,
 0.10301990391214765,
 0.0,
 0.013692518874399453,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.002608098833218943,
 0.0,
 0.0,
 0.0,
 0.11312628689087093,
 0.0,
 0.0,
 0.11671242278654693,
 0.0,
 0.0,
 0.0,
 0.0,
 0.10660603980782364,
 0.0,
 0.003912148249828414,
 0.0,
 0.0743308167467396,
 0.03390528483184632,
 0.0,
 0.0013040494166094714,
 0.0,
 0.0,
 0.002608098833218943,
 0.14833562113932625,
 0.0,
 0.002608098833218943,
 0.049227865477007575,
 0.13203500343170804,
 0.0,
 0.0,
 0.0,
 0.09291352093342435,
 0.02608098833218947,
 0.10530199039121418,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.11345229924502329,
 0.0,
 0.0,
 0.002608098833218943,
 0.0,
 0.0,
 0.14442347288949786,
 0.06292038435140686,
 0.0,
 0.0,
 0.002608098833218943,
 0.0,
 0.0,
 0.0,
 0.10823610157858546,
 0.0,
 0.0,
 0.0,
 0.0,
 0.005216197666437885,
 0.0,
 0.002608098833218943,
 0.0,
 0.002608098833218943])


yt=np.array([0.141792 , 0.155777 , 0.171399 , 0.114669 , 0.145956 , 0.195964 ,
             
       0.0934718, 0.135187 , 0.243187 , 0.157454 , 0.10325  , 0.132749 ,
       0.175858 , 0.127669 , 0.258972 , 0.121604 , 0.159451 , 0.0884239,
       0.131742 , 0.119111 , 0.0923688, 0.141012 , 0.151191 , 0.164326 ,
       0.110303 , 0.210655 , 0.136212 , 0.142303 , 0.229152 , 0.214911 ,
       0.0946784, 0.162916 , 0.109283 , 0.0786593, 0.118066 , 0.0968681,
       0.139271 , 0.144973 , 0.111335 , 0.137071 , 0.129141 , 0.23525  ,
       0.112275 , 0.0902567, 0.238018 , 0.0798554, 0.0871159, 0.10518  ,
       0.125285 , 0.224715 , 0.138537 , 0.154268 , 0.130446 , 0.188725 ,
       0.168555 , 0.120219 , 0.140089 , 0.0810582, 0.12649  , 0.148408 ,
       0.259774 , 0.100642 , 0.149663 , 0.177687 , 0.253112 , 0.107337 ,
       0.113493 , 0.0830884, 0.202357 , 0.166252 , 0.219877 , 0.0892668,
       0.0986425, 0.115824 , 0.0997672, 0.0862278, 0.238388 , 0.10839  ,
       0.0979112, 0.15268  , 0.102104 , 0.116707 , 0.264931 , 0.183886 ,
       0.137758 , 0.0956363, 0.143838 , 0.134126 , 0.0841103, 0.0850433,
       0.227259 , 0.106143 , 0.0912244, 0.104315 , 0.123971 , 0.161264 ,
       0.122792 , 0.147401 , 0.0821305, 0.142961 ])

zt=np.array([55.975, 54.338, 53.247, 59.385, 55.293, 52.565, 62.113, 57.066,
       51.064, 54.201, 60.885, 57.339, 53.11 , 57.884, 50.791, 58.566,
       54.065, 62.795, 57.475, 58.839, 62.249, 56.111, 54.747, 53.656,
       59.93 , 52.292, 56.929, 55.838, 51.61 , 52.155, 61.976, 53.792,
       60.067, 64.022, 58.975, 61.703, 56.384, 55.429, 59.794, 56.793,
       57.748, 51.473, 59.657, 62.522, 51.201, 63.886, 62.931, 60.612,
       58.157, 51.746, 56.52 , 54.474, 57.611, 52.701, 53.383, 58.703,
       56.247, 63.749, 58.021, 55.02 , 50.519, 61.158, 54.883, 52.974,
       50.928, 60.339, 59.521, 63.477, 52.428, 53.519, 51.883, 62.658,
       61.431, 59.248, 61.294, 63.067, 51.337, 60.203, 61.567, 54.611,
       61.021, 59.112, 50.655, 52.837, 56.657, 61.84 , 55.565, 57.202,
       63.34 , 63.204, 52.019, 60.476, 62.385, 60.749, 58.293, 53.929,
       58.43 , 55.156, 63.613, 55.702])


st=np.array([6.34239e+08, 6.97386e+08, 7.54544e+08, 5.91800e+08, 6.59829e+08,
       7.79620e+08, 5.75765e+08, 6.22042e+08, 7.95252e+08, 7.02212e+08,
       5.73820e+08, 6.14455e+08, 7.85336e+08, 6.05621e+08, 7.82245e+08,
       5.94643e+08, 7.11934e+08, 5.69560e+08, 6.12783e+08, 5.90370e+08,
       5.86460e+08, 6.35341e+08, 6.83740e+08, 7.62486e+08, 5.77237e+08,
       7.89925e+08, 6.23441e+08, 6.39974e+08, 8.05487e+08, 7.93919e+08,
       5.69785e+08, 7.66321e+08, 5.83465e+08, 5.57898e+08, 5.86915e+08,
       5.82513e+08, 6.30448e+08, 6.51339e+08, 5.87524e+08, 6.24358e+08,
       6.06136e+08, 7.88719e+08, 5.97281e+08, 5.78652e+08, 7.79911e+08,
       5.71079e+08, 5.72742e+08, 5.94119e+08, 5.97685e+08, 7.93413e+08,
       6.28627e+08, 6.93562e+08, 6.12160e+08, 7.84924e+08, 7.70118e+08,
       5.90558e+08, 6.31819e+08, 5.63184e+08, 6.01220e+08, 6.74542e+08,
       7.60310e+08, 5.79921e+08, 6.82616e+08, 7.88884e+08, 7.86813e+08,
       5.93730e+08, 5.85978e+08, 5.71247e+08, 7.92406e+08, 7.76001e+08,
       7.73670e+08, 5.79302e+08, 5.73851e+08, 5.81902e+08, 5.79999e+08,
       5.61846e+08, 7.79880e+08, 5.80273e+08, 5.76403e+08, 6.91214e+08,
       5.81804e+08, 5.82917e+08, 7.84669e+08, 7.92179e+08, 6.23651e+08,
       5.84146e+08, 6.45906e+08, 6.19413e+08, 5.74477e+08, 5.76595e+08,
       7.86758e+08, 5.93583e+08, 5.85805e+08, 5.80040e+08, 5.93669e+08,
       7.14438e+08, 5.93485e+08, 6.70461e+08, 5.63689e+08, 6.38489e+08])


from smt.surrogate_models import QP
from smt.surrogate_models import KRG





sm10 = QP()
sm10.set_training_values(condiciones, xt)
sm10.train()

num10 = len(xt)
y10 = sm10.predict_values(condiciones)
t_error10 = compute_rms_error(sm10)
rms10 = mean_squared_error(xt, y10, squared=False)
r2_10=r2_score(xt, y10)

plt.plot(e1, xt, "o")
plt.plot(e1, y10,'o')
plt.xlabel("Espesor de la piel [m]")
plt.ylabel("Media del daño ")
plt.legend(["Datos de la muestra", "Predicción"])
plt.xlim([5e-4, 2.5e-3])
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.show()
msdeg=np.polyfit(e1,y10,2)



sm11 = QP()
sm11.set_training_values(condiciones, yt)
sm11.train()

y11 = sm11.predict_values(condiciones)
t_error11 = compute_rms_error(sm11)
rms11 = mean_squared_error(yt, y11, squared=False)
r2_11=r2_score(yt, y11)

plt.plot(e1, yt, "o")
plt.plot(e1, y11,'o')
plt.ylabel("Desplazamiento [m]")
plt.xlabel("Espesor de la piel [m]")
plt.legend(["Datos de la muestra", "Predicción"])
plt.xlim([5e-4, 2.5e-3])
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.show()
u1=np.polyfit(e1,y11,2)




sm12 = QP()
sm12.set_training_values(condiciones, zt)
sm12.train()

y12 = sm12.predict_values(condiciones)
t_error12 = compute_rms_error(sm12)
rms12 = mean_squared_error(zt, y12, squared=False)
r2_12=r2_score(zt, y12)

plt.plot(e1, zt, "o")
plt.plot(e1, y12,'o')
plt.xlabel("Espesor de la piel [m]")
plt.ylabel("Masa [kg]")
plt.legend(["Datos de la muestra", "Predicción"])
plt.xlim([5e-4, 2.5e-3])
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.show()
m=np.polyfit(e1,y12,2)


sm13 = QP()
sm13.set_training_values(condiciones, st)
sm13.train()

y13 = sm13.predict_values(condiciones)
t_error13 = compute_rms_error(sm13)
rms13 = mean_squared_error(st, y13, squared=False)
r2_13=r2_score(st, y13)

plt.plot(e1, st, "o")
plt.plot(e1, y13,'o')
plt.xlabel("Espesor de la piel [m]")
plt.ylabel("Tensión de Von-Mises [Pa]")
plt.legend(["Datos de la muestra", "Predicción"])
plt.xlim([5e-4, 2.5e-3])
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.show()
s1=np.polyfit(e1,y13,2)






ax = plt.axes(projection='3d')

# Data for a three-dimensional line

ax.plot3D(yt, zt, st, 'o')
#ax.scatter3D(yt, zt, st, c=st, cmap='Greens');




#Optimizar

from pyswarm import pso

def banana(x):
    test=np.array([[x[0],x[1]]])
    return sm10.predict_values(test)

def con(x):
    x1 = x[0]
    x2 = x[1]
    return [-(x1 + 0.25)**2 + 0.75*x2]

lb = [0.0005, 0.0005]
ub = [0.0025, 0.0025]

xopt10, fopt10 = pso(banana, lb, ub,omega=0.9,phip=2, phig=2,swarmsize=200)



def banana11(x):
    test=np.array([[x[0],x[1]]])
    return sm11.predict_values(test)


xopt11, fopt11 = pso(banana11, lb, ub,omega=0.9,phip=2, phig=2,swarmsize=200)


def banana12(x):
    test=np.array([[x[0],x[1]]])
    return sm12.predict_values(test)


xopt12, fopt12 = pso(banana12, lb, ub,omega=0.9,phip=2, phig=2,swarmsize=200)


def banana13(x):
    test=np.array([[x[0],x[1]]])
    return sm13.predict_values(test)


xopt13, fopt13 = pso(banana13, lb, ub,omega=0.9,phip=2, phig=2,swarmsize=200)



#con constraints
def con14(x):
    test=np.array([[x[0],x[1]]])
    return sm10.predict_values(test)-0
xopt14, fopt14 = pso(banana, lb, ub, f_ieqcons=con14)

def con15(x):
    test=np.array([[x[0],x[1]]])
    return sm11.predict_values(test)-0.175
xopt15, fopt15 = pso(banana11, lb, ub, f_ieqcons=con15)

def con16(x):
    test=np.array([[x[0],x[1]]])
    return sm12.predict_values(test)-57
xopt16, fopt16 = pso(banana12, lb, ub, f_ieqcons=con16)

def con17(x):
    test=np.array([[x[0],x[1]]])
    return sm13.predict_values(test)-6.5e+8
xopt17, fopt17 = pso(banana13, lb, ub, f_ieqcons=con17)


masa=np.linspace(51,63,20)
opt_masa=[]
for i in masa:
    def conn(x):
        test=np.array([[x[0],x[1]]])
        return sm12.predict_values(test)-i
    opt_masa.append(pso(banana12, lb, ub, f_ieqcons=conn))
    
masa=[]
desplazamiento=[]
daño=[]

for i in range(0,len(opt_masa)):
    masa.append(banana12(opt_masa[i][0]))
    desplazamiento.append(banana11(opt_masa[i][0]))
    daño.append(banana(opt_masa[i][0]))

m=[]    
for i in range(0,len(masa)):
    m.append(masa[i][0][0])
    
u=[]
for i in range(0,len(masa)):
    u.append(desplazamiento[i][0][0])
    
msdeg=[]
for i in range(0,len(masa)):
    msdeg.append(daño[i][0][0])
    
    
plt.plot(m, u, "o")
plt.xlabel("Masa [kg]")
plt.ylabel("Desplazamiento del borde de ataque [m]")
plt.show()



plt.plot(m, msdeg, "o")
plt.xlabel("Masa [kg]")
plt.ylabel("Media del daño del borde de ataque")
plt.show()
