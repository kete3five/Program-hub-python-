import tkinter as tk
from graph_info_receiver import GraphInfoReceiver
import matplotlib.pyplot as plt

class GraphBuilder(tk.Frame):
    """builds a graph"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.info_text = "Please enter the crypto value you would like to check"
        self.crypto_text = tk.Label(parent, text=self.info_text)
        self.crypto_text.grid(row=0, column=7)
        self.crypto_entry = tk.Entry(self, width=15, font=("Arial",12,))
        self.crypto_entry.grid(row=1, column=7)
        self.check_button = tk.Button(self, text="check the value", command=lambda: self.get_graph())
        self.check_button.grid(row=2, column=7)
    def get_graph(self):
        """gives data to another class"""
        #print("the function started")
        crypto = "bitcoin"
        temp = GraphInfoReceiver().get_info(crypto=crypto)
        #print(temp)
        self.dates = temp[0]
        print(self.dates)
        self.prices = temp[1]
        print(self.prices)
        plt.plot(self.dates, self.prices)
        plt.show()
#gb = GraphBuilder()
#gb.get_graph("bitcon")                                                                                   