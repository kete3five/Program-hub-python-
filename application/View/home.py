import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Controller')))
from buttonFactory import buttonFactory

class Home(tk.Frame):
    def __init__(self, controller, parent, buttons):
        super().__init__(parent)
        self.controller=controller
        
        tk.Label(self,text="Program Hub",font=("Arial",18)).pack(pady=10)
        #tk.Button(self,text="go somewhere",command=lambda: controller.show_frame("OtherScreen")).pack(pady=10)
        global counter
        counter = 1
        for i in buttons:
            buttonFactory().buttonBuild(controller, i).pack(pady = counter * 5)
            counter+= 1