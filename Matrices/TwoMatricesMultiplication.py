r1 = int(input("Enter matrix1 rows size: "))
c1 = int(input("Enter matrix1 columns size: "))
r2 = int(input("Enter matrix2 rows size: "))
c2 = int(input("Enter matrix2 columns size: "))

if c1 != r2:
    print("Error: Matrix multiplication is not possible. Columns of Matrix 1 must match rows of Matrix 2.")
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

    result = []
    for i in range(r1):
        res = []
        for j in range(c2):
            s = 0
            for k in range(c1):
                s += matrix1[i][k] * matrix2[k][j]
            res.append(s)
        result.append(res)

    print("=" * 10, "The result matrix (Multiplication)", "=" * 10)
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()
