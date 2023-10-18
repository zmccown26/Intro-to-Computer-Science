"""
Cho-han dice game

Roll two dice and add their sum
The pkayer bets on whether the sum is even or odd

Combines all of our ideas so far:
user input
random generation
if statements
logical operators

You may need to tweak the printed output to match 
what assignment e expects

Look at posted solution on Github for reference
"""

from random import randint, seed

# The seed function sets the state of the random number generator 
# For a given starting seed, the generator always produces the
# same sequence of random values every time it's run
# This is useful, because it allows us to test programs that
# have randomness and still get predictable behavior
#
# when you look at the files, you may see calls to seed at
# the beginning of a file -- don't change that number or you won't
# pass the tests
seed(0)

# 1. Print a welcome message and options for the player
print('Welcome to cho-han.')
print()
print('1. Even')
print('2. Odd')
print()

# 2. Read the players choice
choice = int(input('Select a bet: '))
if (choice > 0) and (choice < 3):
  print('Good luck!')
else:
  print('Invalid entry')
  quit()

# 3. Generate a random roll of two dice
die1 = randint(1, 6)
die2 = randint(1, 6)
roll = die1 + die2

print()
print('The dice are %d and %d.' % (die1, die2))
print('The sum is %d.' % roll)
print()
# 4. Use the combination of players choice and 
#    die roll to determine if player wins or loses

# Two ways to win

if choice == 1 and roll % 2 == 0:
  print('You win.')
elif choice == 2 and roll % 2 == 1:
  print('You win.')
else:
  print('You lose.')