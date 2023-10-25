check_letter = True

while check_letter == True:
    guess = input("Please enter a single letter: ")
    if guess.isalpha() and len(guess) == 1:
        print("Good guess!")
        check_letter = False
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")