from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_but():

    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops!", message="Please make sure you haven't left any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it OK to save? ")

        if is_ok:
            with open('Passwords.txt', 'a') as f:
                f.write(f"{website} | {email} | {password} \n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Image

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website: ")
web_label.grid(row=1,column=0)

Email_username_label = Label(text="Email/Username: ")
Email_username_label.grid(row=2,column=0)

Pass_label = Label(text="Password: ")
Pass_label.grid(row=3,column=0)

#Buttons

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.config(width=21)
gen_button.grid(row=3,column=2)

add_button = Button(text="Add")
add_button.config(width=50, command=add_but)
add_button.grid(row=4,column=1, columnspan=2)

#Entries

web_entry = Entry(width=59)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

user_entry = Entry(width=59)
user_entry.grid(row=2, column=1,columnspan=2)
user_entry.insert(0, "example@gmail.com")

pass_entry = Entry(width=33)
pass_entry.grid(row=3, column=1)

window.mainloop()