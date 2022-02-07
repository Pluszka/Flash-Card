from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

root = Tk()
root.title('Flashy')
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, rowspan=2)
canvas_title = canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 40, 'italic'))
canvas_txt = canvas.create_text(400, 263, text='Word', font=(FONT_NAME, 60, 'bold'))
root.mainloop()
