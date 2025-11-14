import tkinter as tk
from tkinter import *
from tkinter import ttk

class graphEntries:
    def __init__(self, parent, readyRows):
        self.color = ""
        self.width = 0
        self.nameText = tk.Label(parent, text="Please enter the function \n you would like to visualize")
        self.nameText.grid(row=readyRows, column=0)
        self.task_entryFunc = tk.Entry(parent, width=15,font=("Arial",12,))
        self.task_entryFunc.grid(row=readyRows, column=1)
        self.nameText1 = tk.Label(parent, text="Please enter the \n range of your function")
        self.nameText1.grid(row=readyRows, column=2)
        self.task_entryRange = tk.Entry(parent, width=15,font=("Arial",12,))
        self.task_entryRange.grid(row=readyRows, column=3)
        #color
        self.comboColor = ttk.Combobox(parent, font=("Arial",12), width=10, height=5, values=["green", "blue", "red", "yellow", "orange"])
        self.comboColor.grid(row=readyRows, column=4)
        self.comboColor.bind('<<ComboboxSelected>>', self.select_color)
        #width
        self.comboWidth = ttk.Combobox(parent, font=("Arial",12), width=10, height=5, values=[5, 6, 7, 8, 9, 10])
        self.comboWidth.grid(row=readyRows, column=5)
        self.comboWidth.bind('<<ComboboxSelected>>', self.select_width)
        #name
        self.nameName = tk.Label(parent, text="Please enter the \n name of your desired function")
        self.nameName.grid(row=readyRows, column=6)
        self.task_entryName = tk.Entry(parent, width=15,font=("Arial",12,))
        self.task_entryName.grid(row=readyRows, column=7)
    def select_color(self, event):
        print("i am from selecting color")
        self.color = self.comboColor.get()
    def select_width(self, event):
        print("i am from selecting width")
        self.width = self.comboWidth.get()
    def delete_elements(self):
        self.comboColor.destroy()
        self.comboWidth.destroy()
        self.nameName.destroy()
        self.nameText.destroy()
        self.nameText1.destroy()
        self.task_entryFunc.destroy()
        self.task_entryName.destroy()
        self.task_entryRange.destroy()