import random

word_list = ['passion fruit', 'mango', 'raspberry', 'orange', 'banana']
word = random.choice(word_list)

check_letter = True

while check_letter == True:
    guess = input("Please enter a single letter: ")
    if guess.isalpha() and len(guess) == 1:
        print("Good guess!")
        check_letter = False
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again." )