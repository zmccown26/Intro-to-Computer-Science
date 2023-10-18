"""
Read a number of bitcoins from the user and convert to USD
"""

# Key idea: special built-in input function that will read 
# what the user types at the console

user_input = input('Enter a number of bitcoins: ')

# The value returned by input is ALWAYS A STRING TYPE

# Even if the user inputs a number, Python returns it as a string

# To do math on an input you must convert it to an int or float

bitcoins = float(user_input)

# Finish program by converting num of bitcoins to USD

# Use ALL CAPS to indacate that a value is a 
# constant and shouldn't be changed
DOLLARS_PER_BITCOIN = 22733
usd = bitcoins * DOLLARS_PER_BITCOIN

print('That is %.2f dollars' % usd)