import numpy as np
import pandas as pd

dict1={"Isım" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"]}
dataFrame1=pd.DataFrame(dict1)
print(dataFrame1)
print("\n")
dict2={"Isım" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Kalori" : [100,200,150,250]}
dataFrame2=pd.DataFrame(dict2)
print(dataFrame2)
print("\n")
print(pd.merge(dataFrame1,dataFrame2,on="Isım"))