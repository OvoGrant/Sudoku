from random import random
import pygame
from scipy import rand
from .Constants import WHITE, BLACK, ROWS, HEIGHT
from .Cell import cell
from math import ceil,floor
import requests

class Board:
    def get_board(self):
        url = 'https://sugoku.herokuapp.com/board?difficulty=random'
        response =  requests.get(url)
        return (response.json())
    x = lambda self , r: 3 if r % 3 == 0 else 1
    ran = lambda self: floor(random()*9) 
    rand = lambda self: floor(random()*9) + 1 
    def __init__(self):
        self.cellsList =  []
        self.selected_cell = None
        self.game = False
    def select(self, x , y):
        self.selected_cell = self.cellsList[x][y]
        print(self.selected_cell.num)
    def draw_self(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row*(HEIGHT/ROWS), 0) , (row*(HEIGHT/ROWS),HEIGHT),width = self.x(row))
        for row in range(ROWS + 1):
            pygame.draw.line(window, BLACK, (0,row*(HEIGHT/ROWS)), (HEIGHT,row*(HEIGHT/ROWS)),width = self.x(row))
        for row in range(len(self.cellsList)):
            for col in range(len(self.cellsList)):
                self.cellsList[row][col].draw_self(window)
    def toMatrix(self,matrix):
        wor = [[int(x.num) for x in row] for row in matrix]
        return wor

    def solved(self):
        tmp = self.toMatrix(self.cellsList)
        print(tmp)
        self.solve(tmp)
        self.create_board(tmp)

    def create_board(self,board_data=[]):
        if len(board_data) == 0 and not self.game:
            board_data = self.get_board()['board']
            self.game = True
        q = []
        for i in range(len(board_data)):
            tmp = []
            for x in range(len(board_data)):
                tmp.append(cell(i,x,str(board_data[i][x])))
            q.append(tmp)
        self.cellsList = q
            

     #check if the current arrangement of numbers is a valid state       
    def isValid(self,row,column,value,grid):
        valid_row = all([value != grid[row][x] for x in range(9)])
        if valid_row:
            valid_column = all([value != grid[x][column] for x in range(9)])
            if valid_column:
                topx,topy =  3 * (row//3) , 3*(column//3)
                for x in range(topx,topx+3):
                    for y in range(topy,topy+3):
                        if grid[x][y] == value:
                            return False
                return True
        return False
    def find(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    return (i,j)

        return False

    def solve(self,grid):
        find = self.find(grid)
        if not find:
            return True
        else:
            row ,col = find
            for x in range(1,10):
                if self.isValid(row,col,x,grid):
                    print("hello")
                    grid[row][col] = x
                    if  self.solve(grid):
                        return True
                    grid[row][col] = 0
        return False


   


        
        

             