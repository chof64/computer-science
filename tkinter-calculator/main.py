from tkinter import *

def window_geometry(context):
    window_width = 600
    window_height = 300
    screen_width = context.winfo_screenwidth()
    screen_height = context.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return f"{window_width}x{window_height}+{x}+{y}"

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Error: Division by zero")
                return
        else:
            result_label.config(text="Error: Invalid operator")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

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


# Create entry fields
entry1 = Entry(root)
entry1.pack()

entry2 = Entry(root)
entry2.pack()


# Create operator selection
operator_var = StringVar()
operator_var.set("+")  # Set default operator to addition

operator_label = Label(root, text="Operator:")
operator_label.pack()

operator_menu = OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.pack()

# Create the button for calculation
calculate_button = Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create the label to display the result
result_label = Label(root, text="Result:")
result_label.pack()


root.mainloop()
