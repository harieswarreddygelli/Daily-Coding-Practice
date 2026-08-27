n = int(input("Enter a Number: ")) 
temp, s, p = n, 0, 1
while temp > 0:
  d = temp % 10
  s += d
  p *= d 
  temp//= 10
print("The Number is a Spy Number" if s == p else "The Number is Not a Spy Number")
