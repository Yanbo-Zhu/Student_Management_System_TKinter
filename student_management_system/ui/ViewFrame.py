import tkinter as tk
from tkinter import ttk
from data.database import db
import time
from PIL import Image, ImageTk
import PIL as pil


class View_WelcomeFrame(tk.Frame):
    """generate the Welcome View in Main Page"""

    def __init__(self, master):
        super().__init__(master)

        def getTime():
            Stime.configure(text=time.strftime('%H:%M:%S'))
            self.after(1000, getTime)

        self.frame = tk.Frame(self, bg='lightblue')
        self.frame.pack()

        Stime = tk.Label(self.frame, text='', bg='lightblue', font=('Arial', 15), pady=10)
        Stime.grid(row=0, column=0, columnspan=6)
        getTime()

        tk.Label(self.frame, text='Hello', bg='lightblue', font=('Arial', 13), pady=5).grid(row=1, column=0, columnspan=6)

        # insert welcome image
        image = pil.ImageTk.PhotoImage(pil.Image.open('../data/welcome.jpg'))
        image_label = tk.Label(self.frame, image=image,
                               bg='lightblue')  # NOTE: grid() is returning NoneValue, which means that your variable 'file' will be NoneValue.
        image_label.image = image  # keep a reference!
        image_label.grid(row=2, column=0, rowspan=6, columnspan=6, ipady=10)


class View_InsertFrame(tk.Frame):
    """generate the Insert View in Main Page"""

    def __init__(self, master):
        super().__init__(master)

        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.deutsch = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, column=0)

        tk.Label(self, text='Please insert the student grade', font=10).grid(row=1, column=1, sticky='', columnspan=2, padx=10, pady=10)

        tk.Label(self, text="Name").grid(sticky='w', row=2, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, padx=10, pady=10)

        tk.Label(self, text="Math").grid(sticky='w', row=3, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=3, column=2, padx=10, pady=10)

        tk.Label(self, text="English").grid(sticky='w', row=4, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, padx=10, pady=10)

        tk.Label(self, text="Deutsch").grid(sticky='w', row=5, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.deutsch).grid(row=5, column=2, padx=10, pady=10)

        tk.Button(self, text="Submit", command=self.submit_grade).grid(sticky='e', row=6, column=2, padx=10, pady=10)

        tk.Label(self, textvariable=self.status, fg="red").grid(row=7, column=2, padx=10, pady=10)

    def submit_grade(self):
        """Function for Submit Button"""
        if self.name.get() == "" or self.math.get() == "" or self.english.get() == "" or self.deutsch.get() == "":
            self.status.set("Please fill in all fields")
        else:
            student_grade = {'name': self.name.get(), 'math': self.math.get(), 'english': self.english.get(), 'deutsch': self.deutsch.get()}
            flag, message = db.insert_student(student_grade)
            self.status.set(message)


class View_ModifyFrame(tk.Frame):
    """generate the Modify View in Main Page"""

    def __init__(self, master):
        super().__init__(master)

        self.name = tk.StringVar()
        self.math = tk.StringVar()
        self.english = tk.StringVar()
        self.deutsch = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, column=0)

        tk.Label(self, text='Please search the student name and modify the grade', font=10).grid(row=1, column=1, sticky='', columnspan=2,
                                                                                                 padx=10, pady=10)

        tk.Label(self, text="Name").grid(sticky='w', row=2, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=2, column=2, padx=10, pady=10)

        tk.Label(self, text="Math").grid(sticky='w', row=3, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=3, column=2, padx=10, pady=10)

        tk.Label(self, text="English").grid(sticky='w', row=4, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, padx=10, pady=10)

        tk.Label(self, text="Deutsch").grid(sticky='w', row=5, column=1, padx=10, pady=10)
        tk.Entry(self, textvariable=self.deutsch).grid(row=5, column=2, padx=10, pady=10)

        tk.Button(self, text="Search", command=self.search_grade).grid(sticky='w', row=6, column=1, padx=10, pady=10)
        tk.Button(self, text="Modify", command=self.change_grade).grid(sticky='e', row=6, column=2, padx=10, pady=10)

        tk.Label(self, textvariable=self.status, fg="red").grid(row=7, column=1, sticky='', columnspan=2, padx=10, pady=10)

    def search_grade(self):
        """Function for Search Button"""
        if self.name.get() == "":
            self.status.set("Please fill in the name field")
        else:
            flag, info = db.search_by_name(self.name.get())
            if flag:
                self.name.set(info['name'])
                self.math.set(info['math'])
                self.english.set(info['english'])
                self.deutsch.set(info['deutsch'])
                self.status.set("Found")
            else:
                self.status.set(info)

    def change_grade(self):
        """Function for Modify Button"""
        if self.name.get() == "" or self.math.get() == "" or self.english.get() == "" or self.deutsch.get() == "":
            self.status.set("Please fill in all fields")
        else:
            student_grade = {'name': self.name.get(), 'math': self.math.get(), 'english': self.english.get(), 'deutsch': self.deutsch.get()}
            flag, message = db.update_by_name(student_grade)
            self.status.set(message)
        pass


