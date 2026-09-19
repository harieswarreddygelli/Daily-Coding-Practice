import numpy as np
r=int(input("Enter No of rows: "))
c=int(input("Enter No of Colums: "))
matrix=[]
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Enter element: "))
        row.append(e)
    matrix.append(row)
a=np.array(matrix)
        
print("Sum of 2d Colum wise matrix: ",np.sum(a,axis=0))
print("Sum of 2d Row wise matrix: ",np.sum(a,axis=1))
print("mean of 2d Column wise matrix: ",np.mean(a,axis=0))
print("mean of 2d Row wise matrix: ",np.mean(a,axis=1))
