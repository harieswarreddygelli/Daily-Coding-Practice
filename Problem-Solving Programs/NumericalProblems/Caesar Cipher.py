# Read input
text = input().strip()
shift = int(input())

# Encrypt and print
encrypted_chars = []
for char in text:
    new_index = (ord(char) - ord('a') + shift) % 26
    encrypted_chars.append(chr(new_index + ord('a')))

print("".join(encrypted_chars))
