"""
Demonstrate letter frequency counting 
"""


# Tip: USE THIS FOR NEXT CHALLENGE PROJECT

# Decode a ,essage that I've encrypted using a substitution cipher; perform 
# frequency analysis, play around with the output to figure what the 
# substitution rules are



def analyze(text):
  """
  Count up the occurences of each character in text and print them out
  """
  
  frequencies = {}

  for ch in text:

    # Make a new entry for character ch in frequencies 
    # if it doesn't already have one
    if ch not in frequencies:
      frequencies[ch] = 0
  
    # Increment the count associated with ch
    frequencies[ch] += 1

  # For Python, keys are usually returned in the order they were inserted
  for key in frequencies:
    print(key, frequencies[key])


### Main
analyze('The quick brown fox jumps over the lazy dog.')