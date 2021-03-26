import tkinter as tk
from tkinter import ttk
from random import randint
from math import ceil
from time import sleep

class SortBoard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=int(parent.cget('width')), height=(int(parent.cget('height'))*0.85)//1, background='black')
   
        self.parent = parent
        self.numberData = 10;
        self.sortingMethod = 'Bubble Sort'
        self.sorting = False
        self.data = []
        self.rectangles = []

    def generate(self, number):
        self.numberData = int(number)
        self.data = [randint(1, self.numberData) for _ in range(self.numberData)]
        if len(self.rectangles) != 0:
            for rectangle in self.rectangles: self.delete(rectangle)
        self.rectangles = self.__createRectangles()
        return

    def __createRectangles(self):
        paddingX = (int(self.cget('width'))*0.1) // 1
        rectangleWidth = ceil((int(self.cget('width'))-(2*paddingX)) / self.numberData)
        paddingX = (int(self.cget('width')) - (rectangleWidth*self.numberData)) // 2

        paddingY = (int(self.cget('height'))*0.1) // 1
        rectangleHeight = ceil((int(self.cget('height'))-paddingY) / self.numberData)
        paddingY = int(self.cget('height')) - (rectangleHeight*self.numberData)

        return [self.create_rectangle(paddingX+rectangleWidth*x, int(self.cget('height'))-y*rectangleHeight, paddingX+rectangleWidth*x+rectangleWidth, int(self.cget('height')), fill='white') for (x,y) in enumerate(self.data)] 

    def sortData(self, method):
        self.sortingMethod = method
        if method == "Bubble Sort": self.__bubbleSort()
        elif method == "Quick Sort": self.__quickSort()
        elif method == "Merge Sort": self.__mergeSort()
        elif method == "Shell Sort": self.__shellSort() 
        return      

    def __swap(self, a, b):
        if (a != b):
            #Swaping the rectangles sizes
            (x0, y0, x1, y1) = self.coords(self.rectangles[a])
            (x2, y2, x3, y3) = self.coords(self.rectangles[b])
            self.coords(self.rectangles[a], x0, y2, x1, y1)
            self.coords(self.rectangles[b], x2, y0, x3, y3)

            #Swaping the rectangles colors
            if self.sortingMethod != "Quick Sort":
                self.itemconfig(self.rectangles[a], fill='white')
                if (b < len(self.rectangles)-1): self.itemconfig(self.rectangles[b], fill='red')

            #Swaping the values in the array
            self.data[a], self.data[b] = self.data[b], self.data[a]
        return

    def __bubbleSort(self):
        isSorted = False
        while not isSorted:
            isSorted = True
            for i in range(len(self.data)-1):
                #If stop button is pressed
                if not self.sorting: return

                self.itemconfig(self.rectangles[i], fill='red')
                self.update()

                if (self.data[i] > self.data[i+1]):
                    isSorted = False
                    self.__swap(i, i+1)

                else: self.itemconfig(self.rectangles[i], fill='white') 
                sleep(1/self.numberData**2)

        self.parent.sortControls.generateButton['state'] = 'normal'
        return 

    def __quickSort(self):
        self.__actualQuickSort(0, len(self.data)-1)  
        self.parent.sortControls.generateButton['state'] = 'normal'
        return

    def __actualQuickSort(self, left, right):
        if right > left:
            index = self.__partition(left, right)
            if (index != -1):   #If stop button was pressed
                self.__actualQuickSort(left, index-1)
                self.__actualQuickSort(index+1, right)
        return

    def __partition(self, left, right):
        pivot = self.data[right]
        i = left-1

        for j in range(left, right):
            #If stop button is pressed
            if not self.sorting: return -1

            self.itemconfig(self.rectangles[j], fill='red')
            self.update()
            
            if (self.data[j] <= pivot):
                i += 1
                self.__swap(i, j)

            sleep(1/self.numberData)
            self.itemconfig(self.rectangles[j], fill='white')
            
        self.__swap(i+1, right)
        return i+1

    def __mergeSort(self):
        merged = [0 for _ in self.data]
        self.__actualMergeSort(merged, 0, len(self.data)-1)
        self.parent.sortControls.generateButton['state'] = 'normal'
        return

    def __actualMergeSort(self, container, left, right):
        if right > left:
            half = (left+right) // 2
            self.__actualMergeSort(container, left, half)
            self.__actualMergeSort(container, half+1, right)
            self.__mergeHalves(container, left, right)
        return
    
    def __mergeHalves(self, container, leftStart, rightEnd):
        start = leftStart
        leftEnd = (leftStart + rightEnd) // 2
        rightStart = leftEnd + 1
        c = leftStart

        while (leftStart <= leftEnd) and (rightStart <= rightEnd):
            if (self.data[leftStart] <= self.data[rightStart]): 
                container[c] = self.data[leftStart]
                leftStart += 1
            else:
                container[c] = self.data[rightStart]
                rightStart += 1
            c += 1

        while (leftStart <= leftEnd):
            container[c] = self.data[leftStart]
            leftStart += 1
            c += 1
        
        while (rightStart <= rightEnd):
            container[c] = self.data[rightStart]
            rightStart += 1
            c += 1

        for j in range(start, rightEnd+1):
            #If stop button is pressed
            if not self.sorting: return

            (x0, y0, x1, y1) = self.coords(self.rectangles[j])
            rectangleHeight = (int(self.cget('height')) - y0) // self.data[j]
            self.data[j] = container[j]
            self.itemconfig(self.rectangles[j], fill='red')
            self.coords(self.rectangles[j], x0, int(self.cget('height')) - rectangleHeight*self.data[j], x1, y1)
            self.update()
            sleep(1/self.numberData)
            self.itemconfig(self.rectangles[j], fill='white')