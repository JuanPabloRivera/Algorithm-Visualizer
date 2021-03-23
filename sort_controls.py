import tkinter as tk
from tkinter import ttk

class SortControls(tk.Frame):
    def __init__(self, parent, showMain, showPathFinding):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.10)//1, background='red')

        padx=20
        self.parent = parent

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        numberLabel = ttk.Label(self, text='Number of points: ')
        numberLabel.grid(row=0, column=0, sticky='EW', padx=padx)
        self.numberBox = tk.Spinbox(self, from_=10, to=500, textvariable=tk.IntVar(value=10), wrap=False)
        self.numberBox.grid(row=0, column=1, sticky='EW', padx=padx)

        methodLabel = ttk.Label(self, text='Sorting method: ')
        methodLabel.grid(row=0, column=2, sticky='EW', padx=padx)
        self.methodBox = ttk.Combobox(self, textvariable=tk.StringVar())
        self.methodBox['values'] = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Shell Sort']
        self.methodBox['state'] = 'readonly'
        self.methodBox.current(0)
        self.methodBox.grid(row=0, column=3, sticky='EW', padx=padx)

        self.generateButton = ttk.Button(self, text='Generate numbers', cursor='hand2', command=self.__generateCommand, state='normal')
        self.generateButton.grid(row=0, column=4, sticky='EW', padx=padx)

        self.sortButton = ttk.Button(self, text='Sort', cursor='hand2', command=self.__sortCommand, state='disabled')
        self.sortButton.grid(row=1, column=0, columnspan=3, sticky='EW', padx=padx)

        self.stopButton = ttk.Button(self, text='Stop', cursor='hand2', command=self.__stopCommand, state='disabled')
        self.stopButton.grid(row=1, column=3, columnspan=2, sticky='EW', padx=padx)

        self.mainButton = ttk.Button(self, text='Main Menu', cursor='hand2', command=showMain, state='normal')
        self.mainButton.grid(row=0, column=6, sticky='EW', padx=padx)
        
        self.pathFindingButton = ttk.Button(self, text='Path Finding', cursor='hand2', command=showPathFinding, state='normal')
        self.pathFindingButton.grid(row=1, column=6, sticky='EW', padx = padx)

    def __generateCommand(self):
        self.sortButton['state'] = 'normal'
        self.parent.sortBoard.generate(self.numberBox.get())

    def __sortCommand(self):
        self.generateButton['state'] = 'disabled'
        self.stopButton['state'] = 'normal'
        self.parent.sortBoard.sorting = True
        self.parent.sortBoard.sortData(self.methodBox.get())

    def __stopCommand(self):
        self.generateButton['state'] = 'normal'
        self.parent.sortBoard.sorting = False
        