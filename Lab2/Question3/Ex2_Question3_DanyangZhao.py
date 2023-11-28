#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
import seaborn as sbn
from scipy import signal

FindPath='D:\\Master of Geomatics\\uni-stuttgart-Semester3\\0_Class_Semester3\\Satellite Geodesy Observation Techniques\\Lab\\data\\'

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

    Latitude=signal.savgol_filter(Latitude,10,2)
    Longitude=signal.savgol_filter(Longitude,10,2)
    Height=signal.savgol_filter(Height,100,2)

    fig=mb.figure()
    #sbn.set()

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

    ax1=fig.add_subplot(3,1,1)
    color='tab:blue'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Latitude(deg)',color=color)
    ax1.plot(Time,Latitude,color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    ax1=fig.add_subplot(3,1,2)
    color='tab:red'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Longitude(deg)',color=color)
    ax1.plot(Time,Longitude,color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    ax1=fig.add_subplot(3,1,3)
    color='tab:green'
    ax1.set_xlabel('Time of observation.(year)')
    ax1.set_ylabel('Height(m)',color=color)
    ax1.plot(Time,Height,color=color)
    ax1.tick_params(axis='y',labelcolor=color)
    ax1.grid()

    mb.show()