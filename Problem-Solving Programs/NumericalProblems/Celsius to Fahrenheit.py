# Read celsius from input
celsius = int(input())

# Calculate fahrenheit using the correct variable name
f = celsius * (9 / 5) + 32

# Print the results with the correct float specifier (.1f)
print(f"{celsius} Celsius = {f:.1f} Fahrenheit")
