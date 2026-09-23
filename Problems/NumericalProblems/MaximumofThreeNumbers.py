def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print(f"The largest number is: {find_largest(a, b, c)}")
