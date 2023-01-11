import numpy as np
#RESHAPE
list1=np.arange(30)
print("RESHAPE")
list1.reshape(6,5)
print("\n")
list2=np.random.randint(1,40,10)
print(list2.reshape(2,5))
print("\n")
reshapeList=list1.reshape(6,5)
print(reshapeList)

#MAX-MİN
print("\nMAX-MİN")
print(list2.max())
print(list2.min())
print(list2.argmax())
print(list2.argmin())
