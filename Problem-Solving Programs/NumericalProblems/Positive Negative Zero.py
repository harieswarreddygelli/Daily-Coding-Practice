def classify_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"
# Read the number

n = float(input())
print(classify_number(n))
