def BubbleSort(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    return a
            
a=list(map(int,input("Enter Elements Seprated by spaces: ").split()))
print("The Elements after bubble sort:", BubbleSort(a))
