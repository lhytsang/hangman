import random, sys

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
            self.list_of_guesses.append(guess)
            print(f"Good guess! {guess} is in the word")

            indices = []
            for position in range(len(self.word)):
                if self.word[position] == guess:
                    indices.append(self.word.index(guess, position, len(self.word)))
                else:
                    continue

            for index in indices:
                self.word_guessed[index] = guess
            
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. \n You have {self.num_lives} lives left.")
   
    def ask_for_input(self):
        while "-" in self.word_guessed:
            guess = input("Please enter a single letter: ")
                
            if not(guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

word_list = ["passion fruit", "mango", "raspberry", "orange", "banana"]

def play_game(word_list):
    num_lives = 5
    
    while num_lives >= 0:
        game = Hangman(word_list, num_lives)
        if num_lives == 0:
            print("You lost!")
            sys.exit(0)
        if game.num_letters > 0:
            game.ask_for_input()
        if num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!") 
            sys.exit(0)

play_game(word_list)