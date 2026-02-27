from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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
    website.lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------- FIND PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    website.lower()

    try:
        with open("passwords.json", "r") as data_file:
            data =  json.load(data_file)

    except FileNotFoundError:
        with open("passwords.json", "w") as data_file:
            pass
        messagebox.showinfo(title="Oops", message=f"No password found for {website.title()}")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website.title()}", message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Oops", message=f"No password found for {website.title()}")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "ishaangandhi2006@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#Buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(row=1, column=2, sticky="ew")

window.mainloop()
