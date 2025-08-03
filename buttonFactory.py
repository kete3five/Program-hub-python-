import tkinter as tk
import subprocess

class buttonFactory:
    def buttonBuild(self, root, detailsButton, font = ("Arial", 16, "Bold"), width = 10):
        return tk.Button(root, text=detailsButton.name, width=10, command=lambda:subprocess.Popen(["python", detailsButton.path]))