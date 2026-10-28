def compute_hcf(x, y):
    # Loop until y becomes 0
    while(y):
        x, y = y, x % y
    return x

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"HCF of {num1} and {num2} is: {compute_hcf(num1, num2)}")
