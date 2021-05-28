BACKGROUND_COLOR = "#B1DDC6"



















































from tkinter import *
from tkinter import messagebox
import json








# ---------------------------- UI SETUP ------------------------------- #

# create the tkinter window
mywindow = Tk()
mywindow.title('Flashy')
mywindow.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

# Todo Create a canvas
canvas = Canvas(width=400, height=400, highlightthickness=0)
# direct tkinter to the image file
canvas.grid(column=1, row=0)

# TODO Front card
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(100,100,image=front_img)

# TODO Back card
back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(100,100,image=back_img)


# TODO right button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img,highlightthickness=0) 
right_button.grid(column=0, row=2)
# TODO left button
left_img = PhotoImage(file="./images/wrong.png")
left_button = Button(image=left_img,highlightthickness=0) 
left_button.grid(column=2, row=2)


mywindow.mainloop()

