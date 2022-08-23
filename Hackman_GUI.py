from RandWord import rand_word
from string import ascii_uppercase
from tkinter import *  # for GUI creation

# GUI initialization
root = Tk()
root.geometry('1000x1000')
root.title('Hackman')
root.config(bg='#000000')
root.iconbitmap('../Hackman-Project-main/media/Hackman.ico')

# grid configuration
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.columnconfigure(9, weight=1)
root.columnconfigure(10, weight=1)
root.columnconfigure(11, weight=1)

root.rowconfigure(0, weight=6)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

bad_word = rand_word()  # get the objective word
word = bad_word.strip()
num_incorrect_guesses = 0  # tracks the number of incorrect guesses made
guessed_letters = []  # tracks the letters that have been guessed
hackman_images = [PhotoImage(file="media/Hackman0.png"), PhotoImage(file="media/Hackman1.png"),
                  PhotoImage(file="media/Hackman2.png"), PhotoImage(file="media/Hackman3.png"),
                  PhotoImage(file="media/Hackman4.png"), PhotoImage(file="media/Hackman5.png"),
                  PhotoImage(file="media/Hackman6.png")]
string = StringVar()


# put the current hangman image on the screen
def show_hackman():
    Label(root, image=hackman_images[num_incorrect_guesses]).grid(row=0, column=2, columnspan=4)


def guess(letter, index):
    button_list[index].config(state="disabled")
    global num_incorrect_guesses
    guessed_letters.append(letter.lower())
    text_var = []
    count = 0

    if word.count(letter.lower()) > 0:
        letter_count = 0
        for char in word:
            if char in guessed_letters:
                text_var.append(char)
                word_labels[letter_count].config(text=char.upper(), font=('Arial', 40))
                count += 1
            else:
                text_var.append('_')
            if count == len(word) - 1:
                for widget in root.winfo_children():
                    widget.destroy()
                Label(root, text="GAME OVER, YOU WIN!!!", fg="#20C20E", bg="black").grid(row=0, column=0)
                Label(root, text="The word was " + word, fg="#20C20E", bg="black").grid(row=1, column=0)
            letter_count += 1
    else:
        num_incorrect_guesses += 1
        show_hackman()
        if num_incorrect_guesses == 6:
            for widget in root.winfo_children():
                widget.destroy()
            Label(root, image=hackman_images[6]).grid(row=0, column=0)
            Label(root, text="GAME OVER, YOU LOSE!", fg="#20C20E", bg="black").grid(row=1, column=0)
            Label(root, text="The word was "+word, fg="#20C20E", bg="black").grid(row=2, column=0)


# put original hangman on screen
Label(root, image=hackman_images[0]).grid(row=0, column=2, columnspan=4)
# put the current state of the objective word on the screen
x = 0
word_labels = []
for a in word:
    word_labels.append(Label(root, text="_____ ", fg="#20C20E", bg="black", font="Arial"))
    word_labels[x].grid(column=x, row=1)
    x += 1

# put letter buttons into the screen
x, y, a = 0, 2, 0
button_list = []
for i in ascii_uppercase:
    button_list.append(Button(root, text=i, command=lambda c=i, index=a: guess(c, index),
                              fg="#20C20E", bg="black", padx=30, pady=15))
    button_list[a].grid(column=x, row=y)
    x += 1
    if x % 8 == 0:
        y += 1
        x = 0
    a += 1

root.mainloop()
