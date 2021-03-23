import tkinter as tk
from tkinter import ttk

class Controls(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background='red')

        padx = 20
        self.parent = parent

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

    def __generateCommand(self):
        self.sortButton['state'] = 'normal'
        self.parent.board.generate(self.numberBox.get())

    def __sortCommand(self):
        self.generateButton['state'] = 'disabled'
        self.stopButton['state'] = 'normal'
        self.parent.board.sorting = True
        self.parent.board.sortData(self.methodBox.get())

    def __stopCommand(self):
        self.generateButton['state'] = 'normal'
        self.parent.board.sorting = False
        