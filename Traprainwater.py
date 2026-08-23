def maxWater(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    res = 0
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
    for i in range(1, n - 1):
        min_of_2 = min(left[i], right[i])
        res += min_of_2 - arr[i]
    return res

arr=list(map(int,input("Enter Numbers: ").split()))
print("The maximum water that can be stored: ",maxWater(arr))
