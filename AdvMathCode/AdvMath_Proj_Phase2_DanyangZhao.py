#Python Code finished by Danyang Zhao
import pandas as pd
import numpy as np
import matplotlib.pyplot as mb
import pandas as pd
import numpy as np
import seaborn as sns

FindPath='F:\\Master of Geomatics\\uni-stuttgar\\0_Class Start\\Semester 1\\Adv Math Exercise\\Project_Mustafa_Danyang\\Phase2Data-2022-12-05\\'

sh = pd.read_excel(FindPath+"2003.xlsx",sheet_name="2003use",header=None)

Height=sh.loc[:,9].tolist()
East=sh.loc[:,10]
North=sh.loc[:,11]

East_mean=np.nanmean(np.array(East))
North_mean=np.nanmean(np.array(North))
East_median=np.nanmedian(np.array(East))
North_median=np.nanmedian(np.array(North))

Height=np.array(Height)
Height[0]=0
Height[1:]=np.diff(Height)
Height[abs(Height)>900]=np.NaN
Height=pd.DataFrame(Height)

mb.figure()
#mb.quiver(East, North, 0,(-1)*Height, color='c')
mb.scatter(East,North,marker='*',s=260,edgecolors='white')
mb.scatter(East_mean,North_mean,marker='o',s=120,edgecolors='white')
mb.scatter(East_median,North_median,marker='s',s=120,edgecolors='white')
mb.xlabel('East(m)',fontsize=12)
mb.ylabel('North(m)',fontsize=12)
mb.title('2003.xlsx Position Scatter',fontsize=16)
mb.grid()
mb.legend(["Position of Stations","Mean Position","Median Position"])
mb.show()

fig=mb.figure()
sns.set()
fig.suptitle('2003.xlsx Position Analysis',fontsize=26)
#subplot
ax1=fig.add_subplot(1,2,1)
sns.histplot(data=East,binwidth=70,stat="percent",kde=True,ax=ax1)
ax1.set_xlabel('East Position of Stations',fontsize=16)
ax1.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=East_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=East_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["East Position of Stations","Mean Position","Median Position"],loc="upper right",fontsize=12)
ax2=fig.add_subplot(1,2,2)
sns.histplot(data=North,binwidth=360,stat="percent",kde=True,ax=ax2)
ax2.set_xlabel('North Position of Stations',fontsize=16)
ax2.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=North_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=North_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["North Position of Stations","Mean Position","Median Position"],loc="upper left",fontsize=12)
mb.show()

sh = pd.read_excel(FindPath+"2017.xlsx",sheet_name="2017useGAMIT",header=None)

East=sh.loc[:,10]
North=sh.loc[:,11]

East_mean=np.nanmean(np.array(East))
North_mean=np.nanmean(np.array(North))
East_median=np.nanmedian(np.array(East))
North_median=np.nanmedian(np.array(North))

mb.figure()
sns.reset_defaults()
mb.scatter(East,North,marker='*',s=260,edgecolors='white')
mb.scatter(East_mean,North_mean,marker='o',s=120,edgecolors='white')
mb.scatter(East_median,North_median,marker='s',s=120,edgecolors='white')
mb.xlabel('East(m)',fontsize=12)
mb.ylabel('North(m)',fontsize=12)
mb.title('2017.xlsx Position Scatter',fontsize=16)
mb.grid()
mb.legend(["Position of Stations","Mean Position","Median Position"])
mb.show()

fig=mb.figure()
sns.set()
fig.suptitle('2017.xlsx Position Analysis',fontsize=26)
#subplot
ax1=fig.add_subplot(1,2,1)
sns.histplot(data=East,binwidth=70,stat="percent",kde=True,ax=ax1)
ax1.set_xlabel('East Position of Stations',fontsize=16)
ax1.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=East_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=East_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["East Position of Stations","Mean Position","Median Position"],loc="upper right",fontsize=12)
ax2=fig.add_subplot(1,2,2)
sns.histplot(data=North,binwidth=360,stat="percent",kde=True,ax=ax2)
ax2.set_xlabel('North Position of Stations',fontsize=16)
ax2.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=North_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=North_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["North Position of Stations","Mean Position","Median Position"],loc="upper left",fontsize=12)
mb.show()

sh = pd.read_excel(FindPath+"2021.xlsx",sheet_name="2021useCSRSPPPdiff",header=None)

East=sh.loc[:,10]
North=sh.loc[:,11]

East_mean=np.nanmean(np.array(East))
North_mean=np.nanmean(np.array(North))
East_median=np.nanmedian(np.array(East))
North_median=np.nanmedian(np.array(North))

mb.figure()
sns.reset_defaults()
mb.scatter(East,North,marker='*',s=260,edgecolors='white')
mb.scatter(East_mean,North_mean,marker='o',s=120,edgecolors='white')
mb.scatter(East_median,North_median,marker='s',s=120,edgecolors='white')
mb.xlabel('East(m)',fontsize=12)
mb.ylabel('North(m)',fontsize=12)
mb.title('2021.xlsx Position Scatter',fontsize=16)
mb.grid()
mb.legend(["Position of Stations","Mean Position","Median Position"])
mb.show()

fig=mb.figure()
sns.set()
fig.suptitle('2021.xlsx Position Analysis',fontsize=26)
#subplot
ax1=fig.add_subplot(1,2,1)
sns.histplot(data=East,binwidth=70,stat="percent",kde=True,ax=ax1)
ax1.set_xlabel('East Position of Stations',fontsize=16)
ax1.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=East_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=East_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["East Position of Stations","Mean Position","Median Position"],loc="upper right",fontsize=12)
ax2=fig.add_subplot(1,2,2)
sns.histplot(data=North,binwidth=360,stat="percent",kde=True,ax=ax2)
ax2.set_xlabel('North Position of Stations',fontsize=16)
ax2.set_ylabel('Percentage(%)',fontsize=16)
mb.vlines(x=North_mean,ymin=0,ymax=15,color='orange')
mb.vlines(x=North_median,ymin=0,ymax=15,color='limegreen')
mb.legend(["North Position of Stations","Mean Position","Median Position"],loc="upper left",fontsize=12)
mb.show()