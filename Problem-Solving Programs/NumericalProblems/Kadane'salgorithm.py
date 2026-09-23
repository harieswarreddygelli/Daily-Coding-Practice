def maxSubarraySum(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
            maxEnding = max(maxEnding + arr[i], arr[i])
            res = max(res, maxEnding)
    return res
arr=list(map(int,input("Enter a array: ").split()))
print("The maximum sum of sub array is :",maxSubarraySum(arr))
