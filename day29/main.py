from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    # new_list = [(operation to achieve new_item) for item in input(the iteration could be range, for loop)]
    nrletters = [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    nrsymbols = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    nrnumbers = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]


    random.shuffle(password_list)
    password = ''.join(password_list)

    print(f"Your password is: {password}")
    site_password.insert(0,f'{password}')
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credential():
    website = webpage.get()
    email = credential.get()
    password = site_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Invalid Input', message='None of the fields should be empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Here are your details \n Email:{email} \n Password:{password}')
        if is_ok:
            with open('data.txt', 'a') as file:
                file.writelines(f'{website.title()} | {email} | {password}\n')
            webpage.delete(0,END)
            site_password.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

# create the tkinter window
mywindow = Tk()
mywindow.title('Password Manager')
mywindow.config(padx=20, pady=20)

# Todo Create a canvas
canvas = Canvas(width=200, height=224, highlightthickness=0)
# direct tkinter to the image file
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

#TODO Labels
# todo website label
website_label = Label(text='Website:', font=('roboto', 16, "normal"))
website_label.grid(column=0, row=1)

# todo webpage its like input()
webpage = Entry(width=35)
# answer.pack(side='left')
webpage.grid(column=1, row=1, columnspan=2)
webpage.focus()

# todo Email/username label
credential_label = Label(text='Email/Username:', font=('roboto', 16, "normal"))
credential_label.grid(column=0, row=2)

# todo Entry its like input()
credential = Entry(width=35)
# answer.pack(side='left')
credential.grid(column=1, row=2, columnspan=2)
credential.insert(0,'ashdev@gmail.com')

# TODO Password label
# todo password label
pass_label = Label(text='Password:', font=('roboto', 16, "normal"))
pass_label.grid(column=0, row=3)

# todo password its like input()
site_password = Entry(width=35)
site_password.grid(column=1, row=3)

# TODO password button
gen_password = Button(text="Generate Password",highlightthickness=0, command=generate_password)
gen_password.grid(column=3, row=3)

# TODO add button

add_credential = Button(text="Add Credential",highlightthickness=0, command=add_credential)
add_credential.grid(column=1, row=4, columnspan=2)



mywindow.mainloop()