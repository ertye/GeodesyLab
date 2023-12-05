#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
import seaborn as sbn

FindPath='D:\\Master of Geomatics\\uni-stuttgart-Semester3\\0_Class_Semester3\\Satellite Geodesy Observation Techniques\\Lab\\data\\'

fig=mb.figure()
sbn.set()
# ax1=fig.add_subplot(3,1,1)
# ax2=fig.add_subplot(3,1,2)
# ax3=fig.add_subplot(3,1,3)
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

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
    #Time=Time-min(Time)
    Latitude=np.array(data1.loc[:,'_latitude(deg)'].tolist())
    Latitude=Latitude-min(Latitude)
    Longitude=np.array(data1.loc[:,'_longitude(deg)'].tolist())
    Longitude=Longitude-min(Longitude)
    Height=np.array(data1.loc[:,'__height(m)'].tolist())
    Height=Height-min(Height)

    match i:
        case 0:
            label0='Station UWEV'
        case 1:
            label0='Station NPIT'
        case 2:
            label0='Station CNPK'
        case 3:
            label0='Station BYRL'
        case 4:
            label0='Station JOKA'
        case 5:
            label0='Station HNLC'
        case 6:
            label0='Station HILO'
        case 7:
            label0='Station MANE'
        case 8:
            label0='Station KOSM'
        case 9:
            label0='Station AHUP'
    
    color='tab:blue'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Latitude(deg)',color=color)
    ax1.plot(Time,Latitude,label=label0)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.legend()

    color='tab:red'
    ax2.set_xlabel('Time of observation.(year)')
    ax2.set_ylabel('Longitude(deg)',color=color)
    ax2.plot(Time,Longitude,label=label0)
    ax2.tick_params(axis='y',labelcolor=color)
    ax2.legend()

    color='tab:green'
    ax3.set_xlabel('Time of observation.(year)')
    ax3.set_ylabel('Height(m)',color=color)
    ax3.plot(Time,Height,label=label0)
    ax3.tick_params(axis='y',labelcolor=color)
    ax3.legend()

mb.show()
