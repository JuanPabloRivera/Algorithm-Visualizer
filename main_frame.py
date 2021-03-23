import tkinter as tk
from tkinter import ttk

class MainFrame(tk.Frame):
    def __init__(self, parent, width, height, showSort, showPathFinding):
        super().__init__(parent, width=width, height=height, background='red')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.sortingButton = ttk.Button(self, text='Sorting', cursor='hand2', command=showSort)
        self.findingButton = ttk.Button(self, text='Path Finding', cursor='hand2', command=showPathFinding)

        self.sortingButton.grid(row=0, column=0)
        self.findingButton.grid(row=0, column=1)