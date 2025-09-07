import matplotlib.pyplot as plt 
import numpy as np
import re

relations = {"sin": np.sin, "cos": np.cos, "tg": np.tan, "sqrt": np.sqrt}

class functionToPlot:
    def __init__(self, equation):
        self.equation = equation

    def convert(self, x):
        for i in relations:
            self.equation = re.sub(rf"\b{i}\b", f"relations['{i}']", self.equation)
        self.equation = self.equation.replace("x", "x")
        return eval(self.equation, {"__builtins__": None}, {"x": x, "relations": relations})
    def renderGraph(self):
        x=np.linspace(0,10,100)
        plt.figure(figsize=(8,5))
        plt.plot(x, self.convert(x),label="rendered function",color="blue",linewidth=2)
        
        plt.title("rendered function")
        plt.xlabel("x")
        
        plt.legend()
        plt.grid(True)
        
        plt.show()

#func = functionToPlot("sin(2*x)+sqrt(16)")
#func.renderGraph()