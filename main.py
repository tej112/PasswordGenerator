from tkinter import *
from tkinter import messagebox
import string
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    upp= list(string.ascii_uppercase)
    low = list(string.ascii_lowercase)
    dig = list(string.digits)
    chars = list(string.punctuation)
    
    password =  [random.choice(upp) for _ in range(3)]
    password += [random.choice(low) for _ in range(3)]
    password += [random.choice(dig) for _ in range(3)]
    password += [random.choice(chars) for _ in range(3)]
    random.shuffle(password)
    password = ''.join(password)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    mailid = email_entry.get()
    website_name = website_entry.get()
    password = password_entry.get()

    if len(mailid) == 0 or len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title='Warning',message='Fields cannot be empty.')
    else:
        if messagebox.askyesno(title='Save file',message='Are you sure all the fields are correct?'):
            with open('data.txt','a') as file:
                file.write('\n')
                file.write(f'{website_name} | {mailid} | {password}')
            
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            messagebox.showinfo(title='Done!',message='Password has been saved.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=150,height=150)
logo=PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1)

website = Label(text='Website:')
website.grid(row=1,column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2)

email = Label(text='Email/Username:')
email.grid(row=2,column=0)

email_entry = Entry(width=35)
email_entry.insert(END,"you'r_mail@email.com")
email_entry.grid(row=2,column=1,columnspan=2)


password_text = Label(text='Password:')
password_text.grid(row=3,column=0)

password_entry = Entry(width=20)
password_entry.grid(row=3,column=1)

generate = Button(text='Generate Password',command=password_generator)
generate.grid(row=3,column=2,padx=0)

add_button = Button(text='Add',width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()