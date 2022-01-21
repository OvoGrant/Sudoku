import pygame
from .Constants import WHITE, BLACK, ROWS, HEIGHT

class Board:
    def __init__(self):
        self.cells = []
        self.solved = False
    def draw_self(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            pygame.draw.line(window, BLACK, (row*(HEIGHT/ROWS), 0) , (row*(HEIGHT/ROWS),HEIGHT))
            pygame.draw.line(window, BLACK, (0,row*(HEIGHT/ROWS)), (HEIGHT,row*(HEIGHT/ROWS)) )