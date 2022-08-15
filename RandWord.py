# This is a temporary solution to give a random word to test the game until I write my api
from random import seed
from random import randint


def rand_word():
    word_file = open("wordList.txt", 'r')
    word_list = word_file.readlines()
    seed(1)
    word = randint(0, 852)
    return word_list[word]
