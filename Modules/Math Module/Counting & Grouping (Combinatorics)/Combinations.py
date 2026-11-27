import math  # Import the built-in math module so we can access math.comb()


def combinations() -> None:
    # Prompt the user for total objects (n) and convert text input to an integer
    n = int(input("Enter the Total Number of Objects: "))
    # Prompt the user for objects to select (r) and convert text input to an integer
    r = int(input("Enter the Number of Objects to be Selected: "))

    # Validate inputs: n and r must be non-negative, and r cannot exceed n
    if n < 0 or r < 0 or r > n:
        print("Invalid input: ensure 0 <= r <= n.")
        return

    # Display the entered values for verification
    print(f"n = {n}, r = {r}")

    # Calculate combinations C(n, r) = n! / (r! * (n - r)!)
    k = math.comb(n, r)

    # Print the resulting combination count a
    print(f"Combinations: {k})")


# Run combinations() only when this file is executed directly (not when imported)
if __name__ == "__main__":
    combinations()