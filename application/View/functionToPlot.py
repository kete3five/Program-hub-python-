import matplotlib.pyplot as plt 
import numpy as np
import re

relations = {"sin": np.sin, "cos": np.cos, "tg": np.tan, "sqrt": np.sqrt}

class functionToPlot:
    def convert(self, x, equation):
        for i in relations:
            equation = re.sub(rf"\b{i}\b", f"relations['{i}']", equation)
        equation = equation.replace("x", "x")
        return eval(equation, {"__builtins__": None}, {"x": x, "relations": relations})
    def renderGraph(self, range, equations):
        x=np.linspace(0, range, 10000)     
        plt.figure(figsize=(8,5))
        for i in equations:
            plt.plot(x, self.convert(x, i.equation),label=i.name,color=i.colour,linewidth=i.width)
            plt.title(i.name)
            plt.xlabel("x")        
            plt.legend()
            plt.grid(True)
                
        plt.show()

#func = functionToPlot("sin(2*x)+sqrt(16)")
#func.renderGraph()