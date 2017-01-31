import pygame,Colors, Images, Functions

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

class boats():
    def __init__(self, img, hp, ap, x, y):
        self.boatimg = img
        self.healthpoints = hp
        self.attackpower = ap
        self.x = x
        self.y = y

    def drawboat(self):
        gameDisplay.blit(self.boatimg, (self.x, self.y))
