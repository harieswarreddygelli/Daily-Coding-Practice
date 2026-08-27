n = int(input("Enter a Number: ")) 
square = n * n
total = 0 
temp = square
while temp > 0:
    total += temp% 10
    temp //= 10
print("It is a Neon Number" if total == n else "It Is Not Neon Number")
