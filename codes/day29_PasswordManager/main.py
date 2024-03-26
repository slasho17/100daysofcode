from tkinter import *
from tkinter import messagebox
import string
import random
import json


FILE = "random_file_nothing_suspicious_here.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=15))
    global password_entry
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    global website_entry
    global email_username_entry
    global password_entry
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email_username": email_username,
            "password": password,
        }
    }

    if website == '' or email_username == '' or password == '':
        messagebox.showinfo(title="Input error", message="You need to fill all boxes")
        return

    is_ok = messagebox.askokcancel(title="Confirm input", 
                                   message=f"""
                                   Website: {website}
                                   Email/Username: {email_username}
                                   Password: {password}\n
                                   Do you want to save?""")
    if not is_ok:
        return

    try:
        with open(FILE, mode='r') as file:
            data = json.load(file)
            data.update(new_data)
        
    except FileNotFoundError:
        data = new_data
    
    finally:
        with open(FILE, mode='w') as file:
            json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    global website_entry
    website = website_entry.get()
    try:
        with open(FILE, mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="No entries yet", message="Website not found because there is no entry in this file")
        return
    
    try:
        values = data[website]
    except:
        messagebox.showinfo(title="Entry not found", message="You don't seem to have a password saved for this website yet")
        return
    else:
        messagebox.showinfo(title="Entry found", message=f"""Your {website} credentials:
                            Username/Email = {values["email_username"]}
                            Password = {values["password"]}""")
        

# ---------------------------- UI SETUP ------------------------------- #

# ---------- Window ----------- #
window = Tk()
window.title("Passowrd Manager")
window.config(padx=50, pady=50)

# ---------- Canvas ----------- #
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# ---------- Labels ----------- #
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ---------- Entrys ----------- #
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "b.veiga74@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# ---------- Buttons ----------- #

search_button = Button(text="Search", width=15, command=search_website)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=39, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

# ---------- MainLoop ----------- #

window.mainloop()