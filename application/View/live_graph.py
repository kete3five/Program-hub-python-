"""importing modules"""
import tkinter as tk
import threading
import time
import datetime as dt
from tkinter import ttk
import requests
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class live_Graph(tk.Frame):
    """making a live graph"""
    def __init__(self, controller, parent):
        """creating canvas and lists"""
        super().__init__(parent)
        self.controller = controller
        self.dates = []
        self.prices = []
        self.figure = Figure(figsize=(6,4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.chart_frame = ttk.Frame(self)
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.line, = self.ax.plot([], [], marker="o")
        self.canvas = FigureCanvasTkAgg(figure=self.figure, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.start_thread()

    def get_last_value(self):
        """getting the last value"""
        try:
            dates1,prices1 = self.get_info()
        except TypeError as e:
            print(e)
        for i in prices1:
            if i not in self.prices:
                self.prices.append(i)
        if len(self.dates) + len(dates1) >= 50:
            counter = 0
            for i in dates1:
                if i not in self.dates:
                    counter = counter + 1
                    self.dates.append(i)
                    self.dates.pop(counter)
        else:
            for i in dates1:
                if i not in self.dates:
                    self.dates.append(i)

    def redraw_graph(self):
        """redrawing the graph"""
        self.line.set_xdata(range(len(self.dates)))
        self.line.set_ydata(self.prices)
        self.ax.set_xticks(range(len(self.dates)))
        self.ax.set_xticklabels(self.dates, rotation=45, ha="right")
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
    def get_graphs(self):
        """drawing the graph each 5 seconds"""
        while True:
            time.sleep(5)
            self.get_last_value()
            self.redraw_graph()

    def start_thread(self):
        """starting the thread"""
        threading.Thread(target=self.get_graphs, daemon=False).start()
        #threading.Thread(target=programHub.show_frame(programHub, Home), daemon=False).start()

    #def get_delayed_data(self):
     #   while True:
      #      self.after(3000,)

    def get_info(self):
        """getting information for the graph"""
        #threading.Thread(target=self.get_Info(), daemon=True)
        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        params = {
        "vs_currency": "usd",
        "days": 10,
        "interval": "daily"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        try:
            response=requests.get(url,params=params,timeout=10, headers=headers)
            response.raise_for_status()
            data=response.json()
            for i in data["prices"]:
                self.dates.append(dt.datetime.fromtimestamp(i[0] / 1000))
                self.prices.append(i[1])
            print("i get triggered")
            return (self.dates, self.prices)
        except requests.exceptions.RequestException as e:
            print(e)
