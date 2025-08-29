import tkinter as tk
from tkinter import messagebox
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model')))
import dataSaver


class addProject(tk.Frame):
    def __init__(self, controller, parent):
        super().__init__(parent)
        self.dt = dataSaver.dataSaver()
        self.dt.load()
        self.buttons1 = self.dt.buttons
        self.controller=controller
        self.task_entryName = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryPath = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryName.pack(pady=10)
        self.task_entryPath.pack(pady=10)
        tk.Button(self,text="create a button",command=lambda: self.addTask()).pack(pady=10)
        tk.Button(self,text="back",command=lambda: controller.show_frame("Home")).pack(pady=10)  
        tk.Button(self,text="Delete Button", comman=lambda: self.deleteTask()).pack(pady=10) 
        self.task_list=tk.Listbox(self,width=40,height=10,selectmode=tk.SINGLE)
        tk.Button(self, text="Delete", command=lambda: self.deleteTask().pack(pady=10))
        self.task_list.pack(pady=5)
        self.displayTasks()
    #adding the tasks
    def addTask(self):
        task = self.task_entryName.get().strip()
        task2 = self.task_entryPath.get().strip()
        if task and task2:
            dataSaver.dataSaver().update(task, task2)
            messagebox.showinfo("The file has successfully been added")
        else:
            messagebox.showwarning("Please enter text in both fields.")
    #deleting the tasks
    def deleteTask(self):
        #todelete = self.task_entryName.get()
        try:
            selected = self.task_list.curselection()[0]
            self.dt.deleteFromFile(selected)
            self.task_list.delete(selected)
        except IndexError:
            messagebox.showwarning("Warning","please enter a task.")
    #displaying tasks
    def displayTasks(self):
        for i in self.buttons1:
            self.task_list.insert(tk.END, i.name)