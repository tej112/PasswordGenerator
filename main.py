from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from json.decoder import JSONDecodeError

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError as e:
            with open('data.json','w') as data_file:
                data=new_data
        except JSONDecodeError:
            data = new_data
        with open('data.json','w') as data_file:
            json.dump(data,data_file,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ---------------------------------#

def search():
    try:
        with open('data.json','r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        open('data.json','w')
        messagebox.showinfo(title='File Not Found',message='No DataBase of password found\nCreate First!')
    except JSONDecodeError:
        messagebox.showinfo(title='No Data',message='Database is Empty.\nStore some passwords to Search')
    else:
        try:
            web = data[website_entry.get()]
        except KeyError:
            messagebox.showinfo(title='Not Found',message='There were no passwords saved for this website.')
        else:
            mail = web['email']
            password = web['password']
            messagebox.showinfo(title='Password',message=f'mail:{mail}\npassword:{password}\nPassword is copied!')
            pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1,sticky='we')
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2,sticky='we')
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1,sticky='we')

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password,width=20)
generate_password_button.grid(row=3, column=2,sticky='ew')
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2,sticky='ew')

search_button = Button(text='Search',command=search,width=20)
search_button.grid(row=1, column=2,sticky='ew')

window.mainloop()
