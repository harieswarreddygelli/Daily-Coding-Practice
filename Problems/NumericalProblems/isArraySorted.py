def isarraysorted(arr):
  for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
  

arr=list(map(int,input("Enter The Numbers:").split()))
if isarraysorted(arr):
  print("The array is sorted")
else:
  print("The array is unsorted")
  
