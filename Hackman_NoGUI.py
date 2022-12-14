from RandWord import *


print_incorrect = ["\n +---+\n     |\n     |\n     |\n    ===", "\n +---+\n O   |\n     |\n     |\n    ===",
                   "\n +---+\n O   |\n |   |\n     |\n    ===", "\n +---+\n O   |\n/|   |\n     |\n    ===",
                   "\n +---+\n O   |\n/|\  |\n     |\n    ===", "\n +---+\n O   |\n/|\  |\n/    |\n    ===",
                   "\n +---+\n O   |\n/|\  |\n/ \  |\n    ==="]
guessed_letters = []
# Gets the word using the current functionality to choose a random word
temp = rand_word()
word = temp.strip()
size = len(word)


# prints the letters that have been guessed and the blank spaces that still need to be guessed
def print_after_guess(guessed):
    i = 0
    correct = 0
    for char in word:
        if char in guessed:
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
    incorrect = 0
    correct_letters = 0
    while True:
        print(print_incorrect[incorrect])
        guessed_letters.append(input("Input a lowercase letter to guess\n"))
        inc = print_after_guess(guessed_letters)
        if inc > correct_letters:
            correct_letters = inc
            inc -= inc
        else:
            incorrect += 1
            if(incorrect == 6):
                print(print_incorrect[incorrect])
                print("YOU LOSE :(")
                print(word)
                break
        if correct_letters == size:
            print("YOU WIN!! :)")


if __name__ == "__main__":
    hackman()
