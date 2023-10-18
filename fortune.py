"""
Write a program that outputs a random message
every time that it's run

Key idea: using random num generation to make choices 
in a program; that need to make more than two choices
"""

# Import the random module
from random import random, randint


# random genertaes a uniform fractional number in range [0, 1)
u = random()
print(u)

# Use random() with 5 different options
if u < 1/5:
  print('Stay hydrated.')
elif u < 2/5:
  print('Drink water.')
elif u < 3/5:
  print('Cmon.')
elif u < 4/5:
  print('Dude drink some wata')
else:
  print('Yup.')