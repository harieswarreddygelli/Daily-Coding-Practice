# Read the number
n = int(input())

# Count steps to reach 1
c=0
while n!=1:
  if n%2==0:
    n=n//2
    c+=1
  else:
    n=n*3+1
    c+=1
    
print(f"Steps: {c}")