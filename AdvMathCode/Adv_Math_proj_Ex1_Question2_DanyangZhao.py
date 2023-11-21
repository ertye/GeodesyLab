#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
import seaborn as sbn

FindPath='F:\\课件\\研究所\\Preparation for study\\Europe\\Germany\\uni-stuttgar\\0_Class Start\\Semester 1\\Adv Math Exercise\\Project_Mustafa_Danyang\\Data\\'

#data1=pd.read_csv(FindPath+"UWEV.PA.tenv3.txt",header=0,sep='\s+')
#data1=pd.read_csv(FindPath+"NPIT.PA.tenv3.txt",header=0,sep='\s+')
#data1=pd.read_csv(FindPath+"CNPK.PA.tenv3.txt",header=0,sep='\s+')
#data1=pd.read_csv(FindPath+"BYRL.PA.tenv3.txt",header=0,sep='\s+')
data1=pd.read_csv(FindPath+"JOKA.PA.tenv3.txt",header=0,sep='\s+')

Time=np.array(data1.loc[:,'yyyy.yyyy'].tolist())
Latitude=np.array(data1.loc[:,'_latitude(deg)'].tolist())
Longitude=np.array(data1.loc[:,'_longitude(deg)'].tolist())
Height=np.array(data1.loc[:,'__height(m)'].tolist())

fig=mb.figure()
sbn.set()

#fig.suptitle('Station UWEV')
#fig.suptitle('Station NPIT')
#fig.suptitle('Station CNPK')
#fig.suptitle('Station BYRL')
fig.suptitle('Station JOKA')

ax1=fig.add_subplot(3,1,1)
color='tab:blue'
ax1.set_xlabel('Time of observation.(year)')
ax1.set_ylabel('Latitude(deg)',color=color)
ax1.plot(Time,Latitude,color=color)
ax1.tick_params(axis='y',labelcolor=color)

ax1=fig.add_subplot(3,1,2)
color='tab:red'
ax1.set_xlabel('Time of observation.(year)')
ax1.set_ylabel('Longitude(deg)',color=color)
ax1.plot(Time,Longitude,color=color)
ax1.tick_params(axis='y',labelcolor=color)

ax1=fig.add_subplot(3,1,3)
color='tab:green'
ax1.set_xlabel('Time of observation.(year)')
ax1.set_ylabel('Height(m)',color=color)
ax1.plot(Time,Height,color=color)
ax1.tick_params(axis='y',labelcolor=color)

mb.show()
