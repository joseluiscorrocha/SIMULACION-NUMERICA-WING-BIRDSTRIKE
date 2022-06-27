# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:00:01 2022

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
    'S', INTEGRATION_POINT), ), nodeSets=("PIEL-1.SET-IMACTTTTT", ))

curveList = session.curveSet(xyData=xyList)




s=[]

for i in range(0,len(grupo.nodes)):
    s.append(session.xyDataObjects['_S:Mises (Avg: 75%) SP:1 PI: PIEL-1 N: '+str(grupo.nodes[i].label)])
for i in range(0,len(grupo.nodes)):
    s.append(session.xyDataObjects['_S:Mises (Avg: 75%) SP:5 PI: PIEL-1 N: '+str(grupo.nodes[i].label)])
session.xyReportOptions.setValues(totals=ON, minMax=ON)
session.writeXYReport(fileName='abaqus_s_job_definitivo'+str(j)+'.rpt', xyData=(s))
