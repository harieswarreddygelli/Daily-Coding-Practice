import numpy as np
arr=np.array(list(map(int,input("Enter Elements seprated by spaces: ").split())))
print("The  Cumulative sum of given array: ",np.cumsum(arr))
print("The  Cumulative Product of given array: ",np.cumprod(arr))
