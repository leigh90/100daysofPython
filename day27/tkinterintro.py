# todo import tkinter module (comes with every python installation)
import tkinter
# or
from tkinter import *

# todo initialise a window by calling the class
mywindow = tkinter.Tk()

# todo change the title of the window
mywindow.title('My First GUI')

# todo you can set a minimum width
mywindow.minsize(width=500, height=300)

# todo tkinter labels
my_label = tkinter.Label(text="I am a label", font=("roboto", 16, "normal"))
# my_label.pack(side="bottom")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
my_label['text'] = "new Text"
# my_label.config(text='Long')

# todo tkinter button
def button_clicked():
    print("I got clicked")
    my_label.config(text=answer.get())

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
# command is an event listener

# todo new button
new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

# todo Entry its like input()
answer = Entry(width=15)
# answer.pack(side='left')
answer.grid(column=2, row=2)
# answer.config

# to get what has been passed into the entry you use get()
print(answer.get())

# todo new input
new_answer = Entry(width=10)
new_answer.grid(column=3, row=3)


# # todo tkinter Spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to_=10, width=5, command=spinbox_used)
# spinbox.pack()

# # todo tkinter Scale
# def scale_used(value):
#     print(value)
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # todo tkinter checkbutton
# def checkbutton_used():
#     print(checked_state.get())
# checked_state = IntVar()
# # checkbutton = Checkbutton(text="Is on?", variable)
#
# def radio_used():
#     print(radio_state.get())
#
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)
#
# radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radio_button2.pack()

# todo pack()  place() grid()
# my_label.pack(side='right')
# # place() takes parameter side which you plug with right, left, top, bottom
# my_label.place(x=0, y=0)
# # place() allows you to use coordinates
# my_label.grid(column=0, row=0)
# # grid() uses columns and rows for a more orecise positioning
# todo please note we can't use pack and grid together





mywindow.mainloop()