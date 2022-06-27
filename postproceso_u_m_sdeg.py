# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:56:15 2022

@author: josel
"""
from abaqus import *
from abaqusConstants import *

from caeModules import *
from driverUtils import executeOnCaeStartup
import xyPlot

executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
import os

os.chdir(r"D:\Abaqus\working_directory\TFG_MARZO_2022\9 modelos\100 modelos\sin_envergadura")
j=0
odb = session.openOdb(
    name='D:/Abaqus/working_directory/TFG_MARZO_2022/9 modelos/100 modelos/sin_envergadura/job_definitivo'+str(j)+'.odb')
o1 = session.odbs['D:/Abaqus/working_directory/TFG_MARZO_2022/9 modelos/100 modelos/sin_envergadura/job_definitivo'+str(j)+'.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)

grupo=odb.rootAssembly.instances['PIEL-1'].nodeSets['SET-IMACTTTTT']


xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'SDEG', INTEGRATION_POINT), ), nodeSets=("PIEL-1.SET-IMACTTTTT", ))

curveList = session.curveSet(xyData=xyList)

x=[]
for i in range(0,len(grupo.nodes)):
    x.append(session.xyDataObjects['_SDEG (Avg: 75%) SP:1 PI: PIEL-1 N: '+str(grupo.nodes[i].label)])
for i in range(0,len(grupo.nodes)):
    x.append(session.xyDataObjects['_SDEG (Avg: 75%) SP:5 PI: PIEL-1 N: '+str(grupo.nodes[i].label)])

session.xyReportOptions.setValues(totals=ON, minMax=ON)
session.writeXYReport(fileName='abaqus_sdeg_job_definitivo'+str(j)+'.rpt', xyData=(x))


xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=((
    'U', NODAL, ((INVARIANT, 'Magnitude'), )), ), nodeSets=(
    "PIEL-1.SET-IMACTTTTT", ))
u=[]
for i in range(0,len(grupo.nodes)):
    #x.append(session.xyDataObjects['_SDEG (Avg: 75%) SP:1 PI: PIEL-1 N: '+str(grupo.nodes[i].label)])  
    u.append(session.xyDataObjects['_U:Magnitude PI: PIEL-1 N: '+str(grupo.nodes[i].label)])              
        #session.xyDataObjects['_U:Magnitude PI: PIEL-1 N: 153']
session.xyReportOptions.setValues(totals=ON, minMax=ON)
session.writeXYReport(fileName='abaqus_u_job_definitivo'+str(j)+'.rpt', xyData=(u))
session.odbs['D:/Abaqus/working_directory/TFG_MARZO_2022/9 modelos/100 modelos/sin_envergadura/job_definitivo'+str(j)+'.odb'].close()
