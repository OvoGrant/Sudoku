from re import X
import pygame
from Game.Constants import HEIGHT

class cell:
    def __init__(self,row,column,number):
        self.row = row
        self.column = column
        self.num = number
    def draw_self(self,window):
         text = pygame.font.SysFont(None,30)
         img = text.render(str(self.num),True,(0,0,0),(255,255,255))
         window.blit(img, (self.column*(HEIGHT/9) + 0.4*(HEIGHT/9),self.row*(HEIGHT/9) + 0.3*(HEIGHT/9)))
