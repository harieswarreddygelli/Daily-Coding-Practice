n = int(input("Enter a Number"))
temp = n
has_zero = False
while temp > 0:
    if temp % 10 == 0:
        has_zero= True
        break
    temp //= 10
print("It is a Duck Number" if has_zero else "It is Not a Duck Number")
