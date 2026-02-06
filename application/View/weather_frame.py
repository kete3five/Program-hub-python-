import tkinter as tk
import requests
from weather_info_holder import coordinatesHolder

class weatherFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.coordinateText = tk.Label(self, text="Please enter the latitude of your desired area")
        self.coordinateText.grid(row=0, column=0)
        self.coordinateField = tk.Entry(self, width=15, font=("Arial", 12,))
        self.coordinateField.grid(row=1, column=0)
        self.YcoordinateText = tk.Label(self, text="Please enter the longitude of your desired area")
        self.YcoordinateText.grid(row=2, column=0)
        self.YcoordinateField = tk.Entry(self, width=15, font=("Arial", 12,))
        self.YcoordinateField.grid(row=3,column=0)
        self.printInfoButton = tk.Button(self, text="Print out the weather", command=lambda: self.get_Info(parent)).grid(row=4,column=0)
    def get_Info(self, parent):
        self.Xcoordinates = self.coordinateField.get().strip()
        self.Ycoordinates = self.YcoordinateField.get().strip()
        self.data = coordinatesHolder.get_weather_Info(self, Xcoordinates=self.Xcoordinates, Ycoordinates=self.Ycoordinates)
        self.dataText = tk.Label(self, text=f"the current temperature in that region is {self.data} degrees celsius").grid(row=7, column=15)