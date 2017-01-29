import pygame, Colors, Images, Functions
from pygame.locals import *

pygame.init()
display_width = 800
display_height = 600
event = pygame.event.get()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battle Port Rotterdam')


def intro():
    while not quitgame():
        gameDisplay.blit(Images.gameMenu, (0,0))
        Functions.screentext("arila", 115, "BattlePort", display_width/2, display_height/2, Colors.black)
        Functions.button("Start",175,450,100,50,Colors.green,Colors.bright_green, player1)
        Functions.button("Highscore",295,450,100,50,Colors.blue,Colors.bright_blue,high_score)
        Functions.button("Rules",415,450,100,50,Colors.grey,Colors.white,rules)
        Functions.button("Quit",535,450,100,50,Colors.red,Colors.bright_red,quit)
        pygame.display.update()

def gameBoard():
    gameDisplay.fill(Colors.grey)
    grid_width = 30
    grid_height = 30
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

        for row in range(18):
            for column in range(19):
                color = Colors.white
                if grid[row][column] == 1:
                    color = Colors.red
                pygame.draw.rect(gameDisplay,color,
                                 [(grid_margin + grid_width) * column + grid_margin,
                                  (grid_margin + grid_height) * row + grid_margin,grid_width,grid_height])


        gameDisplay.blit(Images.shipImg,(670,450))
        Functions.button("Stop",670,550,130,50,Colors.red,Colors.bright_red, intro)
        pygame.display.flip()

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
        Functions.screentext("comicsansms", 50, "Choose player 1 name:", display_width/2, display_height/3.5, Colors.white)
        Functions.screentext("comicsansms", 50, player1, display_width/2, display_height/2, Colors.white)
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
        Functions.screentext("comicsansms", 50, "Choose player 2 name:", display_width/2., display_height/3.5, Colors.white)
        Functions.screentext("comicsansms", 50, player2, display_width/2, display_height/2, Colors.white)

        pygame.display.update()

def quitgame():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

intro()
pygame.quit()
