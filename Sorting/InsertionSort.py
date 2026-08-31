def insertionsort(a):
    if len(a)<=1:
        return 
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j + 1] = a[j]
            j -= 1
        a[j+1]=key
    return a
            
a=list(map(int,input("Enter Elements Seprated by spaces: ").split()))
print("The Elements after insertion  sort:", insertionsort(a))
