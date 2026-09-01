def Countsort(a):
    maxx=max(a)
    counts=[0]*(maxx+1)
    for x in a:
        counts[x]+=1
    i=0
    for c in range(maxx+1):
        while counts[c]>0:
            a[i]=c
            i+=1
            counts[c]-=1
            
    return a
a=list(map(int,input("Enter Elements seperated by Spaces: ").split()))
print("The elements after Counting Sort:",Countsort(a))
