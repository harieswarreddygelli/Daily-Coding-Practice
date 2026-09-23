def movezeros(arr):
  l=0
  for i in range(len(arr)):
    if arr[i]!=0:
      arr[i],arr[l]=arr[l],arr[i]
      l+=1
  return arr
arr=list(map(int,input("Enter Numbers: ").split()))
print("The Array after MOving zeros to end:",movezeros(arr))
