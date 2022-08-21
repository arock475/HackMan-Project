from RandWord import rand_word
import string
from tkinter import *

game_control = True

# GUI initialization
root = Tk()
root.geometry('1000x1000')
root.title('Hackman')
root.config(bg='#000000')
root.iconbitmap('../Hackman-Project-main/media/Hackman.ico')

# get the objective word
word = rand_word()


def temp(letter):
    temp_label = Label(root, text="clicked " + letter)
    temp_label.grid(row=5, column=0)


while game_control:
    # put the current hangman image on the screen

    # put the current state of the objective word on the screen
    x = 0
    for a in word:
        my_label = Label(root, text="_____ ", fg="#20C20E", bg="black")
        my_label.grid(column=x, row=0)
        x += 1
    # put letter buttons into the screen
    letters = list(string.ascii_uppercase)
    i, x, y = 0, 0, 1
    while i < 26:
        button = Button(root, text=letters[i], command=lambda i=i: temp(letters[i]), fg="#20C20E", bg="black", padx=30,
                        pady=15)
        button.grid(column=x, row=y)
        i += 1
        x += 1
        if x % 8 == 0:
            y += 1
            x = 0

    game_control = False

root.mainloop()
