import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("=== Study Math Tool ===")
print(f"Area of circle (radius = 5): {calculate_circle_area(5):.2f}")
print(f"Hypotenuse (sides = 3, 4): {calculate_hypotenuse(3, 4)}")