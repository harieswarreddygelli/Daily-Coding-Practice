def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Enter a sentence: ")
print(f"Total vowels: {count_vowels(text)}")
