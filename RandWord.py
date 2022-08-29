# This is a temporary solution to give a random word to test the game until I write an api
import random
import requests
import json


# open the file that contains a list of words and choose a random one
def rand_word():
    URL = 'http://arock475.pythonanywhere.com'
    output = requests.get(URL)

    json_vals = output.json()
    word = json_vals['output']
    return word
