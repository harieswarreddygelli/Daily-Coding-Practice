def is_valid(s: str) -> bool:
    bracket_map = {")": "(", "}": "{", "]": "["}
    # Create a set of valid opening brackets for quick lookup
    opening_brackets = set(bracket_map.values())
    stack = []

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        elif char in opening_brackets:
            # Only push onto the stack if it's a valid opening bracket
            stack.append(char)
        else:
            # Ignore spaces, letters, numbers, etc.
            continue

    return len(stack) == 0

user_input = input("Enter a string of brackets: ")
print(is_valid(user_input))
