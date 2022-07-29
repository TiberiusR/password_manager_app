from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for n in range(randint(8, 10))]
    symbols_list = [choice(symbols) for x in range(randint(2, 4))]
    numbers_list = [choice(numbers) for y in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password_join = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password_join)
    pyperclip.copy(password_join)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        website_input.delete(0, END)
        password_entry.delete(0, END)


# --------------------------- SEARCH ---------------------------------- #


def find_password():
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
            email = data[website_input.get()]["email"]
            password = data[website_input.get()]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="File Not Found.")
    except KeyError:
        messagebox.showinfo(title="Data Not Found", message="This Data doesn't exist.")
    else:
        messagebox.showinfo(title=website_input.get(), message=f"Email: {email} \nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(END, "email@email.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)

window.mainloop()
