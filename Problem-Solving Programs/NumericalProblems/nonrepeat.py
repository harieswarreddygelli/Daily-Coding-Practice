from collections import Counter
def first_non_repeating_char(s: str):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None  
user_str = input("Enter a String: ")
result = first_non_repeating_char(user_str)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("All characters repeat or the string is empty.")
