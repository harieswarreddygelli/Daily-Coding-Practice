# Calculate the sum of squares from 1 to N.
# Read N
n = int(input())
sum_Square=0
# Calculate and print sum of squares
for i in range(1,n+1):
  sum_Square+=i*i
  
print(f"Sum: {sum_Square}")
