from tkinter import *

def window_geometry(context):
    window_width = 600
    window_height = 300
    screen_width = context.winfo_screenwidth()
    screen_height = context.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    return f"{window_width}x{window_height}+{x}+{y}"

def buttons_color(context, name,fg, bg):
    return Button(context, fg=fg, bg=bg, text=name, height=2, command=lambda: message.config(fg=fg, bg=bg, text=f"{name}\nForeground: {fg}\nBackground: {bg}"))

root = Tk()

root.title="Primary Colors"
root.geometry(window_geometry(root))

message = Label(root, text="Click a button to change the color of this text")
message.pack(fill="both", expand=True)

colors = [
    buttons_color(root, "Blue", "#1e40af", "#60a5fa"),
    buttons_color(root, "Yellow", "#854d0e", "#facc15"),
    buttons_color(root, "Red", "#991b1b", "#f87171"),
]

for color in colors:
    color.pack(fill=X)

root.mainloop()