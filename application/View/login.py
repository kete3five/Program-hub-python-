import tkinter as tk
import subprocess

#global accounts
#accounts = {}

class loginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("login screen")
        self.root.geometry("450x450")
        #title section ->
        self.title_label = tk.Label(root, text="log in", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        #entry section ->
        #username ->
        self.task_entry = tk.Entry(root, width=25, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        #password ->
        self.task_entry1 = tk.Entry(root, width=25, font=("Arial", 12))
        self.task_entry1.pack(pady=10)
        #buttons ->
        #for logging in ->
        self.loginButton=tk.Button(root,text="Log in",width=10,command=self.logUser)
        self.loginButton.pack(pady=5)
        #for registering ->
        self.registerButton=tk.Button(root,text="Register",width=10,command=self.registerUser)
        self.registerButton.pack(pady=5)
    def logUser(self):
        subprocess.Popen(["python", "something.py"])
        pass
    def registerUser(self):
        pass
if __name__ == "__main__":
    root = tk.Tk()
    app =loginScreen(root)
    root.mainloop()