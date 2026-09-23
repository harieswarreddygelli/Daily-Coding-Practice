def rotatearray(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    def rotatea(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
      
    # 3-step array rotation (Right rotation by k)
    rotatea(arr, 0, n - 1)  # Reverse the entire array
    rotatea(arr, 0, k - 1)  # Reverse the first k elements
    rotatea(arr, k, n - 1)  # Reverse the remaining n-k elements
    
    return arr

arr=list(map(int,input("Enter the Array: ").split()))
k=int(input("Enter how many times you want to rotate a Array: "))
print(rotatearray(arr,k))
  
