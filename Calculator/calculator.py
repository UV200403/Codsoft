import tkinter as tk
def on_button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
def on_clear_click():
    entry.delete(0, tk.END)
def on_equal_click():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                       command=lambda t=text: on_button_click(t) if t != "=" else on_equal_click())
    button.grid(row=row, column=col)
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 16),
                         command=on_clear_click)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()