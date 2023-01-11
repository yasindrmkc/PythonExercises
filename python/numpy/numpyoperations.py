import numpy as np

list1=np.random.randint(1,100,20)

print(list1)
biggerlist=list1>24
print(list1[biggerlist])

print(list1+list1)
print(list1-list1)
print(list1*list1)
print(list1/list1)  
print(np.sqrt(list1))
print(np.max(list1))
print(np.min(list1))