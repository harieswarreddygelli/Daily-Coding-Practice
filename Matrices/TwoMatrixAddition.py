r1 = int(input("Enter matrix1 rows size: "))
c1 = int(input("Enter matrix1 columns size: "))
r2 = int(input("Enter matrix2 rows size: "))
c2 = int(input("Enter matrix2 columns size: "))

# Validate dimensions for matrix addition
if r1 != r2 or c1 != c2:
    print("Error: Matrix addition is not possible. Both matrices must have the same dimensions.")
else:
    matrix1 = []
    print("=" * 10, "Enter matrix 1 elements", "=" * 10)
    for i in range(r1):
        rows = []
        for j in range(c1):
            rows.append(int(input(f"Element [{i}][{j}]: ")))
        matrix1.append(rows)
        
    matrix2 = []
    print("=" * 10, "Enter matrix 2 elements", "=" * 10)
    for i in range(r2):
        rows = []
        for j in range(c2):
            rows.append(int(input(f"Element [{i}][{j}]: ")))
        matrix2.append(rows)

    print("=" * 10, "The result matrix (Addition)", "=" * 10)
    result = []
    for i in range(r1):
        res = []
        for j in range(c1):
            res.append(matrix1[i][j] + matrix2[i][j])
        result.append(res)

    # Fixed formatting: added a newline after each row prints
    for i in range(r1):
        for j in range(c1):
            print(result[i][j], end=" ")
        print()
