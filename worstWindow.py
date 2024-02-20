# importing tkinter module
from tkinter import *

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("De 3 taber")
        self.worstWindow.geometry("200x200")


        Label(self.worstWindow, text="De værste betalere").pack()

