import tkinter as tk
from tkinter import *
from tkinter import ttk

class graphEntries:
    def __init__(self, parent):
        self.color = ""
        self.width = 0
        self.nameText = tk.Label(parent, text="Please enter the function you would like to visualize")
        self.nameText.pack(pady=5)
        self.task_entryFunc = tk.Entry(parent, width=25,font=("Arial",12,))
        self.task_entryFunc.pack(pady=10)
        self.nameText1 = tk.Label(parent, text="Please enter the range of your function")
        self.nameText1.pack(pady=5)
        self.task_entryRange = tk.Entry(parent, width=25,font=("Arial",12,))
        self.task_entryRange.pack(pady=10)
        #color
        self.comboColor = ttk.Combobox(parent, font=("Arial",12), width=10, height=5, values=["green", "blue", "red", "yellow", "orange"])
        self.comboColor.pack(pady=10)
        self.comboColor.bind('<<ComboboxSelected>>', self.selectColor)
        #width
        self.comboWidth = ttk.Combobox(parent, font=("Arial",12), width=10, height=5, values=[5, 6, 7, 8, 9, 10])
        self.comboWidth.pack(pady=10)
        self.comboColor.bind('<<ComboboxSelected>>', self.selectWidth)
        #name
        self.nameName = tk.Label(parent, text="Please enter the name of your desired function")
        self.nameName.pack(pady=5)
        self.task_entryName = tk.Entry(parent, width=25,font=("Arial",12,))
        self.task_entryName.pack(pady=10)
    def selectColor(self, event):
        self.color = self.comboColor.get()
    def selectWidth(self, event):
        self.width = self.comboWidth.get()