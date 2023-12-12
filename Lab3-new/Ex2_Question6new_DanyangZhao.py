#Python Code finished by Danyang Zhao


import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import sys as sys1
from mpl_toolkits.basemap import Basemap
#coastline
# mb.figure(figsize=(10, 6))
# m = Basemap(llcrnrlon=-161, llcrnrlat=17, urcrnrlon=-151, urcrnrlat=24, projection='lcc', lat_1=20, lat_2=-21,
# lon_0=-155)
# m.drawcountries(linewidth=1.5)
# m.drawcoastlines()
# mb.show()
FindPath='D:\\Master of Geomatics\\uni-stuttgart-Semester3\\0_Class_Semester3\\Satellite Geodesy Observation Techniques\\Lab\\data\\'

mb.figure()
m = Basemap(projection='cyl')

for i in range(10):

    #if i!=9:#5 is null
    #    continue

    if i==0:
        data1=pd.read_csv(FindPath+"UWEV.PA.tenv3.txt",header=0,sep='\s+')
    if i==1:
        data1=pd.read_csv(FindPath+"NPIT.PA.tenv3.txt",header=0,sep='\s+')
    if i==2:
        data1=pd.read_csv(FindPath+"CNPK.PA.tenv3.txt",header=0,sep='\s+')
    if i==3:
        data1=pd.read_csv(FindPath+"BYRL.PA.tenv3.txt",header=0,sep='\s+')
    if i==4:
        data1=pd.read_csv(FindPath+"JOKA.PA.tenv3.txt",header=0,sep='\s+')
    if i==5:
        data1=pd.read_csv(FindPath+"HNLC.PA.tenv3.txt",header=0,sep='\s+')
    if i==6:
        data1=pd.read_csv(FindPath+"HILO.PA.tenv3.txt",header=0,sep='\s+')
    if i==7:
        data1=pd.read_csv(FindPath+"MANE.PA.tenv3.txt",header=0,sep='\s+')
    if i==8:
        data1=pd.read_csv(FindPath+"KOSM.PA.tenv3.txt",header=0,sep='\s+')
    if i==9:
        data1=pd.read_csv(FindPath+"AHUP.PA.tenv3.txt",header=0,sep='\s+')

    Time=np.array(data1.loc[:,'yyyy.yyyy'].tolist())
    Latitude=np.array(data1.loc[:,'_latitude(deg)'].tolist())
    Longitude=np.array(data1.loc[:,'_longitude(deg)'].tolist())
    East=np.array(data1.loc[:,'__east(m)'].tolist())
    East=East-East[0]
    North=np.array(data1.loc[:,'_north(m)'].tolist())
    North=North-North[0]
    Height=np.array(data1.loc[:,'__height(m)'].tolist())

    # #all
    # tmpN1=Time>1018
    # tmpN2=Time<3022
    #2018 eruption
    # tmpN1=Time>2018
    # tmpN2=Time<2019
    #2021 eruption
    tmpN1=Time>2021
    tmpN2=Time<2022

    tmpN=tmpN1&tmpN2

    x, y = m(Longitude[tmpN], Latitude[tmpN]) # compute map proj coordinates.
    x1, y1 = m(East[tmpN], North[tmpN])
    m.shadedrelief(scale=1)
    m.drawparallels(circles=np.linspace(-90, 90, 7),
                    labels=[1, 0, 0, 0], color='gray')
    m.drawmeridians(meridians=np.linspace(-180, 180, 13),
                    labels=[0, 0, 0, 1], color='gray')
    #m.drawcoastlines()
    m.drawcountries()

    if(len(x)==0):
        continue

    x10=0.06
    if i==0:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x[0], y[0], marker='v', s=100, facecolor='#00BFFF',
            edgecolor='white', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='#00BFFF',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='#00BFFF',latlon='True')
    if i==1:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='o', s=100, facecolor='b',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='b',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='b',latlon='True')
    if i==2:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='*', s=100, facecolor='r',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='r',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='r',latlon='True')
    if i==3:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='^', s=100, facecolor='g',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='g',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='g',latlon='True')
    if i==4:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='x', s=100, facecolor='k',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='k',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='k',latlon='True')
    if i==5:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='d', s=100, facecolor='c',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='c',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='c',latlon='True')
    if i==6:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='s', s=100, facecolor='m',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='m',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='m',latlon='True')
    if i==7:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='p', s=100, facecolor='y',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='y',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='y',latlon='True')
    if i==8:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker=',', s=100, facecolor='purple',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='purple',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='purple',latlon='True')
    if i==9:
        d0=np.sqrt((x1[0]-x1[len(x1)-1])**2+(y1[0]-y1[len(y1)-1])**2)*x10
        m.scatter(x, y, marker='8', s=100, facecolor='#AABF00',
            edgecolor='blue', linewidth=0)
        m.plot([x[0],x[0]+d0],[y[0],y[0]+d0],linewidth=2,color='#AABF00',latlon='True')
        d1=np.abs(Height[0]-Height[len(Height)-1])*x10
        m.plot([x[0],x[0]],[y[0],y[0]+d1],linewidth=2,color='#AABF00',latlon='True')

    # if i==0:
    #     mb.title('Station UWEV',fontsize=14)
    # if i==1:
    #     mb.title('Station NPIT',fontsize=14)
    # if i==2:
    #     mb.title('Station CNPK',fontsize=14)
    # if i==3:
    #     mb.title('Station BYRL',fontsize=14)
    # if i==4:
    #     mb.title('Station JOKA',fontsize=14)
    # if i==5:
    #     mb.title('Station HNLC',fontsize=14)
    # if i==6:
    #     mb.title('Station HILO',fontsize=14)
    # if i==7:
    #     mb.title('Station MANE',fontsize=14)
    # if i==8:
    #     mb.title('Station KOSM',fontsize=14)
    # if i==9:
    #     mb.title('Station AHUP',fontsize=14)
    
###############################################################


mb.xlabel('\n Longitude(°)',fontsize=12)
mb.ylabel('Latitude(°)\n\n\n',fontsize=12)
mb.show()

