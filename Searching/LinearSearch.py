def linearSearch(a,target):
  for i in range(len(a)):
    if a[i]==target:
      return i
  return -1
a=lis(map(int,input("Enter elements seprated by spaces:").split()))
target=int(input("Enter the element you want to find:"))
print("the element found at :",linearSearch(a),"position")
  
