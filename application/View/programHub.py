import tkinter as tk
import sys
import os
from home import Home
from otherFrame import otherFrame
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Controller')))
from button import Button
from buttonFactory import buttonFactory
import dataSaver
from addProjects import addProject
from functionTPFrame import functionTPFrame

class programHub(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Program Hub")
        self.geometry("1280x720")
        global dt
        dt = dataSaver.dataSaver()
        global container
        container = tk.Frame(self)
        container.pack(fill="both",expand=True)
        dt.load()
        self.frames={}
        self.createFrames()
        self.show_frame("Home")
    #showing the frames   
    def show_frame(self,frame_name):
        dt.load()
        self.createFrames()
        frame=self.frames[frame_name]
        frame.tkraise()
    #rendering the frames
    def createFrames(self):       
        for obj in (Home, addProject, functionTPFrame):
            page_name=obj.__name__
            if page_name == "Home":
                frame= obj(parent=container,controller=self,buttons=dt.buttons)
            else:
                frame= obj(parent=container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")

if __name__== "__main__":
    app = programHub()
    app.mainloop()