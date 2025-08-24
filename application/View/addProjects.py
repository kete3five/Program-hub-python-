import tkinter as tk
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model')))
import dataSaver


class addProject(tk.Frame):
    def __init__(self, controller, parent):
        super().__init__(parent)
        self.controller=controller
        self.task_entry = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entry1 = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entry.pack(pady=10)
        self.task_entry1.pack(pady=10)
        tk.Button(self,text="create a button",command=lambda: self.addTask()).pack(pady=10)
        tk.Button(self,text="back",command=lambda: controller.show_frame("Home")).pack(pady=10)    
    def addTask(self):
        task = self.task_entry.get().strip()
        task2 = self.task_entry1.get().strip()
        if task and task2:
            dataSaver.dataSaver().update(task, task2)
            messagebox.showinfo("The file has successfully been added")
        else:
            messagebox.showwarning("Please enter text in both fields.")