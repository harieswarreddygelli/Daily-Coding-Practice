import numpy as np 
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("The flatten() method converts a multi-dimensional array into a 1D array:")
print(a.flatten())
print("The ravel() method does the same, but returns a view (faster):")
print(a.ravel())
