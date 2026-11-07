def calculate_circle_properties(radius):
    """Calculates the area and circumference of a circle."""
    # Formulas: Area = πr², Circumference = 2πr
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
if radius < 0:
  print("Error: Radius cannot be negative.")
else:
  # Perform calculations
  area, circumference = calculate_circle_properties(radius)
          # Display the results rounded to 2 decimal places
  print(f"\nResults for a circle with radius {radius}:")
  print(f"  • Area: {area:.2f}")
  print(f"  • Circumference: {circumference:.2f}")
