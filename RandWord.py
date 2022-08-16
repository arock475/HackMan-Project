# This is a temporary solution to give a random word to test the game until I write an api
import random


# open the file that contains a list of words and choose a random one
def rand_word():
    word_file = open("wordList.txt", 'r')
    word_list = word_file.readlines()
    return random.choice(word_list)

