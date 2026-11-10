def power(base, exp):
    result = 1
    # Calculate base^exp using a loop
    for _ in range(exp):
        result *= base
    return result

base = int(input())
exp = int(input())
print("Result: " + str(power(base, exp)))