from math import floor
from tkinter import S
import pygame
from Game.Constants import SQUARE_SIZE, WIDTH, HEIGHT;
from Game.Board import Board
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT+60))
pygame.display.set_caption('Sudoku')
SQUARE_SIZE 
pygame.font.init()
import re

FPS = 60
digits = "[0-9]"
getPos = lambda x : floor(x/(HEIGHT/9))*SQUARE_SIZE
getRow = lambda x : floor(getPos(x)/SQUARE_SIZE)

q = range(ord('0'),ord('9')+1)
print(q)
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()
    board.draw_self(WINDOW)
    x = 0
    y = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.selected_cell == None:
                    x,y = pygame.mouse.get_pos()
                    board.select(getRow(x),getRow(y))
                    pygame.draw.rect(WINDOW,(0,255,0),pygame.Rect(getPos(x),getPos(y),SQUARE_SIZE, SQUARE_SIZE),2)
                else:
                    board.draw_self(WINDOW)
                    x,y = pygame.mouse.get_pos()
                    board.select(getRow(x),getRow(y))
                    pygame.draw.rect(WINDOW,(0,255,0),pygame.Rect(getPos(x),getPos(y),SQUARE_SIZE, SQUARE_SIZE),2)
            elif event.type == pygame.KEYDOWN:
                    if event.key in q:
                        c = chr(event.key)
                        print(c)
                        board.selected_cell.num = c
                        board.draw_self(WINDOW)
                        pygame.draw.rect(WINDOW,(0,255,0),pygame.Rect(getPos(x),getPos(y),SQUARE_SIZE, SQUARE_SIZE),2)
                
                
        pygame.display.update()
    pygame.quit()


main()