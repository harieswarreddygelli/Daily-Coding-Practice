def IntersectSortedArray(arr1,arr2):
  i,j=0,0
  intersection=[]
  while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
      i+=1
    elif arr1[i]>arr2[j]:
      j+=1
    else:
      intersectin.append(arr1[i])
      i+=1
      j+=1
  return Intersection
arr1=list(map(int,input("Enter Array1 Elements: ").split()))
arr2=list(map(int,input("Enter Array2 Elements: ").split()))
arr1.sort()
arr2.sort()
print("The Common Elements in both Arrays are:",IntersectSortedArray(arr1,arr2))
