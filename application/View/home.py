import tkinter as tk
import subprocess

class buttonFactory:
    def buttonBuild(self, root, detailsButton, font = ("Arial", 16, "Bold"), width = 10):
        return tk.Button(root, text=detailsButton.name, width=10, command=lambda:subprocess.Popen(["python", detailsButton.path]))

class Home(tk.Frame):
    def __init__(self, controller, parent, buttons):
        super().__init__(parent)
        self.controller=controller
        
        tk.Label(self,text="Program Hub",font=("Arial",18)).pack(pady=10)
        #tk.Button(self,text="go somewhere",command=lambda: controller.show_frame("OtherScreen")).pack(pady=10)
        global counter
        counter = 1
        for i in buttons:
            i.pack(pady = counter * 5)
            counter+= 1