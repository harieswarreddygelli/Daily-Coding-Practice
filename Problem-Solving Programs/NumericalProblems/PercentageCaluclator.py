original = float(input("Enter the original value: ").strip())
new_val = float(input("Enter the new value: ").strip())

if original == 0:
    print("\nError: Original value cannot be zero.\n")
else:
    change = ((new_val - original) / original) * 100  
    if change > 0:
        print(f"\nResult: Percentage Increase of {change:.2f}%\n")
    elif change < 0:
        print(f"\nResult: Percentage Decrease of {abs(change):.2f}%\n")
    else:
        print("\nResult: No change (0%)\n")
