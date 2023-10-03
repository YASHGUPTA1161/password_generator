from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:
            {
                "email" : email,
                "password" : password
            }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any field empty")
        # alert message box
        
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the detailed entered: \nEmail: {email}\n Password: {password} \n Is it ok to save")
        if is_ok:
            # Exception handling
            
            try:
                with open("100_day_py/29_password_manager/data.json",  "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open("100_day_py/29_password_manager/data.json",  "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                
            else:    
                # updating old data with new data
                data.update(new_data)
            
                with open("100_day_py/29_password_manager/data.json",  "w") as data_file:
                        # saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)  

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # get the data of website input field
    website = website_input.get()
    # error here with path
    try:
        with open("100_day_py/29_password_manager/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="NO DATA FILE FOUND")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist")
    
    
# --------------------------- UI SETUP ------------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# labels
website_lable = Label(text="Website:")
website_lable.grid(row=1, column=0)

email_lable = Label(text="Email/Username:")
email_lable.grid(row=2, column=0)

password_lable = Label(text="Password:")
password_lable.grid(row=3, column=0)


# Entry
website_input = Entry(width=34)
website_input.grid(row=1, column=1, columnspan=1)

email_input = Entry(width=45)
email_input.grid(row=2, column=1, columnspan=2)


password_input = Entry(width=34)
password_input.grid(row=3, column=1, columnspan=1)

# Button

add_password = Button(text="Add", width=8, command=save)
add_password.grid(row=3, column=2, columnspan=2)

generate_password = Button(text="Generate Password", width=38, command=generate_password)
generate_password.grid(row=4, column=1, columnspan=2)

search_password = Button(text="search", width=8, command=find_password)
search_password.grid(row=1, column=2, columnspan=2)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="100_day_py/29_password_manager/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

window.mainloop()
