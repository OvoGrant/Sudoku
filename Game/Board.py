from random import random
import pygame
from scipy import rand
from .Constants import WHITE, BLACK, ROWS, HEIGHT
from .Cell import cell

x = lambda r : 3 if r % 3 == 0 else 1
class Board:
    def __init__(self):
        self.cellsList =  []
        self.selected_cell = None
        self.solved = False
    def select(self, x , y):
        self.selected_cell = self.cellsList[x][y]
        print(self.selected_cell.num)

    def draw_self(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row*(HEIGHT/ROWS), 0) , (row*(HEIGHT/ROWS),HEIGHT),width = x(row))
        for row in range(ROWS + 1):
            pygame.draw.line(window, BLACK, (0,row*(HEIGHT/ROWS)), (HEIGHT,row*(HEIGHT/ROWS)),width = x(row))
        for row in range(len(self.cellsList)):
            for col in range(len(self.cellsList)):
                self.cellsList[row][col].draw_self(window)

    def create_board(self):
        for row in range(ROWS):
            tmp = []
            for col in range(ROWS):
                num = round(random()*9)
                tmp.append(cell(row,col,num))
                print(num)
            self.cellsList.append(tmp)
     #check if the current arrangement of numbers is a valid state       
    def isValid(self,row,column,value):
        valid_row = all([value != self.cellsList[x][row] for x in range(9)])
        if valid_row:
            valid_column = all([value != self.cellsList[column][x] for x in range(9)])
            if valid_column:
                print(x)


             