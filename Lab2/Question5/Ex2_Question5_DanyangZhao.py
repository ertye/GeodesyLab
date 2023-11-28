#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
from mpl_toolkits.basemap import Basemap

FindPath='D:\\Master of Geomatics\\uni-stuttgart-Semester3\\0_Class_Semester3\\Satellite Geodesy Observation Techniques\\Lab\\data\\'



Longitude_all=[]
Longitude_all=np.array(Longitude_all)
Latitude_all=[]
Latitude_all=np.array(Latitude_all)

for i in range(10):

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

    fig=mb.figure()

    match i:
        case 0:
            fig.suptitle('Station UWEV')
        case 1:
            fig.suptitle('Station NPIT')
        case 2:
            fig.suptitle('Station CNPK')
        case 3:
            fig.suptitle('Station BYRL')
        case 4:
            fig.suptitle('Station JOKA')
        case 5:
            fig.suptitle('Station HNLC')
        case 6:
            fig.suptitle('Station HILO')
        case 7:
            fig.suptitle('Station MANE')
        case 8:
            fig.suptitle('Station KOSM')
        case 9:
            fig.suptitle('Station AHUP')

    #all
    #tmpN1=Time>2018
    #tmpN2=Time<2022
    #2018 eruption
    tmpN1=Time>2018
    tmpN2=Time<2019
    # #2021 eruption
    # tmpN1=Time>2021
    # tmpN2=Time<2022
    tmpN=tmpN1&tmpN2

    ax1=fig.add_subplot(3,1,1)
    color='tab:blue'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Latitude(deg)',color=color)
    ax1.plot(Time[tmpN],Latitude[tmpN],color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    ax1=fig.add_subplot(3,1,2)
    color='tab:red'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Longitude(deg)',color=color)
    ax1.plot(Time[tmpN],Longitude[tmpN],color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    ax1=fig.add_subplot(3,1,3)
    color='tab:green'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Height(m)',color=color)
    ax1.plot(Time[tmpN],Height[tmpN],color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    mb.show()
    Longitude_all=np.append(Longitude_all,Longitude[tmpN])
    Latitude_all=np.append(Latitude_all,Latitude[tmpN])

    ###############################################################

    mb.figure()
    m = Basemap(projection='cyl')
    x, y = m(Longitude_all, Latitude_all) # compute map proj coordinates.
    m.shadedrelief(scale=0.1)
    m.drawparallels(circles=np.linspace(-90, 90, 7),
                    labels=[1, 0, 0, 0], color='gray')
    m.drawmeridians(meridians=np.linspace(-180, 180, 13),
                    labels=[0, 0, 0, 1], color='gray')
    m.scatter(x, y, marker='v', s=100, facecolor='#00BFFF',
                edgecolor='blue', linewidth=1)
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
    mb.xlabel('\n Longitude(°)',fontsize=12)
    mb.ylabel('Latitude(°)\n\n\n',fontsize=12)
    mb.show()
