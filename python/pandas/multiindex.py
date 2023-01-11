import numpy as np
import pandas as pd

#data=np.random.rand(4,3)
#dataFrame=pd.DataFrame(data,index=["Emir","Yasin","İrem","Rabia"],columns=["Yaş","Çalışma Saati","Maaş"])
#print(dataFrame)
firstIndex=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
secondIndex=["Homer","Bart","Merge","Cartman","Kenny","Kyle"]
thirdIndex=list(zip(firstIndex,secondIndex))
thirdIndex=pd.MultiIndex.from_tuples(thirdIndex)
list1=[[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
list2=np.array(list1)
dataFrame=pd.DataFrame(list2,index=thirdIndex,columns=["Yaş","Meslek"])
print(dataFrame)
print(dataFrame.loc["Simpson"])
dataFrame.index.names=["Film Adı","İsim"]
print(dataFrame)
    