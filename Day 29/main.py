from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generator():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    Password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = Website_Input.get()
    email = Email_input.get()
    password = Password_input.get()
    new_data = {web: {"email": email,"password": password,}}

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Oops",message = f"Please don't leave any fields empty!")
    else:

        # is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email}"
        #                                                   f"\nPassword: {password} \n Is is ok to save?")
        # if is_ok:
        try:
            with open("data.json",mode = 'r') as file:
                # json.dump(new_data,file,indent=4)
                #Rad old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data,file,indent=4)

        else:
            #Update old data with new data
            data.update(new_data)

            with open("data.json", mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            # file.write(f"{web} | {email} | {password}\n")

            Website_Input.delete(0, END)
            Password_input.delete(0, END)
def search():

    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        for name in data:
            if Website_Input.get() == name:
                email = data[name]["email"]
                password = data[name]["password"]
        try:
            messagebox.showinfo(title=Website_Input.get(), message=f"Email: {email}\nPassword: {password}")
        except UnboundLocalError:
            print("Website not registered.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 30,pady = 30)



canvas = Canvas(width = 200, height = 200)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row = 0,column = 1)

Website = Label(text="Website:")

Website.grid(row = 1,column = 0)

Email = Label(text="Email/Username:")
Email.grid(row = 2,column = 0)

Password = Label(text="Password:")
Password.grid(row = 3,column = 0)

Website_Input = Entry(width = 21)
Website_Input.grid(row = 1,column = 1)
Website_Input.focus()

Search_Button = Button(text="Search",command=search,width=13)
Search_Button.grid(row = 1,column = 2)

Email_input = Entry(width = 35)
Email_input.grid(row = 2,column = 1,columnspan = 2)
Email_input.insert(0,"swayammsoni@gmail.com")
#Can use END to insert at the end of the string

Password_input = Entry(width = 21)
Password_input.grid(row = 3,column = 1)

Password_Button = Button(text="Generate Password",command=generator,width=20)
Password_Button.grid(row = 3,column = 2)
print()

Add_Button = Button(text="Add",width = 36,command = save)
Add_Button.grid(row = 4,column = 1,columnspan=2)



window.mainloop()