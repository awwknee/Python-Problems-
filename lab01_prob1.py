"""
CISC 131 Problem 1 - Rajani Lamichhane (lami5034)
"""

print("Enter the first value:  ", end="")
x = int(input())
print("Enter the second value: ", end="")
y = int(input())
print("Enter the third value:  ", end="")
z = int(input())
print("Original values: x={:d}, y={:d}, z={:d}".format(x, y, z))

# Write code to "rotate" values here

x_rotate = x
y_rotate = y
z_rotate = z
x = y_rotate
y = z_rotate
z = x_rotate

# Do NOT change code for the print statements
print("Rotated values: x={:d}, y={:d}, z={:d}".format(x, y, z))
