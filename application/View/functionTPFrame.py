import tkinter as tk
import functionToPlot

class functionTPFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.nameText = tk.Label(self, text="Please enter the function you would like to visualize")
        self.nameText.pack(pady=5)
        self.task_entryFunc = tk.Entry(self, width=25,font=("Arial",12,))
        self.task_entryFunc.pack(pady=10)
        self.task_button = tk.Button(self, text="visualize",command=lambda: self.visualize()).pack(pady=10)
    def getFunction(self):
        task = self.task_entryFunc.get().strip()
        return task
    def visualize(self):
        ftp = functionToPlot.functionToPlot(self.getFunction())
        ftp.renderGraph()