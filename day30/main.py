from tkinter import *
from tkinter import messagebox
# import pyperclip
import json

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
    new_data = {
        website: { "email": email,"password": password,}
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Invalid Input', message='None of the fields should be empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Here are your details \n Email:{email} \n Password:{password}')
        if is_ok:
            with open('data.json', 'r') as data_file:
                # read json file
                data = json.load(data_file)
                # update json file
                data.update(new_data)

            with open("data.json",'w') as data_file:
                # write json data
                json.dump(data,data_file, indent=4)
                print(data)



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








# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# #Password Generator Project
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)

#     password = "".join(password_list)
#     password_entry.insert(0, password)
#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():

#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
#                                                       f"\nPassword: {password} \nIs it ok to save?")
#         if is_ok:
#             with open("data.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)


# # ---------------------------- UI SETUP ------------------------------- #

# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)

# #Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)

# #Entries
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "angela@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

# # Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)

# window.mainloop()