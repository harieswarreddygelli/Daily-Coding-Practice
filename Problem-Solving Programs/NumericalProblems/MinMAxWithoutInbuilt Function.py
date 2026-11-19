def find_min_max(numbers):
    if not numbers:
        return None, None  # Handle empty list

    smallest = largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

# Built-in shorthand:
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(find_min_max(nums))          # (-3, 88)
print(min(nums), max(nums))        # -3 88