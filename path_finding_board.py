import tkinter as tk
from tkinter import ttk

class PathFindingBoard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.85)//1, background='white')

        self.findingMethod = "Breath First Search"
        self.finding = False
        self.squareSize = 25
        self.xNumberSquares = int(self.cget('width')) // self.squareSize
        self.yNumberSquares = int(self.cget('height')) // self.squareSize

        self.xStart = 1
        self.yStart = 1
        self.xEnd = self.xNumberSquares - 2
        self.yEnd = self.yNumberSquares - 2
        
        self.data = [[1 for _ in range(self.xNumberSquares)] for _ in range(self.yNumberSquares)]
        self.squares = [[self.create_rectangle(self.squareSize*x, self.squareSize*y, self.squareSize*x + self.squareSize, self.squareSize*y + self.squareSize, fill='white', activefill='#bdd0db', activewidth=2) for x in range(self.xNumberSquares)] for y in range(self.yNumberSquares)]
        self.itemconfig(self.squares[self.yStart][self.xStart], fill='green')
        self.itemconfig(self.squares[self.yEnd][self.xEnd], fill='red')
        
        self.clickPressed = False
        self.clearing = False
        self.settingStart = False
        self.settingEnd = False
        self.bind('<ButtonPress>', self.__onPress)
        self.bind('<ButtonRelease>', self.__onRelease)
        self.bind('<Motion>', self.__motion)
   
    def generate(self):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                self.itemconfig(self.squares[i][j], fill='white', activefill='#bdd0db', activewidth=2)

        self.itemconfig(self.squares[self.yStart][self.xStart], fill='green', activefill='', activewidth=1)
        self.itemconfig(self.squares[self.yEnd][self.xEnd], fill='red', activefill='', activewidth=1)

    def __onPress(self, event):
        self.clickPressed = True
        xSquare = event.x // self.squareSize
        ySquare = event.y // self.squareSize

        if xSquare == self.xStart and ySquare == self.yStart:
            self.settingStart = True
        elif xSquare == self.xEnd and ySquare == self.yEnd:
            self.settingEnd = True
        elif self.data[ySquare][xSquare]:
            self.clearing = False
        else:
            self.clearing = True

    def __onRelease(self, event):
        self.clickPressed = False
        self.settingStart = False
        self.settingEnd = False

    def __motion(self, event):
        if self.clickPressed:
            xSquare = event.x // self.squareSize
            ySquare = event.y // self.squareSize

            if self.settingStart:
                self.itemconfig(self.squares[self.yStart][self.xStart], fill='white', activefill='#bdd0db')
                self.xStart = event.x // self.squareSize
                self.yStart = event.y // self.squareSize
                self.itemconfig(self.squares[ySquare][xSquare], fill='green', activefill='')

            elif self.settingEnd:
                self.itemconfig(self.squares[self.yEnd][self.xEnd], fill='white', activefill='#bdd0db')
                self.xEnd = event.x // self.squareSize 
                self.yEnd = event.y // self.squareSize
                self.itemconfig(self.squares[ySquare][xSquare], fill='red', activefill='')

            elif ((xSquare != self.xStart or ySquare != self.yStart) and (xSquare != self.xEnd or ySquare != self.yEnd)):
                if self.clearing:
                    self.itemconfig(self.squares[ySquare][xSquare], fill='white', activefill='#bdd0db')
                    self.data[ySquare][xSquare] = 1
                else:
                    self.itemconfig(self.squares[ySquare][xSquare], fill='#042f64', activefill='')
                    self.data[ySquare][xSquare] = 0
                