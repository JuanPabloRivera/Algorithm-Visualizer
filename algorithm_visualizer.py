import tkinter as tk
from tkinter import ttk
from main_frame import MainFrame
from sort_frame import SortFrame
from path_finding_frame import PathFindingFrame

class Algorithm_Visualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Algorithm Visualizer")
        self.width = 1800
        self.height = 1000

        self.frames = dict()

        self.mainFrame = MainFrame(self, self.width, self.height, lambda: self.__showFrame("Sort"), lambda: self.__showFrame("PathFinding"))
        self.sortFrame = SortFrame(self, self.width, self.height, lambda: self.__showFrame("Main"), lambda: self.__showFrame("PathFinding"))
        self.pathFindingFrame = PathFindingFrame(self, self.width, self.height, lambda: self.__showFrame("Main"), lambda: self.__showFrame("Sort"))

        self.mainFrame.grid(row=0, column=0, sticky='NSEW')
        self.sortFrame.grid(row=0, column=0, sticky='NSEW')
        self.pathFindingFrame.grid(row=0, column=0, sticky='NSEW')

        self.frames["Main"] = self.mainFrame
        self.frames["Sort"] = self.sortFrame
        self.frames["PathFinding"] = self.pathFindingFrame

        #Displaying main frame at launch
        self.__showFrame("Main")

    def __showFrame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = Algorithm_Visualizer()
app.mainloop()