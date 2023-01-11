import numpy as np
import pandas as pd 

data=np.random.randn(4,3)
dataFrame=pd.DataFrame(data)
dataFrame=pd.DataFrame(data,index=["Yasin","Bora","İrem","Rabia"],columns=["Maaş","Yaş","Çalışma Saati"])
newIndex=["Ati","Zeynep","Mehmet","Atlas"]
dataFrame["Yeni İndeks"]=newIndex
#print(dataFrame)
#print(dataFrame.set_index("Yeni İndeks"))
dataFrame.set_index("Yeni İndeks",inplace=True)
print(dataFrame)