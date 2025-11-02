import tkinter as tk
import subprocess

class ButtonFactory:
    def buttonBuild(self, root, details_button):
        """initializes a button"""
        return tk.Button(root, text=details_button.name, width=10, command=self.openSP(details_button.path))
    def openSP(self, details):
        """opens a subprocess"""
        subprocess.Popen(["python", details])