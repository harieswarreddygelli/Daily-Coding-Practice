def UnionElement(arr1,arr2):
  return sorted(list(set(arr1)|set(arr2)))
arr1=list(map(int,input("Enter array1 Elements: ").split()))
arr2=list(map(int,input("Enter array2 Elements: ").split()))
print("The Union Elements are:",UnionElement(arr1,arr2))
