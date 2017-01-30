import pygame, time

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battle Port Rotterdam')

black = (0,0,0)
white = (255,255,255)
red = (200, 0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255, 0,0)
bright_green = (0, 255, 0)
bright_blue = (0,0,255)
grey = (220,220,220)

shipImg = pygame.image.load('ship-test.png')
gameMenu = pygame.image.load("game-menu.jpg")
regelsnl = pygame.image.load("RegelsNederlands.png")
regelsen = pygame.image.load("RegelsEngels.png")

def intro():
    while not quitgame():
        gameDisplay.blit(gameMenu,[0,0])
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("BattlePort", largeText)
        TextRect.center = ((display_width / 2),(display_height / 2))
        gameDisplay.blit(TextSurf,TextRect)
        button("Start",175,450,100,50,green,bright_green,gameBoard)
        button("Highscore",275,450,100,50,blue,bright_blue,high_score)
        button("Rules",375,450,100,50,grey,white,rules)
        button("Quit",475,450,100,50,red,bright_red,quit)
        pygame.display.update()



def high_score():
    while not quitgame():
        gameDisplay.blit(gameMenu,[0,0])
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects("Highscore:", largeText)
        TextRect.center = ((display_width / 2),(display_height - 400))
        gameDisplay.blit(TextSurf,TextRect)
        button("Terug",700,550,100,50,red,bright_red,intro)
        pygame.display.update()



def rules():
    while not quitgame():
        gameDisplay.blit(gameMenu, [0, 0])
        gameDisplay.blit(regelsnl, (20, 20))
        button("Terug", 700, 550, 100, 50, red, bright_red, intro)
        button("English", 600, 550, 100, 50, red, bright_red, rules_en)
        pygame.display.update()



def rules_en():
    while not quitgame():
        gameDisplay.blit(gameMenu, [0, 0])
        gameDisplay.blit(regelsen, (20, 20))
        button("Terug", 700, 550, 100, 50, red, bright_red, intro)
        button("Nederlands", 600, 550, 100, 50, red, bright_red, rules)
        pygame.display.update()


def quitgame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                time.sleep(0.12)
                action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects(msg,smallText)
        textRect.center = ( (x + (w / 2)), y +(h / 2) )
        gameDisplay.blit(textSurf, textRect)

def gameBoard():
    gameDisplay.fill(grey)
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (grid_width + grid_margin)
                row = pos[1] // (grid_height + grid_margin)
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        for row in range(18):
            for column in range(19):
                color = white
                if grid[row][column] == 1:
                    color = red
                pygame.draw.rect(gameDisplay,color,
                                 [(grid_margin + grid_width) * column + grid_margin,
                                  (grid_margin + grid_height) * row + grid_margin,grid_width,grid_height])


        gameDisplay.blit(shipImg,(670,450))
        button("Stop",670,550,130,50,red,bright_red,intro)
        pygame.display.flip()


intro()
pygame.quit()
