from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password_entry

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)]
        + [random.choice(symbols) for _ in range(nr_symbols)]
        + [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)

    password_list = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password_list)
    pyperclip.copy(password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_new_password():
    global website_entry, email_username_entry, password_entry

    website        = website_entry.get()
    email_username = email_username_entry.get()
    password       = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Field Empty", message="Website Name cannot be Empty!")
        return

    if len(email_username) == 0:
        messagebox.showinfo(title="Field Empty", message="Email / Username cannot be Empty!")
        return

    if len(password) == 0:
        messagebox.showinfo(title="Field Empty", message="Password cannot be Empty!")
        return

    is_ok  = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \n Is it ok to save? ")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
""" Initiate Window """
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

""" Initiate Canvas Widget """
canvas = Canvas(width=200, height=200, highlightthickness=0)
image  = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=0, columnspan=3)

""" Labels, Entries, Buttons """
website_label = Label(text="Website:", font=("Arial", 12, 'normal'))
website_label.grid(row=1, column=0)
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_username_label = Label(text="Email/Username: ", font=("Arial", 12, 'normal'))
email_username_label.grid(row=2, column=0)
email_username_entry = Entry(width=30)
email_username_entry.insert(0, "tantowi675810@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password", font=("Arial", 12, 'normal'))
password_label.grid(row=3, column=0)
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=add_new_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()