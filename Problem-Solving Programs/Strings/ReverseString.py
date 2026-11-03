# Program to reverse a string using slicing
original_string = input("Enter a string: ")

# Program to reverse a string using slicing
# The magic happens here: [start:stop:step]
reversed_string = original_string[::-1]

print("Reversed string:", reversed_string)

# Program to reverse a string using built-in methods
# reversed() flips the sequence, "".join() merges it back into a string
reversed_string = "".join(reversed(original_string))

print("Reversed string:", reversed_string)

# Program to reverse a string manually using a loop
reversed_string = ""

for char in original_string:
    # Adding the character to the front builds the string backwards
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
