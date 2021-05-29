from tkinter import *

my_window = Tk()
my_window.title('Mile to KM Converter')
my_window.minsize(width=500, height=300)

# todo Miles Input
miles_input = Entry(width=15)
miles_input.grid(column=3, row=2)

# TODO LABELS
# todo Miles Label
miles_label = Label(text='Miles',font=("roboto", 16, "normal"))
miles_label.grid(column=4, row=2)

# todo isequalto label
equal_to = Label(text='is equal to',font=("roboto", 16, "normal"))
equal_to.grid(column=1, row=3)

# todo conversion label
conversion = Label(text='0',font=("roboto", 16, "normal"))
conversion.grid(column=2, row=3)

# todo KM label
kilo_label = Label(text='KM',font=("roboto", 16, "normal"))
kilo_label.grid(column=3, row=3)

# todo calculate button
def calculate():
    miles = miles_input.get()
    print(miles)
    kilometers  = int(miles) * 1.609
    print(kilometers)
    conversion.config(text=str(kilometers))

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=4)

my_window.mainloop()






