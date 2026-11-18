# Read input
first_name = input().strip()
last_name = input().strip()

# Create username (lowercase, no space)
username = (first_name + last_name).lower()

# Create initials (uppercase first letters)
initials = (first_name[0] + last_name[0]).upper()

# Print results
print("Username:", username)
print("Initials:", initials)
