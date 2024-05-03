'''
@coding=UTF-8
@auther:Yanbo Zhu
@time:2024-05
@ui:Main
'''

from ui.LoginPage import LoginPage
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)