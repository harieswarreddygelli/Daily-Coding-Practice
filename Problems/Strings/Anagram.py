def check_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if check_anagram(s1, s2):
    print("The strings are anagrams!")
else:
    print("The strings are NOT anagrams.")
