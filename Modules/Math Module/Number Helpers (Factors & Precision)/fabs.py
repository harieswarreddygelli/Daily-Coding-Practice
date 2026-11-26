import math  # Import the built-in math module to access math.fabs()


def fabs_value() -> None:
    # Prompt the user for a number and convert the input string to an integer
    N = int(input("Enter a Number: "))

    # Print the original integer and its data type (<class 'int'>)
    print(N, type(N))

    # Compute the absolute value using math.fabs(), which always returns a float
    k = math.fabs(N)

    # Print the resulting absolute value and its data type (<class 'float'>)
    print(k, type(k))


# Execute fabs_value() only when this script is run directly
if __name__ == "__main__":
    fabs_value()