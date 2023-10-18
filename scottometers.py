"""
Convert from miles to Scottometers

1 Scottometer = 1 million miles
"""

# Declare a function that takes an input number and 
# then prints out the result of the conversion

# m is the input parameter to the function

# when you call miles_to_sm and supply it woth an input value
# that input value is assigned to the variable m while the function # executes
def miles_to_sm(m):
  print(m / 1000000)
  


### Main

# Read user input to get a number of miles
miles = float(input('Enter a number of miles: '))

# Call the converter function with num miles as its arguement
miles_to_sm(miles)