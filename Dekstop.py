# Basic UI Demo with Tkinter

This guide walks you through creating a simple graphical user interface (GUI) using Python's built-in `tkinter` module.

## Step-by-Step Instructions

### 1. Import Tkinter
```python
import tkinter as tk
```

### 2. Create the Main Window
```python
root = tk.Tk()
root.title("Basic UI Demo")
root.geometry("300x350")
```

### 3. Add a Label
```python
label = tk.Label(root, text="This is a label")
label.pack(pady=10)
```

### 4. Add an Entry Box
```python
entry = tk.Entry(root)
entry.pack(pady=5)
```

### 5. Add a Button
```python
button = tk.Button(root, text="Click Me")
button.pack(pady=5)
```

### 6. Add Radio Buttons
```python
radio1 = tk.Radiobutton(root, text="Option 1", value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", value=2)
radio2.pack()
```

### 7. Add a Checkbox
```python
checkbox = tk.Checkbutton(root, text="Check me")
checkbox.pack(pady=5)
```

### 8. Add a Dropdown Menu
```python
options = ["One", "Two", "Three"]
dropdown_var = tk.StringVar(value=options[0])

dropdown_label = tk.Label(root, text="Choose something:")
dropdown_label.pack(pady=(10, 0))

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()
```

### 9. Start the GUI Loop
```python
root.mainloop()
```

This code creates a simple GUI with various widgets like labels, buttons, radio buttons, checkboxes, and a dropdown menu.

---

**Note:** This requires Python 3 and no additional dependencies since `tkinter` is part of the standard library.
