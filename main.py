from RandWord import *

# tomorrow I need to work on splitting things into more functions
# also need to get the letters that are guessed to be shown each time
# also need to work on a gui
# then an api
# lots of things to do
# my theme is going to be hacking a server, we are finding the password by playing hangman
# so to do this basically want a black screen with green letters
# global variables to simplify things
print_incorrect = ["\n+---+\n    |\n    |\n    |\n   ===", "\n+---+\nO   |\n    |\n    |\n   ===",
                   "\n+---+\nO   |\n|   |\n    |\n   ===", "\n+---+\nO   |\n/|  |\n    |\n   ===",
                   "\n+---+\nO   |\n/|\ |\n    |\n   ===", "\n+---+\nO   |\n/|\ |\n/   |\n   ===",
                   "\n+---+\nO   |\n/|\ |\n/ \ |\n   ==="]
guessed_letters = []
# Gets the word using the current functionality to choose a random word
word = rand_word()
size = len(word)


# prints the letters that have been guessed and the blank spaces that still need to be guessed
def print_after_guess(guessed_letters):
    i = 0
    correct = 0
    for char in word:
        if char in guessed_letters:
            print(word[i], end=" ")
            correct += 1
        else:
            print("_", end=" ")
        i += 1
    return correct


# This function provides the main functionality of the game by calling other smaller functions
def hackman():
    # show the number of letters in the word to allow the player to start guessing
    for x in word:
        print("_", end=" ")
    guess_count = 0
    incorrect = 0
    letters_guessed = 0
    while True:
        print(print_incorrect[incorrect])
        guessed_letters.append(input("Input a lowercase letter to guess\n"))
        inc = print_after_guess(guessed_letters)
        if inc > 0:
            letters_guessed += inc
            inc -= inc
        else:
            incorrect += 1
        if letters_guessed == size:
            print("YOU WIN!! :)")
        guess_count += 1


if __name__ == "__main__":
    hackman()
