import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print The 2d Matrix First
print(a[:])
# Prints The Specified Rows 
# They are denoted as a[[Requried Rows],:]
print(a[[0,1],:])
print(a[[0,2],:])
print(a[[1,2],:])
