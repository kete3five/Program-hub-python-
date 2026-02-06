"""docstring module for button"""
import tkinter as tk
import subprocess

class ButtonFactory:
    """a class to create buttons"""
    def button_build(self, root, db):
        """initializes a button"""
        return tk.Button(root, text=db.name, width=10, command=self.open_sp(db.path))
    def open_sp(self, details):
        """opens a subprocess"""
        #subprocess.Popen(["python", details])
        with subprocess.Popen(["python", details]):
            pass
