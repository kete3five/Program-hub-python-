import tkinter as tk

class graphEntries:
    def __init__(self):
        self.nameText = tk.Label(self, text="Please enter the function you would like to visualize")
        self.nameText.pack(pady=5)
        self.task_entryFunc = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryFunc.pack(pady=10)
        self.nameText1 = tk.Label(self, text="Please enter the range of your function")
        self.nameText1.pack(pady=5)
        self.task_entryRange = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryRange.pack(pady=10)
        self.namecolor = tk.Label(self, text="Please enter the colour of your desired function")
        self.namecolor.pack(pady=5)
        self.task_entryColor = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryColor.pack(pady=10)
        self.namewidth = tk.Label(self, text="Please enter the width of the lines of your desired function")
        self.namewidth.pack(pady=5)
        self.task_entrywidth = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entrywidth.pack(pady=10)
        self.nameName = tk.Label(self, text="Please enter the name of your desired function")
        self.nameName.pack(pady=5)
        self.task_entryName = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryName.pack(pady=10)