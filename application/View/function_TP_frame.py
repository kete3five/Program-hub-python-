import tkinter as tk
from function_to_plot import functionToPlot
from graph_file import graph
from entries_class import graphEntries

class functionTPFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.entryGraphs = []
        self.graphs = []
        self.functions = []
        #self.task_button = tk.Button(self, text="add to list",command=lambda: self.sendToList()).pack(pady=10)
        self.task_visButton = tk.Button(self, text="visualize the Functions",command=lambda: self.visualize()).grid(row=0, column=0)
        self.task_addButton = tk.Button(self, text="+", command=lambda: self.add_func_button()).grid(row=0,column=1)
        self.task_deleteButton = tk.Button(self, text="-", command=lambda: self.delete_func_button()).grid(row=0, column=2)
        self.currentRow = 1
    def get_function(self):
        task = self.task_entryFunc.get().strip()
        return task
    # def sendToList(self):
    #     #ftp = functionToPlot.functionToPlot()
    #     #ftp.renderGraph(int(self.task_entryRange.get().strip()))
    #     #ftp.renderGraph(int(self.task_entryRange.get().strip()), ["sin(x)","cos(x)"])
    #     self.functions.append(graphfile.graph(self.task_entryColor.get().strip(), self.task_entrywidth.get().strip(), self.task_entryName.get().strip(), self.task_entryFunc.get().strip()))
    #     print(len(self.functions))
    def visualize(self):
        self.collect_info()
        ftp = functionToPlot()
        ftp.render_graph(10, self.functions)
    def add_func_button(self):
        self.entryGraphs.append(graphEntries(self, self.currentRow))
        self.currentRow+=1
    def delete_func_button(self):
        self.entryGraphs[-1].delete_elements()
        self.entryGraphs.pop()
        self.currentRow-=1
    def collect_info(self):
        for i in self.entryGraphs:
            print(i.width)
            print(type(i.width))
            self.functions.append(graph(i.color, float(i.width), i.task_entryName.get(), i.task_entryFunc.get()))