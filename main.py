from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

root = Tk()
root.title('Flashy')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526)
card_front_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas_title = canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 40, 'italic'))
canvas_txt = canvas.create_text(400, 263, text='Word', font=(FONT_NAME, 60, 'bold'))

incorrect_img = PhotoImage(file="./images/wrong.png")
left_button = Button(image=incorrect_img, highlightthickness=0, bg=BACKGROUND_COLOR)
left_button.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
left_button = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR)
left_button.grid(row=1, column=1)

root.mainloop()

