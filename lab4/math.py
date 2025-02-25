#1 
import math

# Function to convert degrees to radians
def result(degrees):
    return degrees * (math.pi / 180)

# Input from user
degrees = float(input("Input degree: "))

# Convert to radians
radians = result(degrees)

# Print result
print(f"Output radian: {radians:.6f}")  # Formatting to 6 decimal places

#2
import math
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
S =((base1+base2)/2)*height
print(S)

#3
import math

# Input number of sides and length of a side
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

# Calculate the area
if n == 4:
    area = s ** 2  # Special case for a square
else:
    area = (n * s**2) / (4 * math.tan(math.pi / n))

# Display the result
print("The area of the polygon is:", area)

#4
# Input base length and height
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

# Calculate area
area = base * height

# Display the result
print("The area of the parallelogram is:", area)
