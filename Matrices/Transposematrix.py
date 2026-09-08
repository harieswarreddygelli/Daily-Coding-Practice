r1 = int(input("Enter matrix rows size: "))
c1 = int(input("Enter matrix columns size: "))

matrix = []
print("=" * 10, "Enter matrix elements", "=" * 10)
for i in range(r1):
    rows = []
    for j in range(c1):
        rows.append(int(input(f"Element [{i}][{j}]: ")))
    matrix.append(rows)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

transpose = []
for j in range(c1):
    trans_row = []
    for i in range(r1):
        trans_row.append(matrix[i][j])
    transpose.append(trans_row)


print("\nTransposed Matrix:")
for row in transpose:
    print(row)
