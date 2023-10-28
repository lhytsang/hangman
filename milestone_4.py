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
    
    def word_list(self):
        return self.word_list
    
    def list_of_guesses(self, guess):
        guess_list = []
        
        if guess in self.word:
            if guess not in self.word_guessed:
                self.word_guessed.append(guess)
                print(f"Great choice - your letter is in the word! \n {self.word_guessed}")
                guess_list.append(guess)
            else:
                print('You have already guessed this letter! \n ',
                      'Here are the letters you have already guessed: \n',
                       '{}'.format(self.list_of_guesses))
        else:
            self.num_lives -= 1
            print(f"Sorry - wrong choice! You have {self.num_lives} left.")
            guess_list.append(guess)
            
