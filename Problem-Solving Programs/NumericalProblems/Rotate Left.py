def RotateLeft(numbers, k):
    nl = len(numbers)
    if nl == 0:
        return numbers
    
    # Handle cases where k is greater than the array length
    k = k % nl
    
    def rotatea(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
        
    # 3-step left rotation algorithm:
    # 1. Reverse the first k elements
    rotatea(numbers, 0, k - 1)
    # 2. Reverse the remaining n-k elements
    rotatea(numbers, k, nl - 1)
    # 3. Reverse the entire array
    rotatea(numbers, 0, nl - 1)
    
    return numbers

# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
k = int(input())

# Rotate left and print the updated list
a=RotateLeft(numbers, k)
for i in range(len(a)):
  print(a[i],end=" ")
