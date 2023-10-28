import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

    def word(self):
       return random.choice(self.word_list)

    def __len__(self):
        return len(self.word)
    
    def word_guessed(self):
        return ['-'] * self.__len__(self.word)
    
    def num_letters(self):
        unique_letters = 0
        for letter in self.word:
            if letter not in self.word:
                unique_letters +=1
        return unique_letters
    
    def num_lives(self):
        return self.num_lives