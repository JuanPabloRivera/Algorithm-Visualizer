import tkinter as tk
from tkinter import ttk
from sort_controls import SortControls
from sort_board import SortBoard

class SortFrame(tk.Frame):
    def __init__(self, parent, width, height, showMain, showPathFinding):
        super().__init__(parent, width=width, height=height)

        self.rowconfigure(0, weight=1)

        self.sortBoard = SortBoard(self)
        self.sortControls = SortControls(self, showMain, showPathFinding)

        self.sortControls.grid(row=0, column=0, sticky='NSEW')
        self.sortBoard.grid(row=1, column=0, sticky='EW')

    