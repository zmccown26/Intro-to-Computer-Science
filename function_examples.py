"""
Examples of functions
"""
from math import pi

# Function Ex1
def print_area_of_circle(radius):
  """
  Print the area of the circle with given radius
  """

  area = radius ** 2 * pi
  print(area)


# Function Ex2
def print_max(a, b):
  """
  Print the maximum of the two inputs a and b
  """

  if a > b:
    print(a)
  else:
    print(b)


# Function Ex3
def return_area_of_circle(radius):
  """
  Calculate and return the area of the circle with the given radius
  """

  area = radius ** 2 * pi

  # The return keyword tells Python to send trhe specifed value
  # back as the output of the function
  return area


# Function Ex4
def return_max(m, n):
  """
  Return maximum of two inputs
  """

  # 
  if m > n:
    return m
  else:
    return n




### Main

# Function Ex1 
print_area_of_circle(1)

print_area_of_circle(20) 


# Function Ex2
print()
print_max(101, 111)
print_max(12, 9)


# Function Ex3

# When using key word 'return' you almost always assign the function to a variable
  # Key idea: Python evaluates the function call on the right hand side
  # Whatever the function returns is assigned to the variable on the left side
a = return_area_of_circle(100)
print()
print(a)


# Function Ex4
max_of_x_and_y = return_max(101, 111)
print()
print(max_of_x_and_y)