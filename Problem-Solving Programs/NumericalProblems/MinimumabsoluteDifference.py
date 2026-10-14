import math
import itertools

def minimumAbsDifference(arr):
    arr.sort()
    ans = []
    mn = math.inf
    
    for a, b in itertools.pairwise(arr):
        diff = b - a
        if diff < mn:
            mn = diff
            ans = [[a, b]]
        elif diff == mn:
            ans.append([a, b])
            
    return ans

arr=list(map(int,input().split()))
print(minimumAbsDifference(arr))
