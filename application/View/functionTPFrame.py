import tkinter as tk
import functionToPlot
import graphfile
import entriesClass

class functionTPFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.entryGraphs = []
        self.graphs = []
        self.functions = []
        self.task_button = tk.Button(self, text="add to list",command=lambda: self.sendToList()).pack(pady=10)
        self.task_visButton = tk.Button(self, text="visualize the Functions",command=lambda: self.visualize()).pack(pady=10)
        self.task_addButton = tk.Button(self, text="+", command=lambda: self.addFuncButton()).pack(pady=10)
    def getFunction(self):
        task = self.task_entryFunc.get().strip()
        return task
    def sendToList(self):
        #ftp = functionToPlot.functionToPlot()
        #ftp.renderGraph(int(self.task_entryRange.get().strip()))
        #ftp.renderGraph(int(self.task_entryRange.get().strip()), ["sin(x)","cos(x)"])
        self.functions.append(graphfile.graph(self.task_entryColor.get().strip(), self.task_entrywidth.get().strip(), self.task_entryName.get().strip(), self.task_entryFunc.get().strip()))
        print(len(self.functions))
    def visualize(self):
        ftp = functionToPlot.functionToPlot()
        ftp.renderGraph(int(self.task_entryRange.get()), self.functions)
    def addFuncButton(self):
        self.entryGraphs.append(entriesClass.graphEntries(self))