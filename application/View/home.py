import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Controller')))
from button_factory import ButtonFactory
from add_projects import addProject

class Home(tk.Frame):
    def __init__(self, controller, parent, buttons):
        super().__init__(parent)
        self.controller=controller
        
        tk.Label(self,text="Program Hub",font=("Arial",18)).pack(pady=10)
        tk.Button(self,text="add project",command=lambda: self.controller.show_frame("addProject")).pack(pady=10)
        tk.Button(self,text="View functions", command=lambda: self.controller.show_frame("functionTPFrame")).pack(pady=10)
        tk.Button(self, text="check the weather", command=lambda: self.controller.show_frame("weatherFrame")).pack(pady=10)
        tk.Button(self, text="build a graph on data", command=lambda: self.controller.show_frame("GraphBuilder")).pack(pady=10)
        tk.Button(self, text="check the crypto status", command=lambda: self.controller.show_frame("live_Graph")).pack(pady=10)

        global counter
        counter = 1
        for i in buttons:
            ButtonFactory().button_build(self, i).pack(pady = counter * 2)
            counter+= 1