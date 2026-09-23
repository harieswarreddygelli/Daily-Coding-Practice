def inversionCount(arr):
    
    n = len(arr) 
    invCount = 0  

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                invCount += 1
            
    return invCount  

arr = list(map(int,input("Enter a array: ").split()))
print("The Inversion count in array is:",inversionCount(arr))
