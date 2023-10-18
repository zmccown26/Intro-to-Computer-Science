# Program to generate random words
import random

def make_word(num_letters):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = ''
    for i in range(num_letters):
        word = word + random.choice(letters) 
    return word
    
num_words = 100     #number of words to generate
num_letters = 3     #number of letters in each word
words_line = 5      #print 5 words per line for readability

for i in range(int(num_words/words_line) ):
    for x in range(words_line - 1):   
        print(make_word(num_letters), end = ' ')
    print(make_word(num_letters))
