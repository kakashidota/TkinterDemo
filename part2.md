# 🧠 Tkinter Part 2 – Making the UI Interactive

Welcome to **Part 2** of our Tkinter series! In this section, we'll add **logic** to the UI created in Part 1.

You'll learn how to:

- Retrieve values from input fields
- Track user selections (radio, checkbox, dropdown)
- Display results using a popup window

---

## ⚙️ What You Need

- Python 3.7+
- Tkinter (should already be installed with Python)

✅ Make sure you've completed [Part 1](README.md) before starting this.

---

## 📁 How to Run

1. Save the code below as `part2_interactive_ui.py`
2. Open your terminal and run:

```bash
python part2_interactive_ui.py


import tkinter as tk
from tkinter import messagebox

def on_submit():
    name = entry.get()
    selected_gender = gender_var.get()
    subscribed = subscribe_var.get()
    language = language_var.get()

    info = f"Name: {name}\nGender: {selected_gender}\nSubscribed: {'Yes' if subscribed else 'No'}\nLanguage: {language}"
    messagebox.showinfo("Submitted Info", info)

# Create main window
root = tk.Tk()
root.title("Interactive UI Demo")
root.geometry("350x350")

# Entry widget
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=(10, 0))

entry = tk.Entry(root)
entry.pack()

# Radio buttons for gender
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=(10, 0))

gender_var = tk.StringVar(value="Other")

radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.pack()

radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
radio_other.pack()

# Checkbox for subscription
subscribe_var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var)
checkbox.pack(pady=10)

# Dropdown menu for favorite language
label_language = tk.Label(root, text="Favorite Language:")
label_language.pack(pady=(10, 0))

languages = ["Python", "JavaScript", "Java", "C++", "Go"]
language_var = tk.StringVar(value=languages[0])

dropdown = tk.OptionMenu(root, language_var, *languages)
dropdown.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
