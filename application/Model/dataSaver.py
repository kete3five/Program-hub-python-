import csv
from button import Button
import os

class dataSaver:
    def __init__(self):
        self.buttons = []
        self.load()
    def update(self, name, destination):
        with open("data.csv","a",newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([name, destination])
    def load(self):
       # if not os.path.exists("data.csv"):
        #    return
        with open("data.csv","r+") as f:
            reader = csv.reader(f, delimiter=";")
            flag = 0
            for name,path in reader:
                for k in self.buttons:
                    if k.name == name and k.path == path:
                        flag = 1
                #if self.buttons.__contains__(Button(i,j)):
                 #   continue
                #else:
                #    self.buttons.append(Button(i, j))
                if flag == 0:
                    self.buttons.append(Button(name,path))
                else:
                    flag = 0
    #deleting lines from the file
    def deleteFromFile(self, toDeleteName):
        print(toDeleteName)
        with open("data.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            for i in range(0, len(self.buttons)):
                if i != toDeleteName:
                    writer.writerow([self.buttons[i].name, self.buttons[i].path])