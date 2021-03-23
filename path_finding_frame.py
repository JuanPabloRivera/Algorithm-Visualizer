import tkinter as tk
from tkinter import ttk

class PathFindingFrame(ttk.Frame):
    def __init__(self, parent, width, height, showMain, showSorting):
        super().__init__(parent, width=width, height=height)