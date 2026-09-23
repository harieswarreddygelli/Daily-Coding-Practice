def is_palindrome(s):
    return s == s[::-1]  
user_str = input("Enter a String: ")
print("The String is palindrome" if revstr(user_str) else "The String is not a palindrome")
