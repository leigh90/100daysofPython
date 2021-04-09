# todo import tkinter module (comes with every python installation)
import tkinter

# todo initialise a window by calling the class
mywindow = tkinter.Tk()

# todo change the title of the window
mywindow.title('My First GUI')

# todo you can set a minimum width
mywindow.minsize(width=500, height=300)

# todo tkinter labels
my_label = tkinter.Label(text="I am a label", font=("roboto", 16, "normal"))
my_label.pack(side="bottom")




mywindow.mainloop()