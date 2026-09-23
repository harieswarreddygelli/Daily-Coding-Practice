def subarraysum(arr,taget):
  i=0
  currsum=0
  for j in range(len(arr)):
    currsum+=arr[j]
    while currsum>target and i<=j:
      currsum-=arr[i]
      i+=1
    if currsum==target:
      return [i,j]
  return -1
arr=list(map(int,input("Enter a array: ").split()))
target=int(input("Enter the sum you want to find in the sub array:"))
print("The indices are: ",subarraysum(arr,target))
