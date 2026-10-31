import math

def print_pascal_triangle(rows):
    for i in range(rows):
        # Print leading spaces to create a centered triangle shape
        print(" " * (rows - i), end="")
        
        for j in range(i + 1):
            # math.comb(n, k) calculates n! / (k! * (n - k)!)
            print(math.comb(i, j), end=" ")
            
        print()


n=int(input("Enter How many rows You want to Print"))
print_pascal_triangle(n)
