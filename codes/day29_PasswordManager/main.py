from tkinter import *
from tkinter import messagebox
import string
import random
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
    
    if website_entry.get() == '' or email_username_entry.get() == '' or password_entry.get() == '':
        messagebox.showinfo(title="Input error", message="You need to fill all boxes")
        return

    is_ok = messagebox.askokcancel(title="Confirm input", 
                                   message=f"""
                                   Website: {website_entry.get()}
                                   Email/Username: {email_username_entry.get()}
                                   Password: {password_entry.get()}\n
                                   Do you want to save?""")
    if is_ok:
        with open("random_file_nothing_suspicious_here.txt", mode='a') as file:
            file.write(f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
        

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
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "b.veiga74@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# ---------- Buttons ----------- #

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
add_button = Button(text="Add", width=39, command=add_password)

generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

# ---------- MainLoop ----------- #

window.mainloop()