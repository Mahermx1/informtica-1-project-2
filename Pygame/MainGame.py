import pygame, Colors, Images, Functions, Classes, time
from pygame.locals import *

pygame.init()
display_width = 800
display_height = 600
event = pygame.event.get()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battle Port Rotterdam')
gridImg = pygame.image.load("grid20.png")


def intro():
    while not quitgame():
        gameDisplay.blit(Images.gameMenu, (0,0))
        Functions.screentext("arila", 115, "BattlePort", display_width/2, display_height/2, Colors.black)
        Functions.button("Start",175,450,100,50,Colors.green,Colors.bright_green, player1)
        Functions.button("Highscore",295,450,100,50,Colors.blue,Colors.bright_blue, high_score)
        Functions.button("Rules",415,450,100,50,Colors.grey,Colors.white,rules)
        Functions.button("Quit",535,450,100,50,Colors.red,Colors.bright_red,quit)
        pygame.display.update()

def gameBoard():
    gameDisplay.fill(Colors.grey)
    gameDisplay.blit(gridImg, [0, 0])
    clock = pygame.time.Clock()

    grid_width = 27
    grid_height = 27
    grid_margin = 1


    grid = []
    for row in range(40):
        grid.append([])
        for column in range(40):
            grid[row].append(0)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (grid_width + grid_margin)
                row = pos[1] // (grid_height + grid_margin)
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        #for row in range(20):
            #for column in range(20):
                #color = Colors.white
                #pygame.draw.rect(gameDisplay,color,
                                     #[(grid_margin + grid_width) * column + grid_margin,
                                      #(grid_margin + grid_height) * row + grid_margin,grid_width,grid_height])




        player.turns()
        player.place_boat()
        Functions.button("pause", 670, 0, 130, 50,  Colors.yellow, Colors.bright_yellow, pause)
        Functions.button("Stop",670,550,130,50,Colors.red,Colors.bright_red, intro)

        pygame.display.flip()
        clock.tick(60)

def high_score():
    while not quitgame():
        gameDisplay.blit(Images.gameMenu,[0,0])
        Functions.screentext("arial", 80, "highscore", display_width / 2, display_height - 400, Colors.black)
        Functions.button("Terug",700,550,100,50,Colors.red,Colors.bright_red,intro)
        pygame.display.update()



def rules():
    while not quitgame():
        gameDisplay.blit(Images.gameMenu, [0, 0])
        gameDisplay.blit(Images.regelsnl, (20, 20))
        Functions.button("Terug", 700, 550, 100, 50, Colors.red, Colors.bright_red, intro)
        Functions.button("English", 600, 550, 100, 50, Colors.red, Colors.bright_red, rules_en)
        pygame.display.update()



def rules_en():
    while not quitgame():
        gameDisplay.blit(Images.gameMenu, [0, 0])
        gameDisplay.blit(Images.regelsen, (20, 20))
        Functions.button("Terug", 700, 550, 100, 50, Colors.red, Colors.bright_red, intro)
        Functions.button("Nederlands", 600, 550, 100, 50, Colors.red, Colors.bright_red, rules)
        pygame.display.update()

def pause():
    while not quitgame():
        pygame.draw.rect(gameDisplay,Colors.bright_grey, (245, 145, 20*16, 20*16))
        Functions.screentext("comicsansms", 50, "Paused", (display_width/2), (display_height/3), Colors.black)
        Functions.button("pause", 670, 0, 130, 50,  Colors.yellow, Colors.yellow, None)
        Functions.button("Resume", 340, display_height*9/20, 120, 40,  Colors.green, Colors.bright_green, gameBoard)
        Functions.button("Rules", 340, display_height*11/20, 120, 40,  Colors.blue, Colors.bright_blue, rules)
        Functions.button("Main Menu", 340, display_height*13/20, 120, 40,  Colors.red, Colors.bright_red, intro)
        pygame.display.flip()

