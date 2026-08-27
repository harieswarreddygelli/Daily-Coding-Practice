def nxt(n):
  s = 0
  while n > 0:
    d = n % 10
    s += d * d 
    n //= 10 
  return s
n =int(input("Enter a Number: ")) 
slow, fast = n, nxt(n)
while fast != 1 and slow != fast: 
  slow = nxt(slow)
  fast = nxt(nxt(fast))
print("The Number is a Happy Number" if fast == 1 else "The Number is Not Happy Number")
