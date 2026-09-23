def containerwithmostwater(arr):
    l, r = 0, len(arr) - 1
    max_area = 0
    while l < r:
        max_area = max((r-l) * min(arr[l],arr[r]), max_area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return max_area
arr=list(map(int,input("Enter Numbers: ").split()))
print("The maximum Water can be stored is :",containerwithmostwater(arr))
