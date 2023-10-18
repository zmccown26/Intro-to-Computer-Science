"""
Illustrate giving the user a menu of choices

Key ideas: reading input that corresponds to a fixed set of choices
Then using if statements to select an appropriate actions
"""

# Print a menu of options for user
print('How are you doing today?')
print('1. Good')
print('2. Not good')

# Read user's response
choice = int(input('Enter 1 or 2: '))

# It's possible to combine multiple tests
# Here we want to catch any input that is not 1 or 2
# The OR operator is satisfied if either one or both
# of its tests is true
if choice < 1 or choice > 2:
  print('Invalid entry')
  quit()

# Respond to user's input and print appropriate message
if choice == 1:
  print('I\'m glad you are doing good.')
  print('Stay positive!')
else: 
  print('I\'m sorry to hear that.')
  print('I hope things get better.')