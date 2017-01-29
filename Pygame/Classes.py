import pygame,Colors, Images, Functions, time

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))


class player():
    def __init__(self):
        pass


class boats():
    def __init__(self, w, h, hp, ap, x, y):
        self.width = w
        self.hight = h
        self.healthpoints = hp
        self.attackpower = ap
        self.x = x
        self.y = y

    def boat(self):
        gameDisplay.blit(Images.shipImg, [self.x, self.y])
