import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
df=pd.read_csv('testmarks1.csv')
print(df)
r_no=[]
foc_mrk=[]
eds_mrk=[]
son_mrk=[]
phy_mrk=[] 
sub=['foc','eds','son','phy'] 
r_no=np.array(df['RollNO']) 
foc_mrk=np.array(df['FOC']) 
eds_mrk=np.array(df['EDS']) 
son_mrk=np.array(df['SON']) 
phy_mrk=np.array(df['PHY']) 
max_mrk=[]
min_mrk=[] 
avg_mrk=[]
max_mrk.append(max(foc_mrk)) 
max_mrk.append(max(eds_mrk))
max_mrk.append(max(son_mrk)) 
max_mrk.append(max(phy_mrk)) 
min_mrk.append(min(foc_mrk)) 
min_mrk.append(min(eds_mrk)) 
min_mrk.append(min(son_mrk)) 
min_mrk.append(min(phy_mrk)) 
avg_mrk.append(sum(foc_mrk)/10)
avg_mrk.append(sum(eds_mrk)/10) 
avg_mrk.append(sum(son_mrk)/10) 
avg_mrk.append(sum(phy_mrk)/10)
mo801=[foc_mrk[0],eds_mrk[0],son_mrk[0],phy_mrk[0]] 
mo802=[foc_mrk[1],eds_mrk[1],son_mrk[1],phy_mrk[1]]
mo803=[foc_mrk[2],eds_mrk[2],son_mrk[2],phy_mrk[2]]
print(max_mrk,min_mrk,avg_mrk)
plt.xlabel("Roll No") 
plt.ylabel("Marks")
plt.title("FOC marks") 
plt.plot(r_no,foc_mrk,'o-r') 
plt.xlabel("Roll No") 
plt.ylabel("Marks")
plt.title("EDS marks") 
plt.bar(r_no,eds_mrk)
plt.xlabel("Roll No") 
plt.ylabel("Marks")
plt.title("SON marks") 
plt.barh(r_no,son_mrk,color='hotpink') 
plt.xlabel("Roll No") 
plt.ylabel("Marks")

plt.title("PHY marks") 
plt.plot(r_no,phy_mrk,'o:g') 
plt.xlabel("Roll No") 
plt.ylabel("Marks")
plt.title("MAX marks")
plt.bar(sub,max_mrk,color='green') 
plt.xlabel("Roll No") 
plt.ylabel("Marks")
plt.title("MIN marks")
plt.plot(min_mrk,'o:y')
plt.xlabel("Roll No")
plt.ylabel("Marks")
plt.title("AVG marks")
plt.plot(avg_mrk,'o:b')
plt.xlabel('roll no 801 marks')
plt.pie(mo801,labels=sub)
plt.xlabel('roll no 802| marks')
expl=[0.3,0,0,0] 
plt.pie(mo802,labels=sub,explode=expl)
plt.xlabel('roll no 803 marks')
expl2=[0,0.2,0,0] 
plt.pie(mo803,labels=sub,explode=expl2,shadow=True) 
plt.show()
