from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

root = Tk()
root.title('Flashy')
root.config(bg=BACKGROUND_COLOR, padx=40, pady=40)

canvas = Canvas(bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='./images/card_front.png')
canvas.create_image(300, 300, image=card_front)
canvas.grid(row=0, column=0, rowspan=2)
canvas_title = canvas.create_text(190, 100, text='Title', font=(FONT_NAME, 15, 'italic'))
canvas_txt = canvas.create_text(190, 150, text='Word', font=(FONT_NAME, 25, 'bold'))
root.mainloop()
