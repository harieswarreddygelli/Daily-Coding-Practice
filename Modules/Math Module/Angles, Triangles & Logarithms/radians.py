import math  # Import the built-in math module to access math.radians()


def degrees_to_radians():
    # Prompt the user for an angle in degrees and convert input to float
    deg = float(input("Enter an angle in degrees: "))

    # Print the original degree value 
    print("Degrees:", deg,)
    
    #Converts everyday degrees into radians (required by Python trignometry functions).

    # Convert degrees to radians (returns a float)
    rad = math.radians(deg)

    # Print the converted radian value and its data type (<class 'float'>)
    print("Radians:", rad, type(rad))


# Run degrees_to_radians() only when this script is executed directly
if __name__ == "__main__":
    degrees_to_radians()