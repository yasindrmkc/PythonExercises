import numpy as np
import pandas as pd

sozluk1={"İsim" : ["Ahmet","Mehmet","Zeynep","Atıl"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"],"Kalori" : [100,200,300,400]}
dataFrame1=pd.DataFrame(sozluk1,index=[0,1,2,3])

sozluk2={"İsim" : ["Osman","Levent","Atlas","Fatma"],"Spor" : ["Koşu","Yüzme","Koşu","Basketbol"],"Kalori" : [100,200,250,150]}
dataFrame2=pd.DataFrame(sozluk2,index=[4,5,6,7])

sozluk3={"İsim" : ["Ayşe","Mahmut","Duygu","Nur"],"Spor" : ["Koşu","Yüzme","Badminton","Tenis"],"Kalori" : [400,500,100,200]}
dataFrame3=pd.DataFrame(sozluk3,index=[8,9,10,11])  

obj1=pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0)
print(obj1)

