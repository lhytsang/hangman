import random

word_list = ['passion fruit', 'mango', 'raspberry', 'orange', 'banana']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please enter a single letter: ")

if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input." )
