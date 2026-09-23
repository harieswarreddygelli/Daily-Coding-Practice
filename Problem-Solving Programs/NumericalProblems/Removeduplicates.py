def removeduplicates(arr):
  original=[]
  for i in arr:
    if i not in original:
      original.append(i)
  return original
arr=list(map(int,input("Enter a array: ").split()))
print("The array after removing Duplicates:",removeduplicates(arr))
