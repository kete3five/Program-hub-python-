import csv
from button import Button

class dataSaver:
    def __init__(self):
        self.buttons = []
    def update(self, name, destination):
        with open("data.csv","w",newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerows((name, destination))
    def load(self):
        with open("data.csv","r") as f:
            reader = csv.reader(f, delimiter=";")
            for i,j in reader:
                self.buttons.append(Button(i, j))