def reverse_integer_math(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        last_digit = n % 10
        reversed_num = (reversed_num * 10) + last_digit
        n //= 10  # Remove the last digit
        
    return reversed_num * sign


n=int(input("Enter a Number: "))

print("Reverse of the given number:",reverse_integer_math(n))
