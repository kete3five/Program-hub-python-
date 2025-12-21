import tkinter as tk
import sys
import os
from home import Home
from other_frame import otherFrame
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Controller')))
from button import Button
from button_factory import ButtonFactory
import data_saver
from add_projects import addProject
from function_TP_frame import functionTPFrame
from weather_frame import weatherFrame
from graph_builder import GraphBuilder
import live_graph
import threading

class programHub(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Program Hub")
        self.geometry("1280x720")
        global dt
        dt = data_saver.dataSaver()
        global container
        container = tk.Frame(self)
        container.pack(fill="both",expand=True)
        dt.load()
        self.frames={}
        self.create_frames()
        self.show_frame("Home")
    #showing the frames   
    def show_frame(self,frame_name):
        dt.load()
        self.create_frames()
        frame=self.frames[frame_name]
        frame.tkraise()
    #rendering the frames
    def create_frames(self):       
        for obj in (Home, addProject, functionTPFrame, weatherFrame, GraphBuilder, live_graph.live_Graph):
            page_name=obj.__name__
            if page_name == "Home":
                frame= obj(parent=container,controller=self,buttons=dt.buttons)
            else:
                frame= obj(parent=container,controller=self)
              #  if page_name == "live_Graph":
               #     threading.Thread(target=lambda: frame= obj(parent=container,controller=self, buttons=dt.buttons), daemon=False).start()
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky="nsew")

if __name__== "__main__":
    app = programHub()
    app.mainloop()