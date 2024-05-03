import tkinter as tk
from tkinter import messagebox
from data.database import db
from ui.MainPage import MainPage


class LoginPage():
    """generate the Login Page"""
    def __init__(self, master):
        self.root = master
        self.root.geometry('300x180')
        self.root.title("Login")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text="Username").grid(row=1, column=0)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1)

        tk.Label(self.page, text="Password").grid(row=2, column=0, pady=10)
        tk.Entry(self.page, textvariable=self.password, show="*").grid(row=2, column=1)

        tk.Button(self.page, text="Login", command=self.login).grid(row=3, column=0, pady=10)
        tk.Button(self.page, text="Cancel", command=self.page.quit).grid(row=3, column=1)

        self.root.mainloop()

    def login(self):
        """Funtion for Login Button. Check the username and password"""
        name = self.username.get()
        pwd = self.password.get()
        flag, message = db.check_login(name, pwd)

        if flag:
            print("Login successful")
            self.page.destroy()
            MainPage(self.root)
        else:
            messagebox.showwarning("Warning", message)


if __name__ == "__main__":
    root = tk.Tk()
    LoginPage(master=root)
