def SelectionSort(a):
    for i in range(len(a)):
        mini=i
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    return a
            
a=list(map(int,input("Enter Elements Seprated by spaces: ").split()))
print("The Elements after Selection  sort:", SelectionSort(a))
