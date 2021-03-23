import tkinter as tk
from tkinter import ttk

class PathFindingControls(tk.Frame):
    def __init__(self, parent, showMain, showSorting):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.15)//1, background='blue')

        padx = 20
        self.parent = parent

        xStartLabel = ttk.Label(self, text='Start x: ')
        xStartLabel.grid(row=0, column=0, sticky='EW', padx=padx)
        self.xStartBox = tk.Spinbox(self, from_=0, to=parent.pathFindingBoard.xNumberSquares-1, textvariable=tk.IntVar(value=1), wrap=False)
        self.xStartBox.grid(row=0, column=1, sticky='EW', padx=padx)

        yStartLabel = ttk.Label(self, text='Start y: ')
        yStartLabel.grid(row=1, column=0, sticky='EW', padx=padx)
        self.yStartBox = tk.Spinbox(self, from_=0, to=parent.pathFindingBoard.yNumberSquares-1, textvariable=tk.IntVar(value=1), wrap=False)
        self.yStartBox.grid(row=1, column=1, sticky='EW', padx=padx)

        xEndLabel = ttk.Label(self, text='End x: ')
        xEndLabel.grid(row=0, column=2, sticky='EW', padx=padx)
        self.xEndBox = tk.Spinbox(self, from_=0, to=parent.pathFindingBoard.xNumberSquares-1, textvariable=tk.IntVar(value=20), wrap=False)
        self.xEndBox.grid(row=0, column=3, sticky='EW', padx=padx)

        yEndLabel = ttk.Label(self, text='End y: ')
        yEndLabel.grid(row=1, column=2, sticky='EW', padx=padx)
        self.yEndBox = tk.Spinbox(self, from_=0, to=parent.pathFindingBoard.yNumberSquares-1, textvariable=tk.IntVar(value=20), wrap=False)
        self.yEndBox.grid(row=1, column=3, sticky='EW', padx=padx)

        self.clearButton = ttk.Button(self, text='Clear', cursor='hand2', command=lambda: parent.pathFindingBoard.generate(int(self.xStartBox.get()), int(self.yStartBox.get()), int(self.xEndBox.get()), int(self.yEndBox.get())), state='normal')
        self.clearButton.grid(row=0, column=4, sticky='EW', padx=padx)

        self.mainButton = ttk.Button(self, text='Main Manu', cursor='hand2', command=showMain, state='normal')
        self.mainButton.grid(row=0, column=5, sticky='EW', padx=padx)

        self.sortingButton = ttk.Button(self, text='Sorting', cursor='hand2', command=showSorting, state='normal')
        self.sortingButton.grid(row=1, column=5, sticky='EW', padx=padx)

