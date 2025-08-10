import tkinter as tk
import sys
import os
from home import Home
from otherFrame import otherFrame
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Controller')))
from button import Button
from buttonFactory import buttonFactory

class programHub(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Program Hub")
        self.geometry("450x450")

        container = tk.Frame(self)
        container.pack(fill="both",expand=True)
 
        self.frames={}  

        for obj in (Home, otherFrame):
            page_name=obj.__name__
            if page_name == "Home":
                bf = buttonFactory()
                frame= obj(parent=container,controller=self,buttons=[bf.buttonBuild(self, Button("ToSomething", "something.py"))])
            else:
                frame= obj(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")

 
        self.show_frame("Home")
         
    def show_frame(self,frame_name):
        frame=self.frames[frame_name]
        frame.tkraise()

if __name__== "__main__":
    app = programHub()
    app.mainloop()