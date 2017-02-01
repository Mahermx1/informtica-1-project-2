import pygame,Colors, Images, Functions

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

class ships():
    def __init__(self, img, hp, ap, x, y, moves):
        self.shipimg = img
        self.healthpoints = hp
        self.attackpower = ap
        self.x = x
        self.y = y
        self.moves = moves
    def drawship(self):
        gameDisplay.blit(self.shipimg, (self.x, self.y))
