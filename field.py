import pygame
from constants import Constants

class Field:
    def __init__(self, win, size):
        self.win = win
        self.size = size
        self.x = 0
        self.y = 0
        
        self.img = pygame.image.load('field-2022-kai-dark.png').convert()
        self.img = pygame.transform.scale(self.img, size)
        self.win.blit(self.img, (0, 0))

    def getPos(self):
        self.x = pygame.mouse.get_pos()[0] - 375
        self.y = -1 * (pygame.mouse.get_pos()[1] - 375)
        
        self.x /= 375/72
        self.y /= 375/72
        
        return (round(self.x, 1), round(self.y, 1))
    
    def updatePos(self, win, font):
        posText = font.render(str(self.getPos()), True, Constants.WHITE)
        posTextRect = posText.get_rect()
        posTextRect.center = ((680), (730))
        win.blit(posText, posTextRect)
        
    def updateField(self):
        self.win.blit(self.img, (0, 0))