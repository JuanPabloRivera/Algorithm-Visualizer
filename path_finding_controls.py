import tkinter as tk
from tkinter import ttk

class PathFindingControls(tk.Frame):
    def __init__(self, parent, showMain, showSorting):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.15)//1, background='blue')

        padx = 20
        self.parent = parent

        self.findButton = ttk.Button(self, text='Find', cursor='hand2', state='normal')
        self.findButton.grid(row=0, column=0, sticky='EW', padx=padx)

        self.clearButton = ttk.Button(self, text='Clear', cursor='hand2', command=parent.pathFindingBoard.generate, state='normal')
        self.clearButton.grid(row=1, column=0, sticky='EW', padx=padx)

        self.mainButton = ttk.Button(self, text='Main Manu', cursor='hand2', command=showMain, state='normal')
        self.mainButton.grid(row=0, column=1, sticky='EW', padx=padx)

        self.sortingButton = ttk.Button(self, text='Sorting', cursor='hand2', command=showSorting, state='normal')
        self.sortingButton.grid(row=1, column=1, sticky='EW', padx=padx)

