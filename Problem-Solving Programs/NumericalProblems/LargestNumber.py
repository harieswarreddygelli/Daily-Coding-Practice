def largest(arr):
  largest=arr[0]
  for i in arr:
    if largest<i:
      largest=i
  return largest

arr=list(map(int,input("Enter the Numbers: ").split()))
print("The Largest NUmber in the array is :",largest(arr))
