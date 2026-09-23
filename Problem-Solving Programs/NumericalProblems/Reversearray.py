def Reverse(arr):
  i,j=0,len(arr)-1
  while i<=j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
  return arr
arr=list(map(int,input("Enter Numbers: ").split()))
print("The Reversed array is:",Reverse(arr))
