def isprime(n):
  for i in range(2,(n//2)+1):
    if n%i==0:
      return False
  return True
n=int(input("Enter a Number: "))
if isprime(n):
  print("The entered Number is a prime")
else:
  print("The entered Number is not a prime")
  
