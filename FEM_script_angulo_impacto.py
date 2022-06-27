# -*- coding: utf-8 -*-
"""
Created on March 10 11:39:55 2022

@author: josel
"""

# -*- coding: utf-8 -*-



#Larguero
def Largueros_frontal(posicion,modelo):
    s= mdb.models[modelo].sketches['__profile__']

    if (posicion % 9 == 1):
        s.Line(point1=(coordenadas[64]), point2=(coordenadas[64-1]))
        s.Line(point1=(coordenadas[64-1]), point2=(coordenadas[134+1]))
        s.Line(point1=(coordenadas[134+1]), point2=(coordenadas[134]))
        s.Line(point1=(coordenadas[134]), point2=(coordenadas[64]))
    elif (posicion % 9 == 2):
        s.Line(point1=(coordenadas[63]), point2=(coordenadas[63-1]))
        s.Line(point1=(coordenadas[63-1]), point2=(coordenadas[135+1]))
        s.Line(point1=(coordenadas[135+1]), point2=(coordenadas[135]))
        s.Line(point1=(coordenadas[135]), point2=(coordenadas[63]))
    elif (posicion % 9 == 3):
        s.Line(point1=(coordenadas[62]), point2=(coordenadas[62-1]))
        s.Line(point1=(coordenadas[62-1]), point2=(coordenadas[136+1]))
        s.Line(point1=(coordenadas[136+1]), point2=(coordenadas[136]))
        s.Line(point1=(coordenadas[136]), point2=(coordenadas[62]))
    elif (posicion % 9 == 4):
        s.Line(point1=(coordenadas[61]), point2=(coordenadas[61-1]))
        s.Line(point1=(coordenadas[61-1]), point2=(coordenadas[137+1]))
        s.Line(point1=(coordenadas[137+1]), point2=(coordenadas[137]))
        s.Line(point1=(coordenadas[137]), point2=(coordenadas[61]))
    elif (posicion % 9 == 5):
        s.Line(point1=(coordenadas[60]), point2=(coordenadas[60-1]))
        s.Line(point1=(coordenadas[60-1]), point2=(coordenadas[138+1]))
        s.Line(point1=(coordenadas[138+1]), point2=(coordenadas[138]))
        s.Line(point1=(coordenadas[138]), point2=(coordenadas[60]))
    elif (posicion % 9 == 6):
        s.Line(point1=(coordenadas[59]), point2=(coordenadas[59-1]))
        s.Line(point1=(coordenadas[59-1]), point2=(coordenadas[139+1]))
        s.Line(point1=(coordenadas[139+1]), point2=(coordenadas[139]))
        s.Line(point1=(coordenadas[139]), point2=(coordenadas[59]))
    elif (posicion % 9 == 7):
        s.Line(point1=(coordenadas[58]), point2=(coordenadas[58-1]))
        s.Line(point1=(coordenadas[58-1]), point2=(coordenadas[140+1]))
        s.Line(point1=(coordenadas[140+1]), point2=(coordenadas[140]))
        s.Line(point1=(coordenadas[140]), point2=(coordenadas[58]))
    elif (posicion % 9 == 8):
        s.Line(point1=(coordenadas[57]), point2=(coordenadas[57-1]))
        s.Line(point1=(coordenadas[57-1]), point2=(coordenadas[141+1]))
        s.Line(point1=(coordenadas[141+1]), point2=(coordenadas[141]))
        s.Line(point1=(coordenadas[141]), point2=(coordenadas[57]))
    elif (posicion % 9 == 0):
        s.Line(point1=(coordenadas[56]), point2=(coordenadas[56-1]))
        s.Line(point1=(coordenadas[56-1]), point2=(coordenadas[142+1]))
        s.Line(point1=(coordenadas[142+1]), point2=(coordenadas[142]))
        s.Line(point1=(coordenadas[142]), point2=(coordenadas[56]))
        
        
def contacto_Largueros_frontal(posicion):
    c_slave=[]
    if (posicion % 9 == 1):
        c_slave.append([coordenadas[64][0]+0.007,coordenadas[64][1]/2])
    elif (posicion % 9 == 2):
        c_slave.append([coordenadas[63][0]+0.007,coordenadas[63][1]/2])
    elif (posicion % 9 == 3):
        c_slave.append([coordenadas[62][0]+0.007,coordenadas[62][1]/2])
    elif (posicion % 9 == 4):
        c_slave.append([coordenadas[61][0]+0.007,coordenadas[61][1]/2])
    elif (posicion % 9 == 5):
        c_slave.append([coordenadas[60][0]+0.007,coordenadas[60][1]/2])
    elif (posicion % 9 == 6):
        c_slave.append([coordenadas[59][0]+0.007,coordenadas[59][1]/2])
    elif (posicion % 9 == 7):
        c_slave.append([coordenadas[58][0]+0.007,coordenadas[58][1]/2])
    elif (posicion % 9 == 8):
        c_slave.append([coordenadas[57][0]+0.007,coordenadas[57][1]/2])
    elif (posicion % 9 == 0):
        c_slave.append([coordenadas[56][0]+0.007,coordenadas[56][1]/2])
    return c_slave
        
        
def contacto_top_Largueros_frontal(posicion):
    c_slave=[]
    if (posicion % 9 == 1):
        c_slave.append([coordenadas[64][0],coordenadas[64][1],coordenadas[134][0],coordenadas[134][1]])
    elif (posicion % 9 == 2):
        c_slave.append([coordenadas[63][0],coordenadas[63][1],coordenadas[135][0],coordenadas[135][1]])
    elif (posicion % 9 == 3):
        c_slave.append([coordenadas[62][0],coordenadas[62][1],coordenadas[136][0],coordenadas[136][1]])
    elif (posicion % 9 == 4):
        c_slave.append([coordenadas[61][0]+0.007,coordenadas[61][1],coordenadas[137][0],coordenadas[137][1]])
    elif (posicion % 9 == 5):
        c_slave.append([coordenadas[60][0]+0.007,coordenadas[60][1]+0.000005,coordenadas[138][0]+0.007,coordenadas[138][1]-0.00005])
    elif (posicion % 9 == 6):
        c_slave.append([coordenadas[59][0],coordenadas[59][1],coordenadas[139][0],coordenadas[139][1]])
    elif (posicion % 9 == 7):
        c_slave.append([coordenadas[58][0],coordenadas[58][1],coordenadas[140][0],coordenadas[140][1]])
    elif (posicion % 9 == 8):
        c_slave.append([coordenadas[57][0],coordenadas[57][1],coordenadas[141][0],coordenadas[141][1]])
    elif (posicion % 9 == 0):
        c_slave.append([coordenadas[56][0],coordenadas[56][1],coordenadas[142][0],coordenadas[142][1]])
    return c_slave   
        
def Largueros_trasero(posicion,modelo):
    s= mdb.models[modelo].sketches['__profile__']
    if (posicion <10 ):
        s.Line(point1=(coordenadas[27]), point2=(coordenadas[27-1]))
        s.Line(point1=(coordenadas[27-1]), point2=(coordenadas[171+1]))
        s.Line(point1=(coordenadas[171+1]), point2=(coordenadas[171]))
        s.Line(point1=(coordenadas[171]), point2=(coordenadas[27]))
    elif (posicion < 19):
        s.Line(point1=(coordenadas[26]), point2=(coordenadas[26-1]))
        s.Line(point1=(coordenadas[26-1]), point2=(coordenadas[172+1]))
        s.Line(point1=(coordenadas[172+1]), point2=(coordenadas[172]))
        s.Line(point1=(coordenadas[172]), point2=(coordenadas[26]))
    elif (posicion < 28):
        s.Line(point1=(coordenadas[25]), point2=(coordenadas[25-1]))
        s.Line(point1=(coordenadas[25-1]), point2=(coordenadas[173+1]))
        s.Line(point1=(coordenadas[173+1]), point2=(coordenadas[173]))
        s.Line(point1=(coordenadas[173]), point2=(coordenadas[25]))
    elif (posicion <37):
        s.Line(point1=(coordenadas[24]), point2=(coordenadas[24-1]))
        s.Line(point1=(coordenadas[24-1]), point2=(coordenadas[174+1]))
        s.Line(point1=(coordenadas[174+1]), point2=(coordenadas[174]))
        s.Line(point1=(coordenadas[174]), point2=(coordenadas[24]))
    elif (posicion < 46):
        s.Line(point1=(coordenadas[23]), point2=(coordenadas[23-1]))
        s.Line(point1=(coordenadas[23-1]), point2=(coordenadas[175+1]))
        s.Line(point1=(coordenadas[175+1]), point2=(coordenadas[175]))
        s.Line(point1=(coordenadas[175]), point2=(coordenadas[23]))
    elif (posicion < 55):
        s.Line(point1=(coordenadas[22]), point2=(coordenadas[22-1]))
        s.Line(point1=(coordenadas[22-1]), point2=(coordenadas[176+1]))
        s.Line(point1=(coordenadas[176+1]), point2=(coordenadas[176]))
        s.Line(point1=(coordenadas[176]), point2=(coordenadas[22]))
    elif (posicion < 64):
        s.Line(point1=(coordenadas[21]), point2=(coordenadas[21-1]))
        s.Line(point1=(coordenadas[21-1]), point2=(coordenadas[177+1]))
        s.Line(point1=(coordenadas[177+1]), point2=(coordenadas[177]))
        s.Line(point1=(coordenadas[177]), point2=(coordenadas[21]))
 
        
