# 🧠 Tkinter Beginner Cheat Sheet – 15 Exercises with Solutions

A set of 15 beginner-friendly Tkinter projects with working solutions. Each solution is designed to reinforce core Tkinter concepts like widgets, layout, and logic.

---

## ✅ Exercise 1: Simple Greeting Label

```python
import tkinter as tk

root = tk.Tk()
root.title("Greeting")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

root.mainloop()
✅ Exercise 2: Change Label Text on Button Click
python
Copy
Edit
import tkinter as tk

def change_text():
    label.config(text="You clicked me!")

root = tk.Tk()
label = tk.Label(root, text="Hello")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

root.mainloop()
✅ Exercise 3: Input Box Echo
python
Copy
Edit
import tkinter as tk

def show_name():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=show_name)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
✅ Exercise 4: Radio Button Selector
python
Copy
Edit
import tkinter as tk

def show_selection():
    label.config(text=f"Selected: {color.get()}")

root = tk.Tk()
color = tk.StringVar()

tk.Radiobutton(root, text="Red", variable=color, value="Red").pack()
tk.Radiobutton(root, text="Green", variable=color, value="Green").pack()
tk.Radiobutton(root, text="Blue", variable=color, value="Blue").pack()

tk.Button(root, text="Show", command=show_selection).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
✅ Exercise 5: Checkbox Toggle
python
Copy
Edit
import tkinter as tk

def check_state():
    text = "Subscribed" if var.get() else "Not Subscribed"
    label.config(text=text)

root = tk.Tk()
var = tk.BooleanVar()

tk.Checkbutton(root, text="Subscribe", variable=var, command=check_state).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()
✅ Exercise 6: Dropdown Menu Display
python
Copy
Edit
import tkinter as tk
from tkinter import messagebox

def show_choice():
    messagebox.showinfo("Selection", f"You picked: {choice.get()}")

root = tk.Tk()
options = ["Cat", "Dog", "Rabbit", "Bird"]
choice = tk.StringVar(value=options[0])

tk.OptionMenu(root, choice, *options).pack()
tk.Button(root, text="Submit", command=show_choice).pack()

root.mainloop()
✅ Exercise 7: Simple Login Form (No Auth)
python
Copy
Edit
import tkinter as tk
from tkinter import messagebox

def login():
    messagebox.showinfo("Login Info", f"Username: {username.get()}\nPassword: {password.get()}")

root = tk.Tk()
username = tk.StringVar()
password = tk.StringVar()

tk.Label(root, text="Username").pack()
tk.Entry(root, textvariable=username).pack()

tk.Label(root, text="Password").pack()
tk.Entry(root, textvariable=password, show="*").pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
✅ Exercise 8: Clear Entry Button
python
Copy
Edit
import tkinter as tk

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()
✅ Exercise 9: Counter App
python
Copy
Edit
import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

root = tk.Tk()
label = tk.Label(root, text="0")
label.pack()

tk.Button(root, text="+", command=increase).pack(side="left")
tk.Button(root, text="-", command=decrease).pack(side="right")

root.mainloop()
✅ Exercise 10: Layout with grid()
python
Copy
Edit
import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
tk.Entry(root, show="*").grid(row=1, column=1)

tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2)

root.mainloop()
✅ Exercise 11: Change Background Color
python
Copy
Edit
import tkinter as tk

def change_bg():
    root.config(bg=color.get())

root = tk.Tk()
color = tk.StringVar(value="White")

tk.Radiobutton(root, text="Red", variable=color, value="red").pack()
tk.Radiobutton(root, text="Green", variable=color, value="green").pack()
tk.Radiobutton(root, text="Blue", variable=color, value="blue").pack()

tk.Button(root, text="Apply", command=change_bg).pack()

root.mainloop()
✅ Exercise 12: Simple Calculator
python
Copy
Edit
import tkinter as tk

def calculate():
    try:
        a = float(num1.get())
        b = float(num2.get())
        op = operator.get()
        result = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b if b != 0 else "Error"
        }[op]
        label_result.config(text=f"Result: {result}")
    except:
        label_result.config(text="Invalid input")

root = tk.Tk()
num1 = tk.Entry(root)
num2 = tk.Entry(root)
operator = tk.StringVar(value="+")

num1.pack()
num2.pack()
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()
tk.Button(root, text="Calculate", command=calculate).pack()
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
✅ Exercise 13: To-Do List Box
python
Copy
Edit
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Add Task", command=add_task).pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()
✅ Exercise 14: Open a New Window
python
Copy
Edit
import tkinter as tk

def open_new():
    new = tk.Toplevel(root)
    tk.Label(new, text="This is a new window").pack()

root = tk.Tk()
tk.Button(root, text="Open Window", command=open_new).pack()
root.mainloop()
✅ Exercise 15: Basic Form Validator
python
Copy
Edit
import tkinter as tk
from tkinter import messagebox

def validate():
    if not name.get() or not email.get():
        messagebox.showerror("Error", "All fields are required")
    else:
        messagebox.showinfo("Success", "Form submitted")

root = tk.Tk()
name = tk.StringVar()
email = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email).pack()

tk.Button(root, text="Submit", command=validate).pack()

root.mainloop()