saved_player1 = ""
def player1():
    global saved_player1
    player1 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    player1 += evt.unicode
                    saved_player1 = player1
                elif evt.key == K_BACKSPACE:
                    player1 = player1[:-1]
                    saved_player1 = player1
                elif evt.key == K_SPACE:
                    player1 += " "
                    saved_player1 = player1
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(Images.gameMenu, [0, 0])
        Functions.button("Next", 700, 550, 100, 50, Colors.yellow, Colors.bright_yellow, player2)
        Functions.screentext("arial", 50, "  Player 1 name:", display_width/2, display_height/3.5, Colors.white)
        Functions.screentext("arial", 50, player1, display_width/2, display_height/2, Colors.white)
        pygame.display.update()

saved_player2 = ""
def player2():
    global saved_player2
    player2 = ""
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    player2 += evt.unicode
                    saved_player2 = player2
                elif evt.key == K_BACKSPACE:
                    player2 = player2[:-1]
                    saved_player2 = player2
                elif evt.key == K_SPACE:
                    player2 += " "
                    saved_player2 = player2
            elif evt.type == QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(Images.gameMenu, [0, 0])
        Functions.button("Next", 700, 550, 100, 50, Colors.yellow, Colors.bright_yellow, gameBoard)
        Functions.button("previous", 0, 550, 100, 50, Colors.yellow, Colors.bright_yellow, player1)
        Functions.screentext("arial", 50, "  Player 2 name:", display_width/2, display_height/3.5, Colors.white)
        Functions.screentext("arial", 50, player2, display_width/2, display_height/2, Colors.white)

        pygame.display.update()

class player():
    def __init__(self):
        self.active_player = 1
        self.winner = None

        self.turn = 0


    def turns(self):
        pygame.draw.rect(gameDisplay,Colors.bright_grey, (600, 65, 12*12, 12*2))
        pygame.draw.rect(gameDisplay,Colors.bright_grey, (720, 65, 12*5.5, 12*2))
        Functions.screentext("arial", 20, saved_player1, 640, 75, Colors.green if self.active_player == 1 else Colors.red)
        Functions.screentext("arial", 20, saved_player2, 740, 75, Colors.green if self.active_player == 2 else Colors.red)

    def place_boat(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if self.turn <8:
            if self.active_player == 1:
                if click[0] and mouse[0] >= 1 and mouse[0] <= 588 and mouse[1] >= 468 and mouse[1] <= 554:

                    self.turn += 1
                    self.active_player += 1
                    if self.turn == 1:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_red_big,(x,556-125))
                    elif self.turn == 3:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_red_medium,(x,556-125))
                    elif self.turn == 5:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_red_medium,(x,556-125))
                    elif self.turn == 7:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_red_small,(x,556-125))
            elif self.active_player == 2:
                if click[0] and mouse[0] >= 1 and mouse[0] <= 588 and mouse[1] >= 2 and mouse[1] <= 90:

                    self.turn += 1
                    self.active_player -= 1
                    if self.turn == 2:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_blue_big,(x,0))
                    elif self.turn == 4:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_blue_medium,(x,0))
                    elif self.turn == 6:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_blue_medium,(x,0))
                    elif self.turn == 8:
                        x = mouse[0]
                        gameDisplay.blit(Images.ship_blue_small,(x,0))
        else:
            if self.active_player == 1:
                Functions.button("move", 605, 90, 75, 25, Colors.green, Colors.bright_green, None)
                Functions.button("turn", 605, 115, 75, 25, Colors.blue, Colors.bright_blue, None)
                Functions.button("attack", 605, 140, 75, 25, Colors.yellow, Colors.bright_yellow, None)
                Functions.button("end turn", 605, 165, 75, 25, Colors.red, Colors.bright_red, None)

            elif self.active_player == 2:
                Functions.button("move", 705, 90, 75, 25, Colors.green, Colors.bright_green, None)
                Functions.button("turn", 705, 115, 75, 25, Colors.blue, Colors.bright_blue, None)
                Functions.button("attack", 705, 140, 75, 25, Colors.yellow, Colors.bright_yellow, None)
                Functions.button("end turn", 705, 165, 75, 25, Colors.red, Colors.bright_red, None)


def quitgame():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

player = player()
intro()
pygame.quit()
