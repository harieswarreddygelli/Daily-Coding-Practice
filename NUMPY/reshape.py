import numpy as np 
a=np.arange(12)
print(a)
b=a.reshape(3,4)
print(b)
c=a.reshape(2,2,3)
print(c)
d=a.reshape(4,-1)
print(d)
