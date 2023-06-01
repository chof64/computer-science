from tkinter import *
from tkinter import messagebox

def window_geometry(context):
    window_width = 600
    window_height = 300
    screen_width = context.winfo_screenwidth()
    screen_height = context.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return f"{window_width}x{window_height}+{x}+{y}"

def on_start():
    messagebox.showinfo("Welcome","Welcome to this registration form. You can enter your details and once you're done, you can press submit. If you have any questions or problems, send us (admin) a message.")

def update_data():
    if messagebox.askyesno("Submit your answers", "Do you wish to submit your response?"):
        data["first_name"] = first_name_entry.get()
        data["last_name"] = last_name_entry.get()
        data["email"] = email_entry.get()
        data["password"] = password_entry.get()
        return print(data)
        
    if messagebox.askyesno("Reset Form Fields?","Do you wish to reset the form fields?"):
        first_name_entry.delete(0,"end")
        last_name_entry.delete(0,"end")
        email_entry.delete(0,'end')
        password_entry.delete(0,'end')

def on_close():
    if messagebox.askokcancel("Close the application?", "Do you want to close the application?"):
        root.destroy()

data = {}

root = Tk()
root.title="Registration Form"
root.geometry(window_geometry(root))
root.protocol("WM_DELETE_WINDOW", on_close )


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

root.after(100,on_start)
root.mainloop()
