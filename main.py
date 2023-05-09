from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    new_data = {

        website:{
            "email": email,
            "password": password,
        }
                }

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops!", message="Please make sure you haven't left any fields empty!")

    else:
        try:
            with open('Passwords.json', 'r') as file:
                #Read old data
                data = json.load(file)

        except FileNotFoundError:
            with open('Passwords.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            # Update data with new data
            data.update(new_data)

            with open('Passwords.json', 'w') as file:
                #save updated data
                json.dump(data, file, indent=4)

        finally:
            #Delete entries
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def search_button():
    website = web_entry.get()

    try:
        with open('Passwords.json', 'r') as file:
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
            print(email)
            print(password)

    except FileNotFoundError:
        messagebox.showerror(title="Error",
                             message="No data file found.")

    except KeyError:
        messagebox.showerror(title=f"{website} not found!", message=f"Website {website} was not found in the manager, are you sure you spelled it correctly?")

    else:
        messagebox.showinfo(title=f"{website}", message=f"Email:{email} \n Password: {password}")


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
search_button = Button(text="Search", command=search_button)
search_button.config(width=21)
search_button.grid(row=1,column=2)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.config(width=21)
gen_button.grid(row=3,column=2)

add_button = Button(text="Add")
add_button.config(width=50, command=add_but)
add_button.grid(row=4,column=1, columnspan=2)

#Entries

web_entry = Entry(width=32)
web_entry.grid(row=1, column=1)
web_entry.focus()

user_entry = Entry(width=59)
user_entry.grid(row=2, column=1,columnspan=2)
user_entry.insert(0, "example@gmail.com")

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

window.mainloop()