def primenumber(a, b):
    while a < b:
        if isprime(a):
            print(a, end=" ")
        a += 1

def isprime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True

a, b = map(int, input("Enter two Numbers: ").split())
primenumber(a, b)  # Removed the outer print() here
