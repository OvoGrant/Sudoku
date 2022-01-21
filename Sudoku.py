import pygame
from Game.Constants import SQUARE_SIZE, WIDTH, HEIGHT;
from Game.Board import Board
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Sudoku')
SQUARE_SIZE 
pygame.font.init()

FPS = 10

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.create_board()
    board.draw_self(WINDOW)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


main()