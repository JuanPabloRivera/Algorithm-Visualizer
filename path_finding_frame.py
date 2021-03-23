import tkinter as tk
from tkinter import ttk
from path_finding_controls import PathFindingControls
from path_finding_board import PathFindingBoard

class PathFindingFrame(tk.Frame):
    def __init__(self, parent, width, height, showMain, showSorting):
        super().__init__(parent, width=width, height=height)

        self.rowconfigure(0, weight=1)

        self.pathFindingBoard = PathFindingBoard(self)
        self.pathFindingControls = PathFindingControls(self, showMain, showSorting)

        self.pathFindingControls.grid(row=0, column=0, sticky='EW')
        self.pathFindingBoard.grid(row=1, column=0, sticky='EW')