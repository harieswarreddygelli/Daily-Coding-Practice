def rearrange(arr):
    arr.sort()
    li=[]
    l,r=0,len(arr)-1
    while l<=r:
        li.append(arr[r])
        li.append(arr[l])
        l+=1
        r-=1
    return li
arr=list(map(int,input("Enter Numbers: ").split()))
print(rearrange(arr))
