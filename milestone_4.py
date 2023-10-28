import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

    def word(word_list):
       return random.choice(word_list)

    def __len__(self, word):
        return len(self.word)
    
    def word_guessed(word):
