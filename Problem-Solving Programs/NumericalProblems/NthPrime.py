def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    count = 0
    current = 1
    
    # Keep checking numbers until we find the n-th prime
    while count < n:
        current += 1
        if is_prime(current):
            count += 1
            
    return current

n = int(input("Enter the value of n: "))
result = nth_prime(n)
print(f"The {n}-th prime number is {result}")
