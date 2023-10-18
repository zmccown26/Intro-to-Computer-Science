"""
Calculate the area of a circle given its radius
"""

# Import the built-in value of pi from the math library
from math import pi

# Write a statement that assigns a variable named
# radius to the value 5
radius = 5

# Calculate the area
#
# Use ** for exponentiation
area = pi * radius**2

# Formatted printing
#
# print can take a string that contains
# optional format specifiers
#
# %.2f tells Python to print the next variable
# but show only two digits after the decimal place

# There are different types of format specifiers 
# for different types of data 
# however right now we don't care 

print('The area is %.2f' % area)
