from RandWord import *
# tomorrow i need to work on splitting things into more functions
# also need to get the letters that are guessed to be shown each time
# also need to work on a gui
# then an api
# lots of things to do

def hackman():
    word = rand_word()
    correct = False
    guess_word = ""
    guess_word.ljust(len(word))
    word_size = len(word) - 1
    incorrect = 0
    while not correct:
        guess = input("Guess a letter\n")
        count = 0
        for x in word:
            if x == guess:
                count += 1
                word_size -= 1
        if word_size == 0:
            print("You have completed the word and you win YAY!")
            return
        elif count > 0:
            print("correct!\n%s is in the word %d times" %(guess, count))
        else:
            incorrect += 1
            if incorrect > 6:
                print("You Lose :(")
                return


if __name__ == "__main__":
    hackman()
