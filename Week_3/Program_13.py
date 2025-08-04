def is_right_triangle(a, b, c):
    # Sort the sides to identify the longest side
    sides = sorted([a, b, c])
    # Check the Pythagorean theorem
    return sides[2]**2 == sides[0]**2 + sides[1]**2

# Input lengths of the sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the triangle is a right triangle
if is_right_triangle(side1, side2, side3):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