def contacto_Largueros_trasero(posicion):
    c_slave=[]
    if (posicion <10 ):
        c_slave.append([coordenadas[27][0]+0.007,coordenadas[27][1]/2])
    elif (posicion < 19):
        c_slave.append([coordenadas[26][0]+0.007,coordenadas[26][1]/2])
    elif (posicion < 28):
        c_slave.append([coordenadas[25][0]+0.007,coordenadas[25][1]/2])
    elif (posicion <37):
        c_slave.append([coordenadas[24][0]+0.007,coordenadas[24][1]/2])
    elif (posicion < 46):
        c_slave.append([coordenadas[23][0]+0.007,coordenadas[23][1]/2])
    elif (posicion < 55):
        c_slave.append([coordenadas[22][0]+0.007,coordenadas[22][1]/2])
    elif (posicion < 64):
        c_slave.append([coordenadas[21][0]+0.007,coordenadas[21][1]/2])
    return c_slave   
        
def contacto_top_Largueros_trasero(posicion):
    c_slave=[]
    if (posicion <10 ):
        c_slave.append([coordenadas[27][0],coordenadas[27][1],coordenadas[171][0],coordenadas[171][1]])
    elif (posicion < 19):
        c_slave.append([coordenadas[26][0],coordenadas[26][1],coordenadas[172][0],coordenadas[172][1]])
    elif (posicion < 28):
        c_slave.append([coordenadas[25][0],coordenadas[25][1],coordenadas[173][0],coordenadas[173][1]])
    elif (posicion <37):
        c_slave.append([coordenadas[24][0],coordenadas[24][1],coordenadas[174][0],coordenadas[174][1]])
    elif (posicion < 46):
        c_slave.append([coordenadas[23][0],coordenadas[23][1],coordenadas[175][0],coordenadas[175][1]])
    elif (posicion < 55):
        c_slave.append([coordenadas[22][0],coordenadas[22][1],coordenadas[176][0],coordenadas[176][1]])
    elif (posicion < 64):
        c_slave.append([coordenadas[21][0],coordenadas[21][1],coordenadas[177][0],coordenadas[177][1]])
    return c_slave

coordenadas= [[2.0, 0.00252],
 [1.99496, 0.00334],
 [1.98582, 0.00482],
 [1.9741, 0.0067],
 [1.96038, 0.00888],
 [1.94496, 0.01132],
 [1.92812, 0.01398],
 [1.90998, 0.0168],
 [1.89072, 0.01976],
 [1.87042, 0.02286],
 [1.84922, 0.02606],
 [1.82716, 0.02936],
 [1.80434, 0.03274],
 [1.78082, 0.03616],
 [1.75666, 0.03966],
 [1.73192, 0.04318],
 [1.70664, 0.04674],
 [1.68086, 0.05034],
 [1.65466, 0.05394],
 [1.62802, 0.05754],
 [1.60102, 0.06116],
 [1.5737, 0.06476],
 [1.54606, 0.06836],
 [1.51814, 0.07194],
 [1.49, 0.0755],
 [1.46164, 0.07904],
 [1.4331, 0.08254],
 [1.4044, 0.086],
 [1.37556, 0.08942],
 [1.34662, 0.0928],
 [1.31758, 0.09612],
 [1.2885, 0.0994],
 [1.25936, 0.1026],
 [1.2302, 0.10574],
 [1.20104, 0.10882],
 [1.1719, 0.11182],
 [1.14282, 0.11476],
 [1.11378, 0.1176],
 [1.0848, 0.12036],
 [1.05594, 0.12304],
 [1.02718, 0.1256],
 [0.99854, 0.12808],
 [0.97006, 0.13046],
 [0.94174, 0.13274],
 [0.91358, 0.1349],
 [0.88562, 0.13694],
 [0.85786, 0.13888],
 [0.83034, 0.1407],
 [0.80304, 0.14238],
 [0.77598, 0.14394],
 [0.7492, 0.14538],
 [0.7227, 0.14666],
 [0.69648, 0.14782],
 [0.67058, 0.14886],
 [0.64498, 0.14974],
 [0.61972, 0.15048],
 [0.59478, 0.15106],
 [0.57022, 0.1515],
 [0.54602, 0.1518],
 [0.5222, 0.15196],
 [0.49876, 0.15194],
 [0.47574, 0.15178],
 [0.45312, 0.15148],
 [0.43092, 0.15102],
 [0.40916, 0.1504],
 [0.38786, 0.14962],
 [0.367, 0.14866],
 [0.34662, 0.1475],
 [0.32672, 0.14608],
 [0.3073, 0.1444],
 [0.2884, 0.14244],
 [0.26998, 0.14018],
 [0.2521, 0.1376],
 [0.23476, 0.13474],
 [0.21794, 0.13156],
 [0.20168, 0.12806],
 [0.18598, 0.12428],
 [0.17084, 0.1202],
 [0.15628, 0.11584],
 [0.14232, 0.11124],
 [0.12894, 0.10638],
 [0.11618, 0.10132],
 [0.10402, 0.09604],
 [0.0925, 0.0906],
 [0.0816, 0.085],
 [0.07136, 0.07928],
 [0.06176, 0.07346],
 [0.05282, 0.06758],
 [0.04454, 0.06164],
 [0.03694, 0.0557],
 [0.03004, 0.04974],
 [0.02382, 0.04384],
 [0.0183, 0.03798],
 [0.0135, 0.0322],
 [0.0094, 0.0265],
 [0.00604, 0.02092],
 [0.0034, 0.01548],
 [0.00152, 0.01016],
 [0.00038, 0.005],
 [0.0, 0.0],
 [0.00038, -0.00478],
 [0.00152, -0.00924],
 [0.0034, -0.01342],
 [0.00604, -0.0173],
 [0.0094, -0.02092],
 [0.0135, -0.02426],
 [0.0183, -0.02734],
 [0.02382, -0.0302],
 [0.03004, -0.03284],
 [0.03694, -0.03528],
 [0.04454, -0.03756],
 [0.05282, -0.03966],
 [0.06176, -0.04162],
 [0.07136, -0.04348],
 [0.0816, -0.04524],
 [0.0925, -0.04692],
 [0.10402, -0.04856],
 [0.11618, -0.05014],
 [0.12894, -0.05172],
 [0.14232, -0.0533],
 [0.15628, -0.05488],
 [0.17084, -0.05648],
 [0.18598, -0.05812],
 [0.20168, -0.05982],
 [0.21794, -0.06154],
 [0.23476, -0.06332],
 [0.2521, -0.06516],
 [0.26998, -0.06704],
 [0.2884, -0.06894],
 [0.3073, -0.07088],
 [0.32672, -0.0728],
 [0.34662, -0.07472],
 [0.367, -0.07662],
 [0.38786, -0.07842],
 [0.40916, -0.08014],
 [0.43092, -0.08172],
 [0.45312, -0.08316],
 [0.47574, -0.08446],
 [0.49876, -0.08564],
 [0.5222, -0.08668],
 [0.54602, -0.08758],
 [0.57022, -0.08836],
 [0.59478, -0.089],
 [0.61972, -0.0895],
 [0.64498, -0.08988],
 [0.67058, -0.09014],
 [0.69648, -0.09026],
 [0.7227, -0.09026],
 [0.7492, -0.09012],
 [0.77598, -0.08988],
 [0.80304, -0.08952],
 [0.83034, -0.08904],
 [0.85786, -0.08844],
 [0.88562, -0.08772],
 [0.91358, -0.08692],
 [0.94174, -0.086],
 [0.97006, -0.08498],
 [0.99854, -0.08386],
 [1.02718, -0.08264],
 [1.05594, -0.08134],
 [1.0848, -0.07994],
 [1.11378, -0.07846],
 [1.14282, -0.0769],
 [1.1719, -0.07526],
 [1.20104, -0.07354],
 [1.2302, -0.07174],
 [1.25936, -0.0699],
 [1.2885, -0.06796],
 [1.31758, -0.06598],
 [1.34662, -0.06394],
 [1.37556, -0.06184],
 [1.4044, -0.0597],
 [1.4331, -0.0575],
 [1.46164, -0.05526],
 [1.49, -0.05298],
 [1.51814, -0.05066],
 [1.54606, -0.04832],
 [1.5737, -0.04594],
 [1.60102, -0.04354],
 [1.62802, -0.04112],
 [1.65466, -0.03868],
 [1.68086, -0.03624],
 [1.70664, -0.0338],
 [1.73192, -0.03134],
 [1.75666, -0.0289],
 [1.78082, -0.02648],
 [1.80434, -0.0241],
 [1.82716, -0.02172],
 [1.84922, -0.0194],
 [1.87042, -0.01714],
 [1.89072, -0.01494],
 [1.90998, -0.01282],
 [1.92812, -0.0108],
 [1.94496, -0.0089],
 [1.96038, -0.00714],
 [1.9741, -0.00556],
 [1.98582, -0.00418],
 [1.99496, -0.00312],
 [2.0, -0.00252]]

# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
import mesh
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from connectorBehavior import *
import displayGroupMdbToolset as dgm

