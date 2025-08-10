import tkinter as tk

class otherFrame(tk.Frame):
    def __init__(self, controller, parent):
        super().__init__(parent)
        self.controller=controller
        
        tk.Label(self,text="Program Hub",font=("Arial",18)).pack(pady=10)