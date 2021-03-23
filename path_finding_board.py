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
        
        self.data = [[1 for _ in range(self.xNumberSquares)] for _ in range(self.yNumberSquares)]
        self.squares = [[self.create_rectangle(self.squareSize*x, self.squareSize*y, self.squareSize*x + self.squareSize, self.squareSize*y + self.squareSize, fill='white', activefill='#bdd0db', activewidth=2) for x in range(self.xNumberSquares)] for y in range(self.yNumberSquares)]
        
        self.clickPressed = False
        self.clearing = False
        self.bind('<ButtonPress>', self.onPress)
        self.bind('<ButtonRelease>', self.onRelease)
        self.bind('<Motion>', self.motion)
   
    def generate(self, xStart, yStart, xEnd, yEnd):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                self.itemconfig(self.squares[i][j], fill='white', activefill='#bdd0db', activewidth=2)

        self.itemconfig(self.squares[yStart][xStart], fill='green', activefill='', activewidth=1)
        self.itemconfig(self.squares[yEnd][xEnd], fill='red', activefill='', activewidth=1)

    def onPress(self, event):
        self.clickPressed = True
        xSquare = event.x // self.squareSize
        ySquare = event.y // self.squareSize
        if self.data[ySquare][xSquare]:
            self.clearing = False
        else:
            self.clearing = True

    def onRelease(self, event):
        self.clickPressed = False

    def motion(self, event):
        if self.clickPressed:
            xSquare = event.x // self.squareSize
            ySquare = event.y // self.squareSize
            if self.clearing:
                self.itemconfig(self.squares[ySquare][xSquare], fill='white', activefill='#bdd0db')
                self.data[ySquare][xSquare] = 1
            else:
                self.itemconfig(self.squares[ySquare][xSquare], fill='#042f64', activefill='')
                self.data[ySquare][xSquare] = 0
                