import math  # Import the built-in math module to access math.fsum()


def sum_user_numbers() -> None:
    numbers: list[float] = []  # Initialize an empty list to store entered numbers

    # Ask how many numbers the user wants to enter
    count = int(input("How many numbers do you want to sum? "))

    # Loop 'count' times to collect each number from the user
    for i in range(count):
        # Convert input to float so both integers and decimals work
        value = float(input(f"Enter number {i + 1}: "))
        # Append the number to the list
        numbers.append(value)

    # Display the collected list and its data type
    print("Numbers:", numbers, type(numbers))

    # Calculate the high-precision floating-point sum using math.fsum()
    total = math.fsum(numbers)

    # Print the sum and its data type (<class 'float'>)
    print("Sum:", total, type(total))


# Execute sum_user_numbers() only when this file is run directly
if __name__ == "__main__":
    sum_user_numbers()