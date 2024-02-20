from tkinter import *
from tkinter import messagebox

class payWindowClass:
    def __init__(self, master):
        self.master = master
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        # Labels and entry fields for player's name and payment amount
        Label(self.payWindow, text="Spillerens navn:").pack()
        self.player_name = Entry(self.payWindow)
        self.player_name.pack()

        Label(self.payWindow, text="Indbetal:").pack()
        self.money = Entry(self.payWindow)
        self.money.pack()

        # Button to add payment
        self.button = Button(self.payWindow, text="Betal", command=self.addMoney)
        self.button.pack()

    def addMoney(self):
        # Get player's name and payment amount from entry fields
        player_name = self.player_name.get()
        try:
            amount = int(self.money.get())
        except ValueError:
            messagebox.showerror(parent=self.payWindow, title="Fejl", message="Ugyldigt beløb! Indtast kun heltal.")
            return

        # Update total amount and progress bar
        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        # Add player and payment information to the list
        self.master.fodboldtur[player_name] = amount

        # Print confirmation message
        print(f"{player_name} har betalt {amount} kr.")
