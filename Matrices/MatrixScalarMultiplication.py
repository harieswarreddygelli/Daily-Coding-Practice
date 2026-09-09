r1 = int(input("Enter matrix1 rows size: "))
c1 = int(input("Enter matrix1 columns size: "))

matrix1 = []
print("=" * 10, "Enter matrix 1 elements", "=" * 10)
for i in range(r1):
    rows = []
    for j in range(c1):
        rows.append(int(input(f"Element [{i}][{j}]: ")))
    matrix1.append(rows)
    
n=int(input("Enter the number you want to multiply the matrix with: "))
for i in range(r1):
    for j in range(c1):
        matrix1[i][j]=matrix1[i][j]*n

print("The matrix After Scalar  Multiplication  is: ",matrix1)
