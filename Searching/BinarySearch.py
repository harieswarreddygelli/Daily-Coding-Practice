def binarySearch(a, target):
    low = 0
    high = len(a) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

a = sorted(list(map(int, input("Enter elements separated by spaces: ").split())))
target = int(input("Enter the element you want to find: "))

result = binarySearch(a, target)
if result != -1:
    print(f"Element found at index position: {result}")
else:
    print("Element not found in the list.")
