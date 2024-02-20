# importing necessary modules
from tkinter import *
from PIL import ImageTk, Image
import pickle

class listWindowClass:
    def __init__(self, master):
        self.master = master
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        # Load data from betalinger.pk
        try:
            with open("betalinger.pk", "rb") as file:
                data = pickle.load(file)
                members = list(data.keys())  # Extract member names from the loaded data
        except FileNotFoundError:
            members = []

            # Display list of members and their payments
            Label(self.listWindow, text="Liste over indbetalinger og England").pack()
            for member in members:
                payment = data[member]  # Get the payment for the current member
                display_text = f"{member}: {payment} kr"
                Label(self.listWindow, text=display_text).pack()


        # Display list of members
        Label(self.listWindow, text="Liste over indbetalinger og England").pack()
        for member in members:
            Label(self.listWindow, text=member).pack()

        # Display image
        img = ImageTk.PhotoImage(Image.open("assets/img/England.png"))
        panel = Label(self.listWindow, image=img)
        panel.image = img
        panel.pack(side="left", fill="both", expand="yes")

