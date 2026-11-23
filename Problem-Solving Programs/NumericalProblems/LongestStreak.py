n = int(input())

numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

if n == 0:
    longest = 0
else:
    current = 1
    longest = 1

    for i in range(1, n):
        if numbers[i] == numbers[i - 1]:
            current = current + 1
        else:
            current = 1

        if current > longest:
            longest = current

print("Longest streak:", longest)