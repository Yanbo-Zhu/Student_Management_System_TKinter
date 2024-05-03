import tkinter as tk
from ui.ViewFrame import View_WelcomeFrame, View_InsertFrame, View_ModifyFrame, View_DeleteFrame, View_DisplayFrame, View_AboutFrame


class MainPage:
    """generate the Main Page"""
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title("Student Grade Management System")
        self.root.geometry("500x350")
        self.root['bg'] = 'lightblue'
        self.root.attributes('-alpha', 0.9)
        self.create_page()

    def create_page(self):
        self.welcome_frame = View_WelcomeFrame(self.root)
        self.welcome_frame.pack()

        self.modify_frame = View_ModifyFrame(self.root)
        self.insert_frame = View_InsertFrame(self.root)
        self.display_frame = View_DisplayFrame(self.root)
        self.delete_frame = View_DeleteFrame(self.root)
        self.about_frame = View_AboutFrame(self.root)

        # create a menu bar
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Insert', command=self.show_insert_frame)
        menubar.add_command(label='Modify', command=self.show_modify_frame)
        menubar.add_command(label='Display', command=self.show_display_frame)
        menubar.add_command(label='Delete', command=self.show_delete_frame)
        menubar.add_command(label='About', command=self.show_about_frame)
        self.root['menu'] = menubar

    def show_insert_frame(self):
        self.welcome_frame.pack_forget()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack()
        self.delete_frame.pack_forget()
        self.display_frame.pack_forget()

    def show_modify_frame(self):
        self.welcome_frame.pack_forget()
        self.about_frame.pack_forget()
        self.modify_frame.pack()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.display_frame.pack_forget()

    def show_delete_frame(self):
        self.welcome_frame.pack_forget()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack()
        self.display_frame.pack_forget()

    def show_display_frame(self):
        self.welcome_frame.pack_forget()
        self.about_frame.pack_forget()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.display_frame.pack()

    def show_about_frame(self):
        self.welcome_frame.pack_forget()
        self.about_frame.pack()
        self.modify_frame.pack_forget()
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.display_frame.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
