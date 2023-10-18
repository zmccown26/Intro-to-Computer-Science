"""
Read a number from the user and test 
if that number is negative or not
"""

# Get an input from user and change it to integer type 
user_input = input('Enter an integer value: ')
num = int(user_input)

# Test if the number is negative, postive, or equal to 0 
# and print out a message on which one it is
if num < 0:
  print('Negative.')
if num == 0:
  print('Zero.')
if num > 0:
  print('Positive.')