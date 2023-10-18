"""
Implement the Caesar position-rotation cipher
"""


def caesar(n, plaintext):
  """
  Rotate each letter of the plaintext by n positions
  """
  
  # Let's assume the plaintext is a string of only capital 
  # letters with no puncuation of spacing

  ciphertext = ''
  
  for letter in plaintext:
    
    # Rotate letter to its matching output character

    # Convert the letter to its alphabet position
    position = ord(letter) - ord('A')
    
    # Rotate by n positions, wrapping around alphabet if necessary (%26)
    position = (position + n) % 26
    
    # Convert back to an output character
    converted_letter = chr(position + ord('A'))

    # Attach converted letter to the output string
    ciphertext += converted_letter

  return ciphertext


### Main

ciphertext = caesar(3, 'THEFOXISINTHEHENHOUSE')
print(ciphertext)