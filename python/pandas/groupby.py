import numpy as np
import pandas as pd 


dict1={"Departman" : ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],"Çalışan" : ["Ahmet","Mehmet","Yasin","Bora","İrem","Rabia"],"Maaş" : [100,200,300,400,500,600]}
dataFrame=pd.DataFrame(dict1)
print(dataFrame)
obj1=dataFrame.groupby("Departman")
print(obj1.count())
print(obj1.mean())
print(obj1.min())
print(obj1.max())
print(obj1.describe())
