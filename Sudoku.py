import pygame
from Game.Constants import WIDTH, HEIGHT;
from Game.Board import Board
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Sudoku')

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        board.draw_self(WINDOW) 
        pygame.display.update()
    pygame.quit()


main()