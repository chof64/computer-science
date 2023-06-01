from tkinter import *

def window_geometry(context):
    window_width = 600
    window_height = 300
    screen_width = context.winfo_screenwidth()
    screen_height = context.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return f"{window_width}x{window_height}+{x}+{y}"


def update_data():
    data["first_name"] = first_name_entry.get()
    data["last_name"] = last_name_entry.get()
    data["email"] = email_entry.get()
    data["password"] = password_entry.get()
    print(data)

data = {}

root = Tk()
root.title="Registration Form"
root.geometry(window_geometry(root))


# menu

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", )
helpmenu.add_command(label="About...", )
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# body
body = Frame(root)
body.pack(fill="both", expand=True, padx=20, pady=20)


# welcome
welcome = Label(body, text="Welcome to the registration form")
welcome.pack(fill="both", side="top", expand=True)

# first_name
first_name = Frame(body)
first_name.pack(fill="x", side="top")

firt_name_label = Label(first_name, text="First Name", width=15, anchor="w")
firt_name_label.pack(fill="x", side="left")
first_name_entry = Entry(first_name)
first_name_entry.pack(fill="x", side="right", expand=True)


# last_name
last_name = Frame(body)
last_name.pack(fill="x", side="top")

last_name_label = Label(last_name, text="Last Name", width=15, anchor="w")
last_name_label.pack(fill="x", side="left")
last_name_entry = Entry(last_name)
last_name_entry.pack(fill="x", side="right", expand=True)


# email
email = Frame(body)
email.pack(fill="x", side="top")

email_label = Label(email, text="Email", width=15, anchor="w")
email_label.pack(fill="x", side="left")
email_entry = Entry(email)
email_entry.pack(fill="x", side="right", expand=True)


# password
password = Frame(body)
password.pack(fill="x", side="top")

password_label = Label(password, text="Password", width=15, anchor="w")
password_label.pack(fill="x", side="left")
password_entry = Entry(password)
password_entry.pack(fill="x", side="right", expand=True)


result = Button(body, text="Submit", command=lambda:update_data())
result.pack(fill="x", side="top")


root.mainloop()