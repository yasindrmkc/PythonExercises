import pandas as pd
import numpy as np
def bruttenNete(maas):
    return maas*0.66

dict1={"Isım" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Departman" : ["Yazılım","Satış","Pazarlama","Yazılım"],"Maaş" : [200,300,400,500]}
dataFrame1=pd.DataFrame(dict1)

print(dataFrame1["Departman"].unique())
print(dataFrame1["Departman"].nunique())
print(dataFrame1["Departman"].value_counts())
print(dataFrame1["Maaş"].apply(bruttenNete))
print(dataFrame1.isnull())



