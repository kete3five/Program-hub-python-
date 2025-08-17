import tkinter as tk
from tkinter import messagebox

class addProject(tk.Frame):
        def __init__(self, controller, parent):
            super().__init__(parent)
            self.controller=controller
            self.task.entry = tk.Entry(self.controller, width=25,font=("Arial",12,))
            self.task.entry1 = tk.Entry(self.controller, width=25,font=("Arial",12,))
            self.task_entry.pack(pady=10)
            self.task_entry1.pack(pady=10)
        def addTask(self):
            task = self.task_entry.get().strip()
            task2 = self.task_entry1.get().strip()

            if task and task2:
                return task + ";" + task2
                self.task_entry.delete(0, tk.END)
                self.task_entry1.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter text in both fields.")