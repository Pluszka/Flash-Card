from tkinter import *
import pandas
import random
# Buttons func
SEC = 3000
new_word = []


def next_word():
    global flip_timer, new_word, words
    root.after_cancel(flip_timer)
    new_word = random.choice(words)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(canvas_title, text='French', fill='black')
    canvas.itemconfig(canvas_txt, text=new_word['French'], fill='black')
    flip_timer = root.after(SEC, translation)


def translation():
    global new_word
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(canvas_title, text='English', fill='white')
    canvas.itemconfig(canvas_txt, text=new_word['English'], fill='white')


def known_word():
    global new_word
    words.remove(new_word)
    new_data = pandas.DataFrame(words)
    new_data.to_csv('data/You should review those words.csv', index=False)
    next_word()


# Data
try:
    words = pandas.read_csv('data/You should review those words.csv.csv')
except FileNotFoundError:
    words = pandas.read_csv('data/french_words.csv')
finally:
    words = words.to_dict(orient="records")
# UX
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

root = Tk()
root.title('Flashy')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(SEC, translation)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526)
card_back_img = PhotoImage(file='./images/card_back.png')
card_front_img = PhotoImage(file='./images/card_front.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas_title = canvas.create_text(400, 130, text='Title', font=(FONT_NAME, 40, 'italic'))
canvas_txt = canvas.create_text(400, 263, text='Word', font=(FONT_NAME, 60, 'bold'))

incorrect_img = PhotoImage(file="./images/wrong.png")
left_button = Button(image=incorrect_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
left_button.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
left_button = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_word)
left_button.grid(row=1, column=1)

next_word()

root.mainloop()
