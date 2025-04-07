import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Basic UI Demo")
root.geometry("300x350")

# Label
label = tk.Label(root, text="This is a label")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Click Me")
button.pack(pady=5)

# Radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", value=2)
radio2.pack()

# Checkbox
checkbox = tk.Checkbutton(root, text="Check me")
checkbox.pack(pady=5)

# Dropdown (OptionMenu)
options = ["One", "Two", "Three"]
dropdown_var = tk.StringVar(value=options[0])

dropdown_label = tk.Label(root, text="Choose something:")
dropdown_label.pack(pady=(10, 0))

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

# Start the main loop
root.mainloop()
