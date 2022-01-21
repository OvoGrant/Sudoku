from random import random
import pygame
from scipy import rand
from .Constants import WHITE, BLACK, ROWS, HEIGHT
from .Cell import cell

x = lambda r : 3 if r % 3 == 0 else 1
class Board:
    def __init__(self):
        self.cellsList =  []
        self.solved = False

    def draw_self(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row*(HEIGHT/ROWS), 0) , (row*(HEIGHT/ROWS),HEIGHT),width = x(row))
            pygame.draw.line(window, BLACK, (0,row*(HEIGHT/ROWS)), (HEIGHT,row*(HEIGHT/ROWS)),width = x(row))
        for row in range(len(self.cellsList)):
            for col in range(len(self.cellsList)):
                self.cellsList[row][col].draw_self(window)

    def create_board(self):
        for row in range(ROWS):
            tmp = []
            for col in range(ROWS):
                num = round(random()*10)
                tmp.append(cell(row,col,num))
                print(num)
            self.cellsList.append(tmp)
             