class View_DeleteFrame(tk.Frame):
    """generate the Delete View in Main Page"""

    def __init__(self, master):
        super().__init__(master)
        # tk.Label(self, text='Delete').pack()
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='Please enter the student name (case insensitive)').pack(pady=5)
        tk.Entry(self, textvariable=self.username).pack(pady=5)
        tk.Button(self, text='Delete', command=self.delete_student).pack(pady=5)
        tk.Label(self, textvariable=self.status, fg="red").pack(pady=5)

    def delete_student(self):
        """Function for Delete Button"""
        if self.username.get() == "":
            self.status.set("Please enter the student name")
        else:
            student_name = self.username.get()
            flag, message = db.delete_by_name(student_name)
            self.status.set(message)


class View_DisplayFrame(tk.Frame):
    """generate the Display View in Main Page"""

    def __init__(self, master):
        super().__init__(master)

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

    def create_page(self):
        columns = ("name", "math", "english", "deutsch")
        columns_values = ("name", "math", "english", "deutsch")
        self.tree_view = ttk.Treeview(self, columns=columns, show="headings")
        self.tree_view.column("name", width=100, anchor="center")
        self.tree_view.column("math", width=100, anchor="center")
        self.tree_view.column("english", width=100, anchor="center")
        self.tree_view.column("deutsch", width=100, anchor="center")

        self.tree_view.heading("name", text="name")
        self.tree_view.heading("math", text="math")
        self.tree_view.heading("english", text="english")
        self.tree_view.heading("deutsch", text="deutsch")

        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data_frame()

        tk.Button(self, text="Refresh", command=self.show_data_frame).pack(anchor=tk.E, pady=5)

    def sort_data(self):
        """sort the student information according to the attribute"""
        rows = [(self.tree_view.item(item, 'values'), item) for item in self.tree_view.get_children('')]
        # if you want to sort according to a single column:
        # rows = [(tree.set(item, column), item) for item in tree.get_children('')]
        rows.sort()
        rows.reverse()

        # rearrange items in sorted positions
        for index, (values, item) in enumerate(rows):
            self.tree_view.move(item, '', index)

    def show_data_frame(self):
        """Generate the tablear View to display the student grade"""

        # Clean the previous tree_view at first
        for _ in map(self.tree_view.delete, self.tree_view.get_children("")):
            pass

        # Display the tree_view according to the current student grade data
        students = db.student_grade_list()
        index = 0
        for student in students:
            self.tree_view.insert("", index + 1, values=(student["name"], student["math"], student["english"], student["deutsch"]))

        # sort the student grade
        self.sort_data()


class View_AboutFrame(tk.Frame):
    """generate the About View in Main Page"""

    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text='Auther: Yanbo Zhu').pack()
        tk.Label(self, text='Framework: TKinter').pack()
        tk.Label(self, text='Description: view, insert, modify, delete student grade information').pack()
