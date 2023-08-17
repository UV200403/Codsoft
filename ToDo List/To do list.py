import tkinter as tk
from tkinter import messagebox

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.title("To-Do List ")
        self.geometry("400x300")

        self.label_task = tk.Label(self, text="Enter a task:", font=('Book Antiqua', 15, 'bold'))
        self.label_task.pack(pady=5)
        self.label_task.place(x=10,y=20)

        self.entry_task = tk.Entry(self,  width=40)
        self.entry_task.pack()
        self.entry_task.place(x=30,y=54)

        self.button_add = tk.Button(self, text="Add Task", command=self.add_task, font=('Book Antiqua', 10, 'bold'), bg = "Green")
        self.button_add.pack(pady=5)
        self.button_add.place(x=300,y=49)

        self.label1_task=tk.Label(self, text="List Items",font=('Book Antique', 15, 'bold'))
        self.label1_task.pack(pady=5)
        self.label1_task.place(x=120,y=110)

        self.listbox_tasks = tk.Listbox(self, height=5, width=45)
        self.listbox_tasks.pack(pady=5)
        self.listbox_tasks.place(x=30,y=150)


        self.button_remove = tk.Button(self, text="Remove Task", command=self.remove_task, font=('Book Antiqua', 10, 'bold'), bg="Red")
        self.button_remove.pack(pady=5)
        self.button_remove.place(x=120,y=250)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.listbox_tasks.curselection()
        if selected_index:
            index = selected_index[0]
            self.listbox_tasks.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()