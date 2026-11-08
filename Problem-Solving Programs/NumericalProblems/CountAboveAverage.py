# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Calculate average and count above
total_sum = 0
for i in numbers:
    total_sum += i

# Use standard division for accurate average
Avg = total_sum / n

above_avg = 0
for i in numbers:
    if i > Avg:
        above_avg += 1

print(f"Above average: {above_avg}")
