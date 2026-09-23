def findduplicate(arr):
  count=Counter(arr)
  for i,j in count.items():
    if j>1:
      return i
arr=list(map(int,input("Enter Numbers: ").split()))
print("The duplicate in the Array is:",findduplicate(arr))
