# Ask the user for the width and height
# (assume they put imn valid data)
width = float(input("width: "))
height = float(input("height: "))

# calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")