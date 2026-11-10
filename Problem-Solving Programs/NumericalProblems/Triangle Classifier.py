# Read three sides
a = int(input())
b = int(input())
c = int(input())

# Check if the sides can form a valid triangle
if (a + b > c) and (b + c > a) and (a + c > b):
    # Classify and print
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")
