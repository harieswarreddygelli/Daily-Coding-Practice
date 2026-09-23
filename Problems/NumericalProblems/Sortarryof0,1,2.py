def sortarray(arr):
  l,r=0,len(arr)-1
  mid=0
  while m<=r:
    if arr[m]==0:
      arr[l],arr[m]=arr[m],arr[l]
      l+=1
      m+=1
    elif arr[m]==1:
      m+=1
    else:
      arr[r],arr[m]=arr[m],arr[r]
      r-=1
  return arr
arr=list(map(int,input("Enter a array with 0's,1's,2's :").split()))
print("After sorting :",sortarray(arr))
