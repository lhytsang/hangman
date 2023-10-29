import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['-'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self.guess_list.append(guess)
            print(f"Good guess! {guess} is in the word")

            for letter in self.word:
                indices = [self.word.index(letter, position, len(self.word)) for position in range(len(self.word)) if letter == guess]
                self.word_guessed = [self.word_guessed[num] == guess for num in indices]
            
            self.num_letters -= 1
   
    def ask_for_input(self):
        check_letter = True

        while check_letter == True:
            guess = input("Please enter a single letter: ")
            
            if not(guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(guess)
                self.list_of_guesses.append(guess)
