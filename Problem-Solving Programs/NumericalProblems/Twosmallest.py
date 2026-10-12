def find_two_smallest(arr):
    # Check if array has fewer than 2 elements
    if len(arr) < 2:
        return "Array must have at least two elements"
        
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    if second_smallest == float('inf'):
        return f"Smallest: {smallest}, Second smallest: Does not exist (all elements are equal)"
        
    return smallest, second_smallest

# Corrected input and print statements
list1 = list(map(int, input("Enter array separate by spaces: ").split()))
print(find_two_smallest(list1))  # Fixed the spelling and variable name
