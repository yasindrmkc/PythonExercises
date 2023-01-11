import numpy as np

list1=[[1,2,3],[2,3,4],[3,4,5]]
matrixlist=np.array(list1)
print(matrixlist[0][1])
print(matrixlist[2:,2])
#                ^  ^
#                |  |
#            column number of element

list2=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]       
list3=np.array(list2)
print(list3)
print("\n")
print(list3[[0,1,3]])