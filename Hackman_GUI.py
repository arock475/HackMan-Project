from RandWord import rand_word
from string import ascii_uppercase
from tkinter import *  # for GUI creation

# GUI initialization
root = Tk()
root.geometry('1000x1000')
root.title('Hackman')
root.config(bg='#000000')
root.iconbitmap('../Hackman-Project-main/media/Hackman.ico')

word = rand_word()  # get the objective word
print(word)
num_incorrect_guesses = 0   # tracks the number of incorrect guesses made
guessed_letters = []


def guess(letter):
    global num_incorrect_guesses
    if guessed_letters.count(letter.lower()) == 0: guessed_letters.append(letter.lower())
    else:
        Label(root, text=letter + " has been guessed before, try again").grid(row=10, column=0, columnspan=3)
        return
    text_var = []
    count = 0
    if word.count(letter.lower()) > 0:
        for char in word:
            if char in guessed_letters:
                text_var.append(char)
                count += 1
            else:
                text_var.append('_')
            if count == len(word)-1:
                for widget in root.winfo_children():
                    widget.destroy()
                Label(root, text="GAME OVER, YOU WIN!!!").grid(row=0, column=0)
    else:
        num_incorrect_guesses += 1
        if num_incorrect_guesses == 6:
            for widget in root.winfo_children():
                widget.destroy()
            Label(root, text="GAME OVER, YOU LOSE!").grid(row=0, column=0)

# put the current hangman image on the screen

# put the current state of the objective word on the screen
x = 0
for a in word:
    my_label = Label(root, text="_____ ", fg="#20C20E", bg="black")
    my_label.grid(column=x, row=0)
    x += 1

# put letter buttons into the screen
x, y = 0, 1
for i in ascii_uppercase:
    Button(root, text=i, command=lambda c=i: guess(c), fg="#20C20E", bg="black", padx=30, pady=15).grid(column=x, row=y)
    x += 1
    if x % 8 == 0:
        y += 1
        x = 0

root.mainloop()
