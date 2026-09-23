def missingnumber(arr):
  n=len(arr)+1
  xor_all=0
  for i in range(1,n+1):
    xor_all^=i
  for num in arr:
    xor_all^=num
  return xor_all
arr=list(map(int,input("Enter Numbers: ").split()))
print("The Missing Number in the array :",missingnumber(arr))
