r1 = int(input("Enter matrix1 rows size: "))
c1 = int(input("Enter matrix1 columns size: "))

matrix1 = []
print("=" * 10, "Enter matrix 1 elements", "=" * 10)
for i in range(r1):
    rows = []
    for j in range(c1):
        rows.append(int(input(f"Element [{i}][{j}]: ")))
    matrix1.append(rows)
n=len(matrix1)
seconddiagonalsum=0
for i in range(r1):
        seconddiagonalsum+=matrix1[i][n-i-1]

print("The Secondary Diagonal Sum of  the matrix is: ",seconddiagonalsum)