#unidades en SI: kg,m,s,Pa
condiciones= array([[0.00131, 0.00161],
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
   
velocidad_l= [ 0.,  5., 10., 15., 20., 25., 30., 35., 40., 45.]
def modelo_completo(indice):

    #Revestimiento
    envergadura= 0.6 #m
    espesor_revestimiento=condiciones[0][0] 
    espesor_larguerillo=condiciones[0][1] 
    posicion_larguero=32  #1->63
    angulo=velocidad_l[indice]
    
    espesor_costilla= 0.02 #m
    velocidad= 120 #ms-1
    celda_pajaro=0.01 #m
    celda_costilla=0.04
    celda_largueros=0.02
    celda_piel=0.04
    
    modelo='Model-'+str(indice)
    nombre_modelo='job_definitivo' + str(indice)
    
    
    
    nombre_revest='Piel'
    mdb.Model(name=modelo, modelType=STANDARD_EXPLICIT)
    mdb.models[modelo].ConstrainedSketch(name='__profile__', sheetSize=4.0)
    for i in range(0,len(coordenadas)):
        mdb.models[modelo].sketches['__profile__'].Spot(point=(coordenadas[i][0], coordenadas[i][1]))
    for i in range(0,len(coordenadas)-1):    
        mdb.models[modelo].sketches['__profile__'].Line(point1=(coordenadas[i][0], coordenadas[i][1]), 
        point2=(coordenadas[i+1][0], coordenadas[i+1][1]))
    
    mdb.models[modelo].sketches['__profile__'].Line(point1=(coordenadas[len(coordenadas)-1][0], -coordenadas[len(coordenadas)-1][1]), 
        point2=(coordenadas[len(coordenadas)-1]))
    
    
    mdb.models[modelo].Part(dimensionality=THREE_D, name=nombre_revest, type=
        DEFORMABLE_BODY)
    mdb.models[modelo].parts[nombre_revest].BaseShellExtrude(depth=envergadura, sketch=
        mdb.models[modelo].sketches['__profile__'])
    del mdb.models[modelo].sketches['__profile__']
    
    p = mdb.models[modelo].parts['Piel']
    s = p.features['Shell extrude-1'].sketch
    mdb.models[modelo].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s1 = mdb.models[modelo].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1, 
        upToFeature=p.features['Shell extrude-1'], filter=COPLANAR_EDGES)
    mdb.models[modelo].ConstrainedSketch(name='Sketch-perfil', objectToCopy=s1)
    s1.unsetPrimaryObject()
    del mdb.models[modelo].sketches['__edit__']
    p = mdb.models[modelo].parts['Piel']
    p.regenerate()
    
    
    
    #Costilla
    nombre_costilla= 'Costilla'
    
    mdb.models[modelo].ConstrainedSketch(name='__profile__', sheetSize=2.0)
    for i in range(0,len(coordenadas)):
        mdb.models[modelo].sketches['__profile__'].Spot(point=(coordenadas[i][0], coordenadas[i][1]))
    for i in range(0,len(coordenadas)-1):    
        mdb.models[modelo].sketches['__profile__'].Line(point1=(coordenadas[i][0], coordenadas[i][1]), 
        point2=(coordenadas[i+1][0], coordenadas[i+1][1]))
    
    mdb.models[modelo].sketches['__profile__'].Line(point1=(coordenadas[len(coordenadas)-1][0], -coordenadas[len(coordenadas)-1][1]), 
        point2=(coordenadas[len(coordenadas)-1]))
    
    
    mdb.models[modelo].Part(dimensionality=THREE_D, name=nombre_costilla, type=
        DEFORMABLE_BODY)
    mdb.models[modelo].parts['Costilla'].BaseSolidExtrude(depth=espesor_costilla, sketch=
        mdb.models[modelo].sketches['__profile__'])
    del mdb.models[modelo].sketches['__profile__']
    
    
    
    #Larguero
    mdb.models[modelo].ConstrainedSketch(name='__profile__', sheetSize=2.0)
    mdb.models[modelo].ConstrainedSketch(name='__profile__', sheetSize=2.0)
    s= mdb.models[modelo].sketches['__profile__']
    
    Largueros_frontal(posicion_larguero,modelo)
    
    Largueros_trasero(posicion_larguero,modelo)
    mdb.models[modelo].Part(dimensionality=THREE_D, name='Larguero', type=
        DEFORMABLE_BODY)
    mdb.models[modelo].parts['Larguero'].BaseSolidExtrude(depth=envergadura-2*espesor_costilla, sketch=
        mdb.models[modelo].sketches['__profile__'])
    del mdb.models[modelo].sketches['__profile__']
    
    #Pájaro
    nombre_pajaro= 'Bird'
    mdb.models[modelo].ConstrainedSketch(name='__profile__', sheetSize=200.0)
    mdb.models[modelo].sketches['__profile__'].ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
    mdb.models[modelo].sketches['__profile__'].Spot(point=(0.05, 0.0))
    mdb.models[modelo].sketches['__profile__'].Line(point1=(0.05, 0.0), point2=(0.05, -0.09))
    mdb.models[modelo].sketches['__profile__'].ArcByStartEndTangent(entity=mdb.models[modelo].sketches['__profile__'].geometry[3], point1=(0.05, -0.09), point2=(0.0, -0.14))
    mdb.models[modelo].sketches['__profile__'].Line(point1=(0.05, 0.0), point2=(0.05, 0.09))
    mdb.models[modelo].sketches['__profile__'].Spot(point=(0.0, 0.14))
    mdb.models[modelo].sketches['__profile__'].ArcByStartEndTangent(entity=mdb.models[modelo].sketches['__profile__'].geometry[5], point1=(0.05, 0.09), point2=(0.0, 0.14))
    mdb.models[modelo].sketches['__profile__'].Line(point1=(0.0, 0.14), point2=(0.0, -0.14))
    mdb.models[modelo].Part(dimensionality=THREE_D, name=nombre_pajaro, type=DEFORMABLE_BODY)
    mdb.models[modelo].parts['Bird'].BaseSolidRevolve(angle=360.0, flipRevolveDirection=OFF, sketch=mdb.models[modelo].sketches['__profile__'])
    del mdb.models[modelo].sketches['__profile__']
    
    nombre_partes=[nombre_revest,nombre_pajaro]
    
    #materiales
    densidad_AL7075=2780
    E_AL7075= 7e10
    v_AL7075= 0.3
    mdb.models[modelo].Material(name='bird')
    mdb.models[modelo].materials['bird'].Density(table=((942.7, ), ))
    mdb.models[modelo].materials['bird'].Eos(table=((1480.0, 0.17, 0.0), ), type=USUP)
    mdb.models[modelo].materials['bird'].Viscosity(table=((1.0, ), ))
    
    
    mdb.models[modelo].Material(name='Al-2024')
    mdb.models[modelo].materials['Al-2024'].Density(table=((densidad_AL7075, ), ))
    mdb.models[modelo].materials['Al-2024'].Elastic(table=((E_AL7075, v_AL7075), ))
    mdb.models[modelo].materials['Al-2024'].Plastic(table=((320000000.0, 0.0), (
        338000000.0, 0.012), (381000000.0, 0.02), (419000000.0, 0.032), (
        440000000.0, 0.04), (450000000.0, 0.052), (460000000.0, 0.06), (
        475000000.0, 0.072), (480000000.0, 0.08), (495000000.0, 0.092), (
        499000000.0, 0.1), (505000000.0, 0.112), (511000000.0, 0.12), (517000000.0, 
        0.132), (525000000.0, 0.14), (532000000.0, 0.152), (539000000.0, 0.16), (
        545000000.0, 0.172), (551000000.0, 0.18)))
    mdb.models[modelo].materials['Al-2024'].DuctileDamageInitiation(table=((
        0.18, 0.0, 0.0), ))
    mdb.models[modelo].materials['Al-2024'].ductileDamageInitiation.DamageEvolution(
        table=((0.02, ), ), type=DISPLACEMENT)
    p = mdb.models[modelo].parts['Piel']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models[modelo].materials['Al-2024'].ductileDamageInitiation
    mdb.models[modelo].materials['Al-2024'].plastic.setValues(
        hardening=JOHNSON_COOK, table=((369000000.0, 684000000.0, 0.73, 1.7, 800.0, 
        650.0), ))
    mdb.models[modelo].materials['Al-2024'].JohnsonCookDamageInitiation(table=((
        0.13, 0.13, -1.5, 0.011, 0.0, 800.0, 650.0, 0.0005), ))
    mdb.models[modelo].materials['Al-2024'].johnsonCookDamageInitiation.DamageEvolution(
        type=ENERGY, table=((0, ), ))
    
    mdb.models[modelo].materials['Al-2024'].plastic.RateDependent(table=((
        0.0083, 1.0), ), type=JOHNSON_COOK)
    
    
    
    mdb.models[modelo].Material(name='Al-7075-T6', 
        objectToCopy=mdb.models[modelo].materials['Al-2024'])
    mdb.models[modelo].materials['Al-7075-T6'].johnsonCookDamageInitiation.setValues(
        table=((-0.068, 0.451, -0.952, 0.036, 0.697, 800.0, 650.0, 0.0005), ))
    mdb.models[modelo].materials['Al-7075-T6'].johnsonCookDamageInitiation.damageEvolution.setValues(
        type=ENERGY)
    mdb.models[modelo].materials['Al-7075-T6'].plastic.setValues(table=((
        546000000.0, 678000000.0, 0.71, 1.56, 800.0, 650.0), ))
    mdb.models[modelo].materials['Al-7075-T6'].plastic.rateDependent.setValues(
        table=((0.024, 1.0), ))
    
    
    
    
    
    #Section
    
    
    mdb.models[modelo].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
        integrationRule=SIMPSON, material='Al-2024', name='Section-revestimiento', 
        nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
        preIntegrate=OFF, temperature=GRADIENT, thickness=espesor_revestimiento, thicknessField='', 
        thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
    
    mdb.models[modelo].HomogeneousSolidSection(material='bird', name=
        'Section-bird', thickness=None)
    mdb.models[modelo].HomogeneousSolidSection(material='Al-7075-T6', name=
        'Section-costilla', thickness=None)
    
    
    #Assigns sections
    
    
    p = mdb.models[modelo].parts['Piel']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Piel']
    
    
    f=p.faces
    faces=f.getByBoundingBox(-2,-1,-envergadura*2,2,1,envergadura*2)
    
    region = p.Set(faces=faces, name='Set-3')
    p = mdb.models[modelo].parts['Piel']
    p.SectionAssignment(region=region, sectionName='Section-revestimiento', 
        offset=0.0, offsetType=TOP_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models[modelo].parts['Costilla']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Costilla']
    c = p.cells
    cells = c.findAt(((1.991913, -0.003473, 0.066667*espesor_costilla/0.1), ))
    
    region = p.Set(cells=cells, name='Set-3')
    p = mdb.models[modelo].parts['Costilla']
    p.SectionAssignment(region=region, sectionName='Section-costilla', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    
    
    
    
    
    p = mdb.models[modelo].parts['Bird']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Bird']
    c = p.cells
    cells = c.findAt(((0.030393, 0.128111, -0.011126), ))
    region = p.Set(cells=cells, name='Set-4')
    p = mdb.models[modelo].parts['Bird']
    p.SectionAssignment(region=region, sectionName='Section-bird', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    
    
    p = mdb.models[modelo].parts['Larguero']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Larguero']
    c = p.cells
    cells=c.getByBoundingBox(-2,-1,-envergadura*2,2,1,envergadura*2)
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models[modelo].parts['Larguero']
    p.SectionAssignment(region=region, sectionName='Section-costilla', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    
    
    #Stringers
    cst=0.5
    espesor_st=0.001
    p = mdb.models[modelo].parts['Piel']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models[modelo].ArbitraryProfile(name='Profile-omega', table=((-0.0425*cst, 
        0.0), (-0.0275*cst, 0.0, espesor_st), (-0.01018*cst, 0.03*cst, espesor_st), (0.01018*cst, 0.03*cst, 
        espesor_st), (0.0275*cst, 0.0, espesor_st), (0.0425*cst, 0.0, espesor_st)))                                                         
    mdb.models[modelo].BeamSection(name='Section-stringer', 
        integration=DURING_ANALYSIS, poissonRatio=0.0, profile='Profile-omega', 
        material='Al-2024', temperatureVar=LINEAR, consistentMassMatrix=False)
    
    
    
    
    mdb.models[modelo].ArbitraryProfile(name='Profile-Z', table=((-0.0105, 0.0), 
        (0.0, 0.0, espesor_larguerillo*0.68), (0.0, 0.026, espesor_larguerillo), (0.0105, 0.026, espesor_larguerillo*0.68)))
    
    def crear_stringer(x,y,nombre,x1,y1):                                                      
        p = mdb.models[modelo].parts['Piel']
        e = p.edges
        edges = e.findAt(((x, y, 0.5*envergadura*0.5), ))
        p.Stringer(edges=edges, name=nombre)
        p = mdb.models[modelo].parts['Piel']
        e = p.edges
        edges = e.findAt(((x, y, 0.5*envergadura*0.5), ))
        region=p.Set(stringerEdges=((nombre, edges), ), name='Set-'+nombre)
        p = mdb.models[modelo].parts['Piel']
        vector=[x1-x,y1-y]
        if (y < 0):
            p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(vector[0], vector[1], 
                0))
        else:
            p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(-vector[0], -vector[1], 
                0))
        region = p.sets['Set-'+nombre]
        p.SectionAssignment(region=region, sectionName='Section-stringer', offset=0.0, 
            offsetType=TOP_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION) 
        
        
    
        
        
        
    crear_stringer(0.20168, -0.05982, 'Stringer1',0.21794, -0.06154)
    crear_stringer(0.20168, 0.12806, 'Stringer2',0.21794, 0.13156 )
    crear_stringer(0.3073, -0.07088, 'Stringer3',0.32672, -0.0728)
    crear_stringer(0.3073, 0.1444, 'Stringer4',0.32672, 0.14608 )
    crear_stringer(0.40916, 0.1504, 'Stringer5',0.43092, 0.15102  )
    crear_stringer(0.40916, -0.08014, 'Stringer6',0.43092, -0.08172  )
    
    crear_stringer(0.59478, -0.089, 'Stringer7',0.61972, -0.0895  )
    crear_stringer(0.59478, 0.15106, 'Stringer8',0.61972, 0.15048  )
    
    crear_stringer(0.69648, 0.14782, 'Stringer9',0.7227, 0.14666)
    crear_stringer(0.69648, -0.09026, 'Stringer10',0.7227, -0.09026)
    crear_stringer(0.80304, 0.14238, 'Stringer11',0.83034, 0.1407)
    crear_stringer(0.80304, -0.08952, 'Stringer12',0.83034, -0.08904)
    crear_stringer(0.91358, -0.08692, 'Stringer13',0.94174, -0.086)
    crear_stringer(0.91358, 0.1349, 'Stringer14',0.94174, 0.13274)
    crear_stringer(0.99854, -0.08386, 'Stringer15',1.02718, -0.08264  )
    crear_stringer(0.99854, 0.12808, 'Stringer16',1.02718, 0.1256  )
    
    crear_stringer(1.0848, -0.07994, 'Stringer17',1.11378, -0.07846 )
    crear_stringer(1.0848, 0.12036, 'Stringer18',1.11378, 0.1176  )
    
    crear_stringer(1.20104, -0.07354, 'Stringer19',1.2302, -0.07174  )
    crear_stringer(1.20104, 0.10882, 'Stringer20',1.2302, 0.10574  )
    
    
    
    crear_stringer(1.31758, 0.09612, 'Stringer21',1.34662, 0.0928)
    crear_stringer(1.31758, -0.06598, 'Stringer22',1.34662, -0.06394)
    
    crear_stringer(1.4044, -0.0597, 'Stringer23',1.4331, -0.0575 )
    crear_stringer(1.4044, 0.086, 'Stringer24',1.4331, 0.08254  )
    
    
    mdb.models[modelo].LProfile(name='Profile-2', a=0.005, b=0.01, t1=0.001, 
        t2=0.001)
    mdb.models[modelo].sections['Section-stringer'].setValues(poissonRatio=0.0, 
        profile='Profile-Z')
    
    
    
    
    
    
    #Assembly
    mdb.models[modelo].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models[modelo].rootAssembly.Instance(dependent=ON, name='Piel-1', part=
        mdb.models[modelo].parts['Piel'])
    mdb.models[modelo].rootAssembly.Instance(dependent=ON, name='Bird-1', 
        part=mdb.models[modelo].parts['Bird'])
    a1 = mdb.models[modelo].rootAssembly
    p = mdb.models[modelo].parts['Costilla']
    a1.Instance(name='Costilla-2', part=p, dependent=ON)
    p = mdb.models[modelo].parts['Larguero']
    a1.Instance(name='Larguero-1', part=p, dependent=ON)
    
    
    #Translate bird
    mdb.models[modelo].rootAssembly.translate(instanceList=('Bird-1', ), vector=
        (0.0, 0.0, 1.0*envergadura*0.5))
    mdb.models[modelo].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 0.0, 
        1.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Bird-1', ))
    mdb.models[modelo].rootAssembly.translate(instanceList=('Bird-1', ), vector=
        (-0.2, 0.0, 0.0))
    a1 = mdb.models[modelo].rootAssembly
    a1.translate(instanceList=('Bird-1', ), vector=(0.045, 0.0, 0.0))
    a1.rotate(instanceList=('Bird-1', ), axisPoint=(-0.065, -0.05, 0.331), 
    axisDirection=(0.0, 0.1, 0.0), angle=angulo)
    
    
    a1 = mdb.models[modelo].rootAssembly
    a1.LinearInstancePattern(instanceList=('Costilla-2', ), direction1=(1.0, 0.0, 
        0.0), direction2=(0.0, 0.0, envergadura), number1=1, number2=2, spacing1=2.0, 
        spacing2=envergadura-espesor_costilla)
    a1 = mdb.models[modelo].rootAssembly
    a1.translate(instanceList=('Larguero-1', ), vector=(0.0, 0.0, espesor_costilla))
    
    #Steps
    step_inicial=0.0005
    step_periodo=0.0045
    mdb.models[modelo].ExplicitDynamicsStep(improvedDtMethod=ON, name=
        'Initial-vel', previous='Initial', timePeriod=step_inicial)
    mdb.models[modelo].ExplicitDynamicsStep(improvedDtMethod=ON, name='Impact', 
        previous='Initial-vel', timePeriod=step_periodo)
    
    
    
    
    #Condiciones de contorno
    
    a = mdb.models[modelo].rootAssembly
    region = a.instances['Bird-1'].sets['Set-4']
    mdb.models[modelo].Velocity(name='Predefined Field-1', region=region, 
        field='', distributionType=MAGNITUDE, velocity1=velocidad, velocity2=0.0, 
        velocity3=0.0, omega=0.0)
    
    a = mdb.models[modelo].rootAssembly
    f1 = a.instances['Costilla-2-lin-1-2'].faces
    faces1 = f1.findAt(((1.99832, -0.00104, envergadura), ))
    f2 = a.instances['Piel-1'].faces
    faces2 = f2.findAt(((2.0, -0.00084, 0.666667*envergadura), ))
    f3 = a.instances['Costilla-2'].faces
    faces3 = f3.findAt(((1.99832, -0.00104, 0.0), ))
    region = a.Set(faces=faces1+faces2+faces3, name='Set-12')
    mdb.models[modelo].EncastreBC(name='BC-2', createStepName='Initial', 
        region=region, localCsys=None)
    
    
    
    
    #Interaction
    mdb.models[modelo].ContactProperty('IntProp-1')
    mdb.models[modelo].interactionProperties['IntProp-1'].TangentialBehavior(
        dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
        formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
        pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
        table=((0.3, ), ), temperatureDependency=OFF)
    mdb.models[modelo].ContactExp(createStepName='Initial-vel', name='Int-1')
    mdb.models[modelo].interactions['Int-1'].includedPairs.setValuesInStep(
        stepName='Initial-vel', useAllstar=ON)
    mdb.models[modelo].interactions['Int-1'].contactPropertyAssignments.appendInStep(
        assignments=((GLOBAL, SELF, 'IntProp-1'), ), stepName='Initial-vel')
    mdb.models[modelo].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    
    #Constraints
    slave1=contacto_Largueros_frontal(posicion_larguero)
    slave2=contacto_Largueros_trasero(posicion_larguero)
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Costilla-2'].faces
    side1Faces1 = s1.findAt(((1.99832, -0.00104, espesor_costilla), ))
    region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-1')
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Larguero-1'].faces
    side1Faces1 = s1.findAt(((slave2[0][0], slave2[0][1], espesor_costilla), ), ((slave1[0][0], slave1[0][1], 
        espesor_costilla), ))
    region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
    mdb.models[modelo].Tie(name='Constraint-1', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
    
    
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Costilla-2-lin-1-2'].faces
    side1Faces1 = s1.findAt(((1.99832, -0.00104, envergadura-espesor_costilla), ))
    region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-3')
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Larguero-1'].faces
    side1Faces1 = s1.findAt(((slave2[0][0], slave2[0][1], envergadura-espesor_costilla), ), ((slave1[0][0], slave1[0][1], 
        envergadura-espesor_costilla), ))
    region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-3')
    mdb.models[modelo].Tie(name='Constraint-2', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
    
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Costilla-2'].faces
    side1Faces1=s1[0:len(s1)-2]
    a.Surface(side1Faces=side1Faces1, name='Surf-5')
    
    
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Costilla-2-lin-1-2'].faces
    side1Faces1=s1[0:len(s1)-2]
    a.Surface(side1Faces=side1Faces1, name='Surf-6')
    
    
   
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Piel-1'].faces
    side1Faces1=s1[0:len(s1)]
    
    a.Surface(side1Faces=side1Faces1, name='Surf-piel')
    #: The surface 'Surf-piel' has been created (199 faces).
    a = mdb.models[modelo].rootAssembly
    region1=a.surfaces['Surf-5']
    a = mdb.models[modelo].rootAssembly
    region2=a.surfaces['Surf-piel']
    mdb.models[modelo].Tie(name='Constraint-3', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
    a = mdb.models[modelo].rootAssembly
    region1=a.surfaces['Surf-6']
    a = mdb.models[modelo].rootAssembly
    region2=a.surfaces['Surf-piel']
    mdb.models[modelo].Tie(name='Constraint-4', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
    
    
    slave3=contacto_top_Largueros_frontal(posicion_larguero)
    slave4=contacto_top_Largueros_trasero(posicion_larguero)
    
    a = mdb.models[modelo].rootAssembly
    s1 = a.instances['Larguero-1'].faces
    side1Faces1 = s1.findAt(((s1[8].getCentroid()[0]), ), ((s1[6].getCentroid()[0]), ), ((s1[0].getCentroid()[0]), ), ((s1[2].getCentroid()[0]), ))
    region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-10')
    a = mdb.models[modelo].rootAssembly
    region1=a.surfaces['m_Surf-10']
    a = mdb.models[modelo].rootAssembly
    region2=a.surfaces['Surf-piel']
    mdb.models[modelo].Tie(name='Constraint-6', master=region1, slave=region2, 
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
    
    mdb.models[modelo].constraints['Constraint-1'].setValues(
        constraintEnforcement=NODE_TO_SURFACE)
    mdb.models[modelo].constraints['Constraint-2'].setValues(
        constraintEnforcement=NODE_TO_SURFACE)
    mdb.models[modelo].constraints['Constraint-3'].setValues(
        constraintEnforcement=NODE_TO_SURFACE)
    mdb.models[modelo].constraints['Constraint-4'].setValues(
        constraintEnforcement=NODE_TO_SURFACE)
    mdb.models[modelo].constraints['Constraint-6'].setValues(
        constraintEnforcement=NODE_TO_SURFACE)
    
    mdb.models[modelo].constraints['Constraint-3'].swapSurfaces()
    mdb.models[modelo].constraints['Constraint-4'].swapSurfaces()
    mdb.models[modelo].constraints['Constraint-6'].swapSurfaces()
    
    
    
    
    #Mesh
    
    mdb.models[modelo].parts['Bird'].setMeshControls(elemShape=TET, regions=
        mdb.models[modelo].parts['Bird'].cells.getSequenceFromMask(('[#1 ]', ), 
        ), technique=FREE)
    mdb.models[modelo].parts['Bird'].setElementType(elemTypes=(ElemType(
        elemCode=C3D8R, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, 
        kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
        distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=EXPLICIT), 
        ElemType(elemCode=C3D4, elemLibrary=EXPLICIT, secondOrderAccuracy=OFF, 
        distortionControl=DEFAULT, particleConversion=TIME, 
        particleConversionThreshold=0, particleConversionPPD=1, 
        particleConversionKernel=CUBIC)), regions=(
        mdb.models[modelo].parts['Bird'].cells.getSequenceFromMask(('[#1 ]', ), 
        ), ))
    mdb.models[modelo].parts['Bird'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=celda_pajaro)
    mdb.models[modelo].parts['Bird'].generateMesh()
    
    mdb.models[modelo].parts['Piel'].seedPart(deviationFactor=0.1, 
        minSizeFactor=0.1, size=celda_piel)
    mdb.models[modelo].parts['Piel'].generateMesh()
    mdb.models[modelo].rootAssembly.regenerate()
    
    
    
    
    
    p = mdb.models[modelo].parts['Piel']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = ElemType(elemCode=S4R, elemLibrary=EXPLICIT, 
        secondOrderAccuracy=OFF, hourglassControl=ENHANCED, elemDeletion=ON, 
        maxDegradation=0.95)
    elemType2 = ElemType(elemCode=S3R, elemLibrary=EXPLICIT)
    p = mdb.models[modelo].parts['Piel']
    f=p.faces
    faces=f.getByBoundingBox(-2,-1,-envergadura*2,2,1,envergadura*2)
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    
    p = mdb.models[modelo].parts['Piel']
    elemType1 = mesh.ElemType(elemCode=B31, elemLibrary=EXPLICIT)
    p = mdb.models[modelo].parts['Piel']
    pickedRegions = p.sets['Set-Stringer1']
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    elemType1 = mesh.ElemType(elemCode=B31, elemLibrary=EXPLICIT)
    p = mdb.models[modelo].parts['Piel']
    pickedRegions = p.sets['Set-Stringer2']
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    elemType1 = mesh.ElemType(elemCode=B31, elemLibrary=EXPLICIT)
    p = mdb.models[modelo].parts['Piel']
    pickedRegions = p.sets['Set-Stringer3']
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    
    def element_type_stringer(name):
        p = mdb.models[modelo].parts['Piel']
        pickedRegions = p.sets['Set-'+name]
        p.setElementType(regions=pickedRegions, elemTypes=(elemType1, ))
    element_type_stringer('Stringer4')
    element_type_stringer('Stringer5')
    element_type_stringer('Stringer6')
    element_type_stringer('Stringer7')
    element_type_stringer('Stringer8')
    element_type_stringer('Stringer9')
    element_type_stringer('Stringer10')
    element_type_stringer('Stringer11')
    element_type_stringer('Stringer12')
    element_type_stringer('Stringer13')
    element_type_stringer('Stringer14')
    element_type_stringer('Stringer15')
    element_type_stringer('Stringer16')
    element_type_stringer('Stringer17')
    element_type_stringer('Stringer18')
    element_type_stringer('Stringer19')
    element_type_stringer('Stringer20')
    element_type_stringer('Stringer21')
    element_type_stringer('Stringer22')
    element_type_stringer('Stringer23')
    element_type_stringer('Stringer24')
    
    
    
    
    p = mdb.models[modelo].parts['Costilla']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Costilla']
    p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Costilla']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Costilla']
    p.generateMesh()
    p = mdb.models[modelo].parts['Costilla']
    p.deleteMesh()
    p = mdb.models[modelo].parts['Costilla']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Costilla']
    p.seedPart(size=0.07, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Costilla']
    p.generateMesh()
    p = mdb.models[modelo].parts['Costilla']
    p.deleteMesh()
    p = mdb.models[modelo].parts['Costilla']
    p.seedPart(size=celda_costilla, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Costilla']
    p.generateMesh()
    p = mdb.models[modelo].parts['Larguero']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models[modelo].parts['Larguero']
    p.seedPart(size=celda_largueros, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models[modelo].parts['Larguero']
    p.generateMesh()
    
    
    
    
    
    
    
    #Field output request
    mdb.models[modelo].FieldOutputRequest(createStepName='Impact', name='F-Output-2', variables=('SDEG', 'STATUS'))
    
    
    #Refinamiento borde de ataque
    
    mdb.models[modelo].parts['Piel'].DatumPlaneByPrincipalPlane(offset=0.20168, 
        principalPlane=YZPLANE)
    mdb.models[modelo].parts['Costilla'].DatumPlaneByPrincipalPlane(offset=
        0.20168, principalPlane=YZPLANE)
    mdb.models[modelo].parts['Costilla'].deleteMesh(regions=
        mdb.models[modelo].parts['Costilla'].cells.findAt(((1.991913, -0.003473, 
        0.013333), )))
    mdb.models[modelo].parts['Costilla'].PartitionCellByDatumPlane(cells=
        mdb.models[modelo].parts['Costilla'].cells.findAt(((1.991913, -0.003473, 
        0.013333), )), datumPlane=
        mdb.models[modelo].parts['Costilla'].datums[8])
    mdb.models[modelo].parts['Piel'].Set(faces=
        mdb.models[modelo].parts['Piel'].faces.findAt(((0.180933, 0.12292, 
        0.333333*envergadura/0.5), ), ((0.165987, 0.118747, 0.333333*envergadura/0.5), ), ((0.151627, 0.114307, 
        0.333333*envergadura/0.5), ), ((0.13786, 0.10962, 0.333333*envergadura/0.5), ), ((0.124687, 0.104693, 
        0.333333*envergadura/0.5), ), ((0.112127, 0.09956, 0.333333*envergadura/0.5), ), ((0.10018, 0.094227, 
        0.333333*envergadura/0.5), ), ((0.088867, 0.088733, 0.333333*envergadura/0.5), ), ((0.078187, 0.083093, 
        0.333333*envergadura/0.5), ), ((0.06816, 0.07734, 0.333333*envergadura/0.5), ), ((0.05878, 0.0715, 
        0.333333*envergadura/0.5), ), ((0.05006, 0.0656, 0.333333*envergadura/0.5), ), ((0.042007, 0.05966, 
        0.333333*envergadura/0.5), ), ((0.03464, 0.053713, 0.333333*envergadura/0.5), ), ((0.027967, 0.047773, 
        0.333333*envergadura/0.5), ), ((0.02198, 0.041887, 0.333333*envergadura/0.5), ), ((0.0167, 0.036053, 
        0.333333*envergadura/0.5), ), ((0.012133, 0.0303, 0.333333*envergadura/0.5), ), ((0.00828, 0.02464, 
        0.333333*envergadura/0.5), ), ((0.00516, 0.019107, 0.333333*envergadura/0.5), ), ((0.002773, 0.013707, 
        0.333333*envergadura/0.5), ), ((0.00114, 0.00844, 0.333333*envergadura/0.5), ), ((0.000253, 0.003333, 
        0.333333*envergadura/0.5), ), ((0.000127, -0.001593, 0.333333*envergadura/0.5), ), ((0.00076, -0.006267, 
        0.333333*envergadura/0.5), ), ((0.002147, -0.010633, 0.333333*envergadura/0.5), ), ((0.00428, -0.014713, 
        0.333333*envergadura/0.5), ), ((0.00716, -0.018507, 0.333333*envergadura/0.5), ), ((0.010767, -0.022033, 
        0.333333*envergadura/0.5), ), ((0.0151, -0.025287, 0.333333*envergadura/0.5), ), ((0.02014, -0.028293, 
        0.333333*envergadura/0.5), ), ((0.025893, -0.03108, 0.333333*envergadura/0.5), ), ((0.03234, -0.033653, 
        0.333333*envergadura/0.5), ), ((0.039473, -0.03604, 0.333333*envergadura/0.5), ), ((0.0473, -0.03826, 
        0.333333*envergadura/0.5), ), ((0.0558, -0.040313, 0.333333*envergadura/0.5), ), ((0.06496, -0.04224, 
        0.333333*envergadura/0.5), ), ((0.074773, -0.044067, 0.333333*envergadura/0.5), ), ((0.085233, -0.0458, 
        0.333333*envergadura/0.5), ), ((0.09634, -0.047467, 0.333333*envergadura/0.5), ), ((0.108073, -0.049087, 
        0.333333*envergadura/0.5), ), ((0.120433, -0.050667, 0.333333*envergadura/0.5), ), ((0.1334, -0.052247, 
        0.333333*envergadura/0.5), ), ((0.146973, -0.053827, 0.333333*envergadura/0.5), ), ((0.161133, -0.055413, 
        0.333333*envergadura/0.5), ), ((0.175887, -0.057027, 0.333333*envergadura/0.5), ), ), name='Set-imacttttt')
    mdb.models[modelo].parts['Piel'].deleteMesh(regions=
        mdb.models[modelo].parts['Piel'].faces.findAt(((0.180933, 0.12292, 
        0.333333*envergadura/0.5), ), ((0.165987, 0.118747, 0.333333*envergadura/0.5), ), ((0.196447, 0.1268, 
        0.333333*envergadura/0.5), ), ((0.151627, 0.114307, 0.333333*envergadura/0.5), ), ((0.13786, 0.10962, 
        0.333333*envergadura/0.5), ), ((0.124687, 0.104693, 0.333333*envergadura/0.5), ), ((0.112127, 0.09956, 
        0.333333*envergadura/0.5), ), ((0.10018, 0.094227, 0.333333*envergadura/0.5), ), ((0.088867, 0.088733, 
        0.333333*envergadura/0.5), ), ((0.078187, 0.083093, 0.333333*envergadura/0.5), ), ((0.06816, 0.07734, 
        0.333333*envergadura/0.5), ), ((0.05878, 0.0715, 0.333333*envergadura/0.5), ), ((0.05006, 0.0656, 
        0.333333*envergadura/0.5), ), ((0.042007, 0.05966, 0.333333*envergadura/0.5), ), ((0.03464, 0.053713, 
        0.333333*envergadura/0.5), ), ((0.027967, 0.047773, 0.333333*envergadura/0.5), ), ((0.02198, 0.041887, 
        0.333333*envergadura/0.5), ), ((0.0167, 0.036053, 0.333333*envergadura/0.5), ), ((0.012133, 0.0303, 
        0.333333*envergadura/0.5), ), ((0.00828, 0.02464, 0.333333*envergadura/0.5), ), ((0.00516, 0.019107, 
        0.333333*envergadura/0.5), ), ((0.002773, 0.013707, 0.333333*envergadura/0.5), ), ((0.00114, 0.00844, 
        0.333333*envergadura/0.5), ), ((0.000253, 0.003333, 0.333333*envergadura/0.5), ), ((0.000127, -0.001593, 
        0.333333*envergadura/0.5), ), ((0.00076, -0.006267, 0.333333*envergadura/0.5), ), ((0.002147, -0.010633, 
        0.333333*envergadura/0.5), ), ((0.00428, -0.014713, 0.333333*envergadura/0.5), ), ((0.00716, -0.018507, 
        0.333333*envergadura/0.5), ), ((0.010767, -0.022033, 0.333333*envergadura/0.5), ), ((0.0151, -0.025287, 
        0.333333*envergadura/0.5), ), ((0.02014, -0.028293, 0.333333*envergadura/0.5), ), ((0.025893, -0.03108, 
        0.333333*envergadura/0.5), ), ((0.03234, -0.033653, 0.333333*envergadura/0.5), ), ((0.039473, -0.03604, 
        0.333333*envergadura/0.5), ), ((0.0473, -0.03826, 0.333333*envergadura/0.5), ), ((0.0558, -0.040313, 
        0.333333*envergadura/0.5), ), ((0.06496, -0.04224, 0.333333*envergadura/0.5), ), ((0.074773, -0.044067, 
        0.333333*envergadura/0.5), ), ((0.085233, -0.0458, 0.333333*envergadura/0.5), ), ((0.09634, -0.047467, 
        0.333333*envergadura/0.5), ), ((0.108073, -0.049087, 0.333333*envergadura/0.5), ), ((0.120433, -0.050667, 
        0.333333*envergadura/0.5), ), ((0.1334, -0.052247, 0.333333*envergadura/0.5), ), ((0.146973, -0.053827, 
        0.333333*envergadura/0.5), ), ((0.161133, -0.055413, 0.333333*envergadura/0.5), ), ((0.175887, -0.057027, 
        0.333333*envergadura/0.5), ), ((0.191213, -0.058687, 0.333333*envergadura/0.5), ), ))
    mdb.models[modelo].parts['Piel'].seedEdgeBySize(constraint=FINER, 
        deviationFactor=0.1, edges=
        mdb.models[modelo].parts['Piel'].edges.findAt(((0.182195, 0.12326, 0.5*envergadura/0.5), 
        ), ((0.17084, 0.1202, 0.125*envergadura/0.5), ), ((0.182195, 0.12326, 0.0*envergadura/0.5), ), ((0.18598, 
        0.12428, 0.125*envergadura/0.5), ), ((0.1672, 0.11911, 0.5*envergadura/0.5), ), ((0.15628, 0.11584, 0.125*envergadura/0.5), 
        ), ((0.1672, 0.11911, 0.0*envergadura/0.5), ), ((0.15279, 0.11469, 0.5*envergadura/0.5), ), ((0.14232, 
        0.11124, 0.125*envergadura/0.5), ), ((0.15279, 0.11469, 0.0*envergadura/0.5), ), ((0.138975, 0.110025, 
        0.5*envergadura/0.5), ), ((0.12894, 0.10638, 0.125*envergadura/0.5), ), ((0.138975, 0.110025, 0.0*envergadura/0.5), ), ((
        0.12575, 0.105115, 0.5*envergadura/0.5), ), ((0.11618, 0.10132, 0.125*envergadura/0.5), ), ((0.12575, 
        0.105115, 0.0*envergadura/0.5), ), ((0.11314, 0.1, 0.5*envergadura/0.5), ), ((0.10402, 0.09604, 0.125*envergadura/0.5), ), 
        ((0.11314, 0.1, 0.0*envergadura/0.5), ), ((0.10114, 0.09468, 0.5*envergadura/0.5), ), ((0.0925, 0.0906, 
        0.125*envergadura/0.5), ), ((0.10114, 0.09468, 0.0*envergadura/0.5), ), ((0.089775, 0.0892, 0.5*envergadura/0.5), ), ((
        0.0816, 0.085, 0.125*envergadura/0.5), ), ((0.089775, 0.0892, 0.0*envergadura/0.5), ), ((0.07904, 0.08357, 
        0.5*envergadura/0.5), ), ((0.07136, 0.07928, 0.125*envergadura/0.5), ), ((0.07904, 0.08357, 0.0*envergadura/0.5), ), ((
        0.06896, 0.077825, 0.5*envergadura/0.5), ), ((0.06176, 0.07346, 0.125*envergadura/0.5), ), ((0.06896, 
        0.077825, 0.0*envergadura/0.5), ), ((0.059525, 0.07199, 0.5*envergadura/0.5), ), ((0.05282, 0.06758, 
        0.125*envergadura/0.5), ), ((0.059525, 0.07199, 0.0*envergadura/0.5), ), ((0.05075, 0.066095, 0.5*envergadura/0.5), ), ((
        0.04454, 0.06164, 0.125*envergadura/0.5), ), ((0.05075, 0.066095, 0.0*envergadura/0.5), ), ((0.04264, 
        0.060155, 0.5*envergadura/0.5), ), ((0.03694, 0.0557, 0.125*envergadura/0.5), ), ((0.04264, 0.060155, 0.0*envergadura/0.5), 
        ), ((0.035215, 0.05421, 0.5*envergadura/0.5), ), ((0.03004, 0.04974, 0.125*envergadura/0.5), ), ((0.035215, 
        0.05421, 0.0), ), ((0.028485, 0.048265, 0.5*envergadura/0.5), ), ((0.02382, 0.04384, 
        0.125*envergadura/0.5), ), ((0.028485, 0.048265, 0.0), ), ((0.02244, 0.042375, 0.5*envergadura/0.5), ), ((
        0.0183, 0.03798, 0.125*envergadura/0.5), ), ((0.02244, 0.042375, 0.0), ), ((0.0171, 
        0.036535, 0.5*envergadura/0.5), ), ((0.0135, 0.0322, 0.125*envergadura/0.5), ), ((0.0171, 0.036535, 0.0), 
        ), ((0.012475, 0.030775, 0.5*envergadura/0.5), ), ((0.0094, 0.0265, 0.125*envergadura/0.5), ), ((0.012475, 
        0.030775, 0.0), ), ((0.00856, 0.025105, 0.5*envergadura/0.5), ), ((0.00604, 0.02092, 
        0.125*envergadura/0.5), ), ((0.00856, 0.025105, 0.0), ), ((0.00538, 0.01956, 0.5*envergadura/0.5), ), ((
        0.0034, 0.01548, 0.125*envergadura/0.5), ), ((0.00538, 0.01956, 0.0), ), ((0.00293, 
        0.01415, 0.5*envergadura/0.5), ), ((0.00152, 0.01016, 0.125*envergadura/0.5), ), ((0.00293, 0.01415, 0.0), 
        ), ((0.001235, 0.00887, 0.5*envergadura/0.5), ), ((0.00038, 0.005, 0.125*envergadura/0.5), ), ((0.001235, 
        0.00887, 0.0), ), ((0.000285, 0.00375, 0.5*envergadura/0.5), ), ((0.0, 0.0, 0.125*envergadura/0.5), ), ((
        0.000285, 0.00375, 0.0), ), ((9.5e-05, -0.001195, 0.5*envergadura/0.5), ), ((0.00038, 
        -0.00478, 0.125*envergadura/0.5), ), ((9.5e-05, -0.001195, 0.0), ), ((0.000665, -0.005895, 
        0.5*envergadura/0.5), ), ((0.00152, -0.00924, 0.125*envergadura/0.5), ), ((0.000665, -0.005895, 0.0), ), ((
        0.00199, -0.010285, 0.5*envergadura/0.5), ), ((0.0034, -0.01342, 0.125*envergadura/0.5), ), ((0.00199, 
        -0.010285, 0.0), ), ((0.00406, -0.01439, 0.5*envergadura/0.5), ), ((0.00604, -0.0173, 
        0.125*envergadura/0.5), ), ((0.00406, -0.01439, 0.0), ), ((0.00688, -0.018205, 0.5*envergadura/0.5), ), ((
        0.0094, -0.02092, 0.125*envergadura/0.5), ), ((0.00688, -0.018205, 0.0), ), ((0.010425, 
        -0.021755, 0.5*envergadura/0.5), ), ((0.0135, -0.02426, 0.125*envergadura/0.5), ), ((0.010425, -0.021755, 
        0.0), ), ((0.0147, -0.02503, 0.5*envergadura/0.5), ), ((0.0183, -0.02734, 0.125*envergadura/0.5), ), ((
        0.0147, -0.02503, 0.0), ), ((0.01968, -0.028055, 0.5*envergadura/0.5), ), ((0.02382, 
        -0.0302, 0.125*envergadura/0.5), ), ((0.01968, -0.028055, 0.0), ), ((0.025375, -0.03086, 
        0.5*envergadura/0.5), ), ((0.03004, -0.03284, 0.125*envergadura/0.5), ), ((0.025375, -0.03086, 0.0), ), ((
        0.031765, -0.03345, 0.5*envergadura/0.5), ), ((0.03694, -0.03528, 0.125*envergadura/0.5), ), ((0.031765, 
        -0.03345, 0.0), ), ((0.03884, -0.03585, 0.5*envergadura/0.5), ), ((0.04454, -0.03756, 
        0.125*envergadura/0.5), ), ((0.03884, -0.03585, 0.0), ), ((0.04661, -0.038085, 0.5*envergadura/0.5), ), ((
        0.05282, -0.03966, 0.125*envergadura/0.5), ), ((0.04661, -0.038085, 0.0), ), ((0.055055, 
        -0.04015, 0.5*envergadura/0.5), ), ((0.06176, -0.04162, 0.125*envergadura/0.5), ), ((0.055055, -0.04015, 
        0.0), ), ((0.06416, -0.042085, 0.5*envergadura/0.5), ), ((0.07136, -0.04348, 0.125*envergadura/0.5), ), ((
        0.06416, -0.042085, 0.0), ), ((0.07392, -0.04392, 0.5*envergadura/0.5), ), ((0.0816, 
        -0.04524, 0.125*envergadura/0.5), ), ((0.07392, -0.04392, 0.0), ), ((0.084325, -0.04566, 
        0.5*envergadura/0.5), ), ((0.0925, -0.04692, 0.125*envergadura/0.5), ), ((0.084325, -0.04566, 0.0), ), ((
        0.09538, -0.04733, 0.5*envergadura/0.5), ), ((0.10402, -0.04856, 0.125*envergadura/0.5), ), ((0.09538, 
        -0.04733, 0.0), ), ((0.10706, -0.048955, 0.5*envergadura/0.5), ), ((0.11618, -0.05014, 
        0.125*envergadura/0.5), ), ((0.10706, -0.048955, 0.0), ), ((0.11937, -0.050535, 0.5*envergadura/0.5), ), ((
        0.12894, -0.05172, 0.125*envergadura/0.5), ), ((0.11937, -0.050535, 0.0), ), ((0.132285, 
        -0.052115, 0.5*envergadura/0.5), ), ((0.14232, -0.0533, 0.125*envergadura/0.5), ), ((0.132285, -0.052115, 
        0.0), ), ((0.14581, -0.053695, 0.5*envergadura/0.5), ), ((0.15628, -0.05488, 0.125*envergadura/0.5), ), ((
        0.14581, -0.053695, 0.0), ), ((0.15992, -0.05528, 0.5*envergadura/0.5), ), ((0.17084, 
        -0.05648, 0.125*envergadura/0.5), ), ((0.15992, -0.05528, 0.0), ), ((0.174625, -0.05689, 
        0.5*envergadura/0.5), ), ((0.18598, -0.05812, 0.125*envergadura/0.5), ), ((0.174625, -0.05689, 0.0), ), ), 
        minSizeFactor=0.1, size=0.02)
    mdb.models[modelo].parts['Piel'].generateMesh()
    mdb.models[modelo].parts['Costilla'].seedEdgeBySize(constraint=FINER, 
        deviationFactor=0.1, edges=
        mdb.models[modelo].parts['Costilla'].edges.findAt(((0.189905, 0.125225, 
        0.02), ), ((0.174625, 0.12122, 0.02), ), ((0.15992, 0.11693, 0.02), ), ((
        0.14581, 0.11239, 0.02), ), ((0.132285, 0.107595, 0.02), ), ((0.11937, 
        0.102585, 0.02), ), ((0.10706, 0.09736, 0.02), ), ((0.09538, 0.09196, 
        0.02), ), ((0.084325, 0.0864, 0.02), ), ((0.07392, 0.08071, 0.02), ), ((
        0.06416, 0.074915, 0.02), ), ((0.055055, 0.06905, 0.02), ), ((0.04661, 
        0.063125, 0.02), ), ((0.03884, 0.057185, 0.02), ), ((0.031765, 0.05123, 
        0.02), ), ((0.025375, 0.045315, 0.02), ), ((0.01968, 0.039445, 0.02), ), ((
        0.0147, 0.033645, 0.02), ), ((0.010425, 0.027925, 0.02), ), ((0.00688, 
        0.022315, 0.02), ), ((0.00406, 0.01684, 0.02), ), ((0.00199, 0.01149, 
        0.02), ), ((0.000665, 0.00629, 0.02), ), ((9.5e-05, 0.00125, 0.02), ), ((
        0.000285, -0.003585, 0.02), ), ((0.001235, -0.008125, 0.02), ), ((0.00293, 
        -0.012375, 0.02), ), ((0.00538, -0.01633, 0.02), ), ((0.00856, -0.020015, 
        0.02), ), ((0.012475, -0.023425, 0.02), ), ((0.0171, -0.02657, 0.02), ), ((
        0.02244, -0.029485, 0.02), ), ((0.028485, -0.03218, 0.02), ), ((0.035215, 
        -0.03467, 0.02), ), ((0.04264, -0.03699, 0.02), ), ((0.05075, -0.039135, 
        0.02), ), ((0.059525, -0.04113, 0.02), ), ((0.06896, -0.043015, 0.02), ), (
        (0.07904, -0.0448, 0.02), ), ((0.089775, -0.0465, 0.02), ), ((0.10114, 
        -0.04815, 0.02), ), ((0.11314, -0.049745, 0.02), ), ((0.12575, -0.051325, 
        0.02), ), ((0.138975, -0.052905, 0.02), ), ((0.15279, -0.054485, 0.02), ), 
        ((0.1672, -0.05608, 0.02), ), ((0.182195, -0.05771, 0.02), ), ((0.197755, 
        -0.059395, 0.02), ), ((0.18598, -0.05812, 0.005), ), ((0.189905, -0.058545, 
        0.0), ), ((0.17084, -0.05648, 0.005), ), ((0.174625, -0.05689, 0.0), ), ((
        0.15628, -0.05488, 0.005), ), ((0.15992, -0.05528, 0.0), ), ((0.14232, 
        -0.0533, 0.005), ), ((0.14581, -0.053695, 0.0), ), ((0.12894, -0.05172, 
        0.005), ), ((0.132285, -0.052115, 0.0), ), ((0.11618, -0.05014, 0.005), ), 
        ((0.11937, -0.050535, 0.0), ), ((0.10402, -0.04856, 0.005), ), ((0.10706, 
        -0.048955, 0.0), ), ((0.0925, -0.04692, 0.005), ), ((0.09538, -0.04733, 
        0.0), ), ((0.0816, -0.04524, 0.005), ), ((0.084325, -0.04566, 0.0), ), ((
        0.07136, -0.04348, 0.005), ), ((0.07392, -0.04392, 0.0), ), ((0.06176, 
        -0.04162, 0.005), ), ((0.06416, -0.042085, 0.0), ), ((0.05282, -0.03966, 
        0.005), ), ((0.055055, -0.04015, 0.0), ), ((0.04454, -0.03756, 0.005), ), (
        (0.04661, -0.038085, 0.0), ), ((0.03694, -0.03528, 0.005), ), ((0.03884, 
        -0.03585, 0.0), ), ((0.03004, -0.03284, 0.005), ), ((0.031765, -0.03345, 
        0.0), ), ((0.02382, -0.0302, 0.005), ), ((0.025375, -0.03086, 0.0), ), ((
        0.0183, -0.02734, 0.005), ), ((0.01968, -0.028055, 0.0), ), ((0.0135, 
        -0.02426, 0.005), ), ((0.0147, -0.02503, 0.0), ), ((0.0094, -0.02092, 
        0.005), ), ((0.010425, -0.021755, 0.0), ), ((0.00604, -0.0173, 0.005), ), (
        (0.00688, -0.018205, 0.0), ), ((0.0034, -0.01342, 0.005), ), ((0.00406, 
        -0.01439, 0.0), ), ((0.00152, -0.00924, 0.005), ), ((0.00199, -0.010285, 
        0.0), ), ((0.00038, -0.00478, 0.005), ), ((0.000665, -0.005895, 0.0), ), ((
        0.0, 0.0, 0.005), ), ((9.5e-05, -0.001195, 0.0), ), ((0.00038, 0.005, 
        0.005), ), ((0.000285, 0.00375, 0.0), ), ((0.00152, 0.01016, 0.005), ), ((
        0.001235, 0.00887, 0.0), ), ((0.0034, 0.01548, 0.005), ), ((0.00293, 
        0.01415, 0.0), ), ((0.00604, 0.02092, 0.005), ), ((0.00538, 0.01956, 0.0), 
        ), ((0.0094, 0.0265, 0.005), ), ((0.00856, 0.025105, 0.0), ), ((0.0135, 
        0.0322, 0.005), ), ((0.012475, 0.030775, 0.0), ), ((0.0183, 0.03798, 
        0.005), ), ((0.0171, 0.036535, 0.0), ), ((0.02382, 0.04384, 0.005), ), ((
        0.02244, 0.042375, 0.0), ), ((0.03004, 0.04974, 0.005), ), ((0.028485, 
        0.048265, 0.0), ), ((0.03694, 0.0557, 0.005), ), ((0.035215, 0.05421, 0.0), 
        ), ((0.04454, 0.06164, 0.005), ), ((0.04264, 0.060155, 0.0), ), ((0.05282, 
        0.06758, 0.005), ), ((0.05075, 0.066095, 0.0), ), ((0.06176, 0.07346, 
        0.005), ), ((0.059525, 0.07199, 0.0), ), ((0.07136, 0.07928, 0.005), ), ((
        0.06896, 0.077825, 0.0), ), ((0.0816, 0.085, 0.005), ), ((0.07904, 0.08357, 
        0.0), ), ((0.0925, 0.0906, 0.005), ), ((0.089775, 0.0892, 0.0), ), ((
        0.10402, 0.09604, 0.005), ), ((0.10114, 0.09468, 0.0), ), ((0.11618, 
        0.10132, 0.005), ), ((0.11314, 0.1, 0.0), ), ((0.12894, 0.10638, 0.005), ), 
        ((0.12575, 0.105115, 0.0), ), ((0.14232, 0.11124, 0.005), ), ((0.138975, 
        0.110025, 0.0), ), ((0.15628, 0.11584, 0.005), ), ((0.15279, 0.11469, 0.0), 
        ), ((0.17084, 0.1202, 0.005), ), ((0.1672, 0.11911, 0.0), ), ((0.18598, 
        0.12428, 0.005), ), ((0.182195, 0.12326, 0.0), ), ((0.197755, 0.127115, 
        0.0), ), ), minSizeFactor=0.1, size=0.02)
    mdb.models[modelo].parts['Costilla'].generateMesh()
    mdb.models[modelo].rootAssembly.regenerate()
    
    
    #Agujeros de costillas
    
    
    session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)
    
    p = mdb.models[modelo].parts['Costilla']
    s = p.features['Solid extrude-1'].sketch
    mdb.models[modelo].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s2 = mdb.models[modelo].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=3.89159, 
        farPlane=4.14687, width=0.830113, height=0.328487, cameraPosition=(
        0.383789, 0.0229813, 4.02923), cameraTarget=(0.383789, 0.0229813, 0))
    s2.CircleByCenterPerimeter(center=(0.125, 0.025), point1=(0.1625, 0.05))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=3.78708, 
        farPlane=4.25138, width=1.57389, height=0.62281, cameraPosition=(0.539274, 
        0.0295935, 4.02923), cameraTarget=(0.539274, 0.0295935, 0))
    s2.CircleByCenterPerimeter(center=(0.35, 0.025), point1=(0.3875, 0.075))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=3.68503, 
        farPlane=4.35343, width=2.30014, height=0.910196, cameraPosition=(0.845587, 
        0.0222291, 4.02923), cameraTarget=(0.845587, 0.0222291, 0))
    s2.undo()
    s2.CircleByCenterPerimeter(center=(0.3, 0.0375), point1=(0.325, 0.0875))
    s2.CircleByCenterPerimeter(center=(0.8, 0.025), point1=(0.825, 0.0875))
    s2.CircleByCenterPerimeter(center=(1.2, 0.024), point1=(1.25, 0.0365))
    s2.CircleByCenterPerimeter(center=(1.0125, 0.025), point1=(1.075, 0.05))
    s2.unsetPrimaryObject()
    p = mdb.models[modelo].parts['Costilla']
    p.features['Solid extrude-1'].setValues(sketch=s2)
    del mdb.models[modelo].sketches['__edit__']
    p = mdb.models[modelo].parts['Costilla']
    p.regenerate()
    #: Warning: Failed to attach mesh to part geometry.
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models[modelo].parts['Costilla']
    p.generateMesh()
    
   
    #Generate Job
    
    mdb.Job(activateLoadBalancing=False, atTime=None, contactPrint=OFF, 
        description='', echoPrint=OFF, explicitPrecision=SINGLE, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model=modelo, modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name=nombre_modelo, 
        nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, 
        parallelizationMethodExplicit=DOMAIN, queue=None, resultsFormat=ODB, 
        scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
    mdb.jobs[nombre_modelo].submit(consistencyChecking=OFF)
    mdb.jobs[nombre_modelo].waitForCompletion()
    
    
for i in range(0,len(velocidad_l)):
    modelo_completo(i)

    
