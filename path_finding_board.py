import tkinter as tk
from tkinter import ttk
import queue
import math
from time import sleep

DARK_ORANGE = '#ec7014'
LIGHT_ORANGE = '#f6a437'
YELLOW = '#ffd366'
DARK_GRAY = '#758a9b'
LIGHT_GRAY = '#b0b0b0'
DARK_BLUE = '#042f64'

class PathFindingBoard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.85)//1, background='white')

        self.parent = parent

        self.findingMethod = "Breath First Search"
        self.finding = False
        self.squareSize = 25
        self.xNumberSquares = int(self.cget('width')) // self.squareSize
        self.yNumberSquares = int(self.cget('height')) // self.squareSize

        self.xStart = 1
        self.yStart = 1
        self.xEnd = self.xNumberSquares - 2
        self.yEnd = self.yNumberSquares - 2
        
        self.data = [[0 for _ in range(self.xNumberSquares)] for _ in range(self.yNumberSquares)]
        self.data[self.yStart][self.xStart] = 1
        self.data[self.yEnd][self.xEnd] = -1
        self.squares = [[self.create_rectangle(self.squareSize*x, self.squareSize*y, self.squareSize*x + self.squareSize, self.squareSize*y + self.squareSize, fill='white', activefill=LIGHT_GRAY, activewidth=2) for x in range(self.xNumberSquares)] for y in range(self.yNumberSquares)]
        self.itemconfig(self.squares[self.yStart][self.xStart], fill=YELLOW)
        self.itemconfig(self.squares[self.yEnd][self.xEnd], fill=DARK_ORANGE)
        
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
                self.data[i][j] = 0
                self.itemconfig(self.squares[i][j], fill='white', activefill=LIGHT_GRAY, activewidth=2)

        self.data[self.yStart][self.xStart] = 1
        self.data[self.yEnd][self.xEnd] = -1
        self.itemconfig(self.squares[self.yStart][self.xStart], fill=YELLOW, activefill='', activewidth=1)
        self.itemconfig(self.squares[self.yEnd][self.xEnd], fill=DARK_ORANGE, activefill='', activewidth=1)

    def __onPress(self, event):
        self.clickPressed = True
        xSquare = event.x // self.squareSize
        ySquare = event.y // self.squareSize

        if xSquare == self.xStart and ySquare == self.yStart:
            self.settingStart = True
        elif xSquare == self.xEnd and ySquare == self.yEnd:
            self.settingEnd = True
        elif not self.data[ySquare][xSquare]:
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
                self.data[self.yStart][self.xStart] = 0
                self.itemconfig(self.squares[self.yStart][self.xStart], fill='white', activefill=LIGHT_GRAY)
                self.xStart = event.x // self.squareSize
                self.yStart = event.y // self.squareSize
                self.data[self.yStart][self.xStart] = 1
                self.itemconfig(self.squares[ySquare][xSquare], fill=YELLOW, activefill='')

            elif self.settingEnd:
                self.data[self.yEnd][self.xEnd] = 0
                self.itemconfig(self.squares[self.yEnd][self.xEnd], fill='white', activefill=LIGHT_GRAY)
                self.xEnd = event.x // self.squareSize 
                self.yEnd = event.y // self.squareSize
                self.data[self.yEnd][self.xEnd] = 2
                self.itemconfig(self.squares[ySquare][xSquare], fill=DARK_ORANGE, activefill='')

            elif ((xSquare != self.xStart or ySquare != self.yStart) and (xSquare != self.xEnd or ySquare != self.yEnd)):
                if self.clearing:
                    self.itemconfig(self.squares[ySquare][xSquare], fill='white', activefill=LIGHT_GRAY)
                    self.data[ySquare][xSquare] = 0
                else:
                    self.itemconfig(self.squares[ySquare][xSquare], fill=DARK_BLUE, activefill='')
                    self.data[ySquare][xSquare] = math.inf

    def find(self, method):
        self.findingMethod = method
        if method == "Breath First Search":
            self.__bfs()
        elif method == "Dijkstra's":
            pass
        elif method == "A*":
            pass

    def __bfs(self):
        prev = self.__bfsSolve()
        self.__bfsReconstructPath(prev)
        self.finding = False
        self.parent.pathFindingControls.clearButton['state'] = 'normal'

    def __bfsSolve(self):
        prev = [[[None, None] for _ in range(self.xNumberSquares)] for _ in range(self.yNumberSquares)]
        q = queue.Queue()
        q.put([self.yStart, self.xStart])

        rowVals = [-1, 1, 0, 0]
        colVals = [0, 0, -1, 1]

        while (not q.empty()):
            current = q.get()
            if (current != [self.yStart, self.xStart]):
                self.itemconfig(self.squares[current[0]][current[1]], fill=LIGHT_GRAY)
                
            for i in range(4):
                newRow = current[0] + rowVals[i]
                newCol = current[1] + colVals[i]
                if (0 <= newRow < self.yNumberSquares) and (0 <= newCol < self.xNumberSquares):
                    if (self.data[newRow][newCol] == -1): #Reached destination
                        prev[self.yEnd][self.xEnd] = [current[0], current[1]]
                        return prev
                    if (self.data[newRow][newCol] not in [1, math.inf]): #Hasn´t been visited and is not a wall
                        prev[newRow][newCol] = [current[0], current[1]]
                        q.put([newRow, newCol])
                        self.data[newRow][newCol] = 1
                        self.itemconfig(self.squares[newRow][newCol], fill=DARK_GRAY)
            self.update()
        return []

    def __bfsReconstructPath(self, prev):
        if len(prev) != 0:     # If a path was found
            current = [self.yEnd, self.xEnd]
            path = [current]
            while(current != [self.yStart, self.xStart]):
                next = prev[current[0]][current[1]]
                path.append(next)
                current = next
            path.reverse()
            
            # Painting the solution path in the board
            for [y, x] in path:
                self.itemconfig(self.squares[y][x], fill=LIGHT_ORANGE) 
                self.update()
                sleep(0.01)


        
                