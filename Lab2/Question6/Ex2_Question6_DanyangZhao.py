#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
from mpl_toolkits.basemap import Basemap

FindPath='D:\\Master of Geomatics\\uni-stuttgart-Semester3\\0_Class_Semester3\\Satellite Geodesy Observation Techniques\\Lab\\data\\'

mb.figure()
m = Basemap(projection='cyl')

for i in range(10):

    #if i!=9:#5 is null
    #    continue

    match i:
        case 0:
            data1=pd.read_csv(FindPath+"UWEV.PA.tenv3.txt",header=0,sep='\s+')
        case 1:
            data1=pd.read_csv(FindPath+"NPIT.PA.tenv3.txt",header=0,sep='\s+')
        case 2:
            data1=pd.read_csv(FindPath+"CNPK.PA.tenv3.txt",header=0,sep='\s+')
        case 3:
            data1=pd.read_csv(FindPath+"BYRL.PA.tenv3.txt",header=0,sep='\s+')
        case 4:
            data1=pd.read_csv(FindPath+"JOKA.PA.tenv3.txt",header=0,sep='\s+')
        case 5:
            data1=pd.read_csv(FindPath+"HNLC.PA.tenv3.txt",header=0,sep='\s+')
        case 6:
            data1=pd.read_csv(FindPath+"HILO.PA.tenv3.txt",header=0,sep='\s+')
        case 7:
            data1=pd.read_csv(FindPath+"MANE.PA.tenv3.txt",header=0,sep='\s+')
        case 8:
            data1=pd.read_csv(FindPath+"KOSM.PA.tenv3.txt",header=0,sep='\s+')
        case 9:
            data1=pd.read_csv(FindPath+"AHUP.PA.tenv3.txt",header=0,sep='\s+')

    Time=np.array(data1.loc[:,'yyyy.yyyy'].tolist())
    Latitude=np.array(data1.loc[:,'_latitude(deg)'].tolist())
    Longitude=np.array(data1.loc[:,'_longitude(deg)'].tolist())
    Height=np.array(data1.loc[:,'__height(m)'].tolist())

    #all
    tmpN1=Time>1018
    tmpN2=Time<3022
    #2018 eruption
    #tmpN1=Time>2018
    #tmpN2=Time<2019
    #2021 eruption
    #tmpN1=Time>2021
    #tmpN2=Time<2022
    tmpN=tmpN1&tmpN2

    x, y = m(Longitude[tmpN], Latitude[tmpN]) # compute map proj coordinates.
    m.shadedrelief(scale=0.1)
    m.drawparallels(circles=np.linspace(-90, 90, 7),
                    labels=[1, 0, 0, 0], color='gray')
    m.drawmeridians(meridians=np.linspace(-180, 180, 13),
                    labels=[0, 0, 0, 1], color='gray')
    
    match i:
        case 0:
            m.scatter(x, y, marker='v', s=100, facecolor='#00BFFF',
                edgecolor='white', linewidth=0)
        case 1:
            m.scatter(x, y, marker='o', s=100, facecolor='b',
                edgecolor='blue', linewidth=0)
        case 2:
            m.scatter(x, y, marker='*', s=100, facecolor='r',
                edgecolor='blue', linewidth=0)
        case 3:
            m.scatter(x, y, marker='^', s=100, facecolor='g',
                edgecolor='blue', linewidth=0)
        case 4:
            m.scatter(x, y, marker='x', s=100, facecolor='k',
                edgecolor='blue', linewidth=0)
        case 5:
            m.scatter(x, y, marker='d', s=100, facecolor='c',
                edgecolor='blue', linewidth=0)
        case 6:
            m.scatter(x, y, marker='s', s=100, facecolor='m',
                edgecolor='blue', linewidth=0)
        case 7:
            m.scatter(x, y, marker='p', s=100, facecolor='y',
                edgecolor='blue', linewidth=0)
        case 8:
            m.scatter(x, y, marker=',', s=100, facecolor='purple',
                edgecolor='blue', linewidth=0)
        case 9:
            m.scatter(x, y, marker='8', s=100, facecolor='#AABF00',
                edgecolor='blue', linewidth=0)

    match i:
        case 0:
            mb.title('Station UWEV',fontsize=14)
        case 1:
            mb.title('Station NPIT',fontsize=14)
        case 2:
            mb.title('Station CNPK',fontsize=14)
        case 3:
            mb.title('Station BYRL',fontsize=14)
        case 4:
            mb.title('Station JOKA',fontsize=14)
        case 5:
            mb.title('Station HNLC',fontsize=14)
        case 6:
            mb.title('Station HILO',fontsize=14)
        case 7:
            mb.title('Station MANE',fontsize=14)
        case 8:
            mb.title('Station KOSM',fontsize=14)
        case 9:
            mb.title('Station AHUP',fontsize=14)
    
###############################################################


mb.xlabel('\n Longitude(°)',fontsize=12)
mb.ylabel('Latitude(°)\n\n\n',fontsize=12)
mb.show()

