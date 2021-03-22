import tkinter as tk
from tkinter import ttk
from board import SortBoard
from controls import Controls

class Algorithm_Visualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Algorithm Visualizer")
        self.board = SortBoard(self)
        self.controls = Controls(self)

        self.controls.grid(row=0, column=0, sticky='EW')
        self.board.grid(row=1, column=0, sticky='EW')

app = Algorithm_Visualizer()
app.mainloop()