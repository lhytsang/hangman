import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

    def word(word_list):
        word = random.choice(word_list)

    def word_guessed(word):
        