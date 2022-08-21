import random
from tkinter import *
from Pillow import Image, ImageTk
game_control = True

while game_control:
    root = Tk()
    root.geometry('1000x1000')
    root.title('Hackman')
    root.config(bg='#ffffff')
    # put letters into the screen
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    Dict = []
    inc = 0
    while inc < 26:
        Dict.append(ImageTk.PhotoImage(Image.open('Buttons/' + letters[inc] + '.png')))
