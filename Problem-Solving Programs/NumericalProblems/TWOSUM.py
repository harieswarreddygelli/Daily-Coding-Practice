def two_sum_two_pointer(nums, target):
    # Pair each number with its original index and sort by the number value
    indexed_nums = sorted((num, idx) for idx, num in enumerate(nums))
    
    # Initialize pointers at both ends of the sorted list
    left = 0
    right = len(indexed_nums) - 1
    
    while left < right:
        # Extract values using index [0] of the tuples
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return the original indices stored at index [1] of the tuples
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            # Sum is too small, move the left pointer to increase the sum
            left += 1
        else:
            # Sum is too large, move the right pointer to decrease the sum
            right -= 1
            
    return []  # Return empty list if no pair matches the target

# Example Usage:
# Fixed the missing brackets and the .split() spelling mistake
nums_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
target_val = int(input("Enter Target value: "))
print(two_sum_two_pointer(nums_list, target_val))
