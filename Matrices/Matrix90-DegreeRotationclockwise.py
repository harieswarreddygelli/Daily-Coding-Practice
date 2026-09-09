r1 = int(input("Enter matrix1 rows size: "))
c1 = int(input("Enter matrix1 columns size: "))

matrix1 = []
print("=" * 10, "Enter matrix 1 elements", "=" * 10)
for i in range(r1):
    rows = []
    for j in range(c1):
        rows.append(int(input(f"Element [{i}][{j}]: ")))
    matrix1.append(rows)
transpose=[]
for i in range(c1):
    tranele=[]
    for j in range(r1):
        tranele.append(matrix1[j][i])
    transpose.append(tranele)


for row in transpose:
    row.reverse()
    
print("The Matrix 90-Degree Rotation in clock wise:")
for row in transpose:
    print(row)
