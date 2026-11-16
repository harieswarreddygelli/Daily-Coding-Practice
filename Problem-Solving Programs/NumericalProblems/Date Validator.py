day = int(input())
month = int(input())
year = int(input())

is_valid = True

# Check month and year range
if month < 1 or month > 12 or year < 1:
    is_valid = False
else:
    # Determine maximum days in the given month
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:  # February (month == 2)
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_days = 29 if is_leap else 28

    # Check if day falls within the valid range
    if day < 1 or day > max_days:
        is_valid = False

if is_valid:
    print("Valid")
else:
    print("Invalid")
