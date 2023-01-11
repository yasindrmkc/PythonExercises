import numpy as np


list1=np.arange(0,15)
print(list1[3:5])
list1[3:8] = -2
print(list1)
list2=np.arange(0,15)
list3=list2[3:8]
print(list3)

list3[:] = 100
print(list3)
print(list2)

#COPY
list4=np.arange(0,15)
list5=list4.copy()

list5[3:8] = 50
print(list5)
print(list4)
