import pygame, time, random, sys


pygame.init()

display_width = 800
display_height = 600

#Kleuren
black = (0,0,0)
white = (255,255,255)
red = (200, 0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255, 0,0)
bright_green = (0, 255, 0)
bright_blue = (0,0,255)
grey = (220,220,220)

ship_width = 130

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Battle Port Rotterdam')
clock = pygame.time.Clock()

shipImg = pygame.image.load('ship-test.png').convert()
gameMenu = pygame.image.load("game-menu.jpg").convert()
regelsnl = pygame.image.load("RegelsNederlands.png").convert()
regelsen = pygame.image.load("RegelsEngels.png").convert()

def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("arial",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2),(display_height / 2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crashIntoWall():
    message_display('Crashed!')

def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("arial", 20)
        textSurf, textRect = text_objects(msg,smallText)
        textRect.center = ( (x + (w / 2)), y +(h / 2) )
        gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def high_score():

    highscore = True
    while highscore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(gameMenu,[0,0])

        largeText = pygame.font.SysFont("arial",80)
        TextSurf, TextRect = text_objects("Highscore:", largeText)
        TextRect.center = ((display_width / 2),(display_height - 400))
        gameDisplay.blit(TextSurf,TextRect)

        button("Terug",700,550,100,50,red,bright_red,toMenu)

        pygame.display.update()
        clock.tick(15)

def text_white(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def toRulesNL():
    pygame.display.update()
    rules()

def toRulesEN():
    pygame.display.update()
    rules_en()

def rules():
    x = 10
    y = 10
    rules = True
    while rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(gameMenu, [0, 0])
        gameDisplay.blit(regelsnl, (x, y))

        button("Terug", 700, 550, 100, 50, red, bright_red, toMenu)
        button("English", 600, 550, 100, 50, red, bright_red, toRulesEN)


        pygame.display.update()
        clock.tick(15)


def rules_en():
    x = 10
    y = 10
    rules_en = True
    while rules_en:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(gameMenu, [0, 0])
        gameDisplay.blit(regelsen, (x, y))

        button("Terug", 700, 550, 100, 50, red, bright_red, toMenu)
        button("Nederlands", 600, 550, 100, 50, red, bright_red, toRulesNL)


        pygame.display.update()
        clock.tick(15)


def gameBoard():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameDisplay.fill(grey)
    clock = pygame.time.Clock()

    #Grid opties
    grid_width = 30
    grid_height = 30
    grid_margin = 5

    # Create a 2 dimensional array. A two dimensional array is simply a list of lists.
    grid = []
    for row in range(18):
        # Lege array die elke kolomcel vasthoudt
        grid.append([])
        for column in range(19):
            grid[row].append(0)  # Toevoegen van een kolomcel aan de array
    # Set row 1, cell 5 to one. (Remember rows and column numbers start at zero.)
    #grid[1][5] = 1

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Muisklik positie ophalen
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (grid_width + grid_margin)
                row = pos[1] // (grid_height + grid_margin)
                # Set that location to one
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
        button("Stop",670,550,130,50,red,bright_red,toMenu)
        pygame.display.flip()
        clock.tick(60)

def toMenu():
    pygame.display.update()
    game_intro()

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(gameMenu,[0,0])
        largeText = pygame.font.SysFont("arial",115)
        TextSurf, TextRect = text_objects("BattlePort", largeText)
        TextRect.center = ((display_width / 2),(display_height / 2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Start",75,450,100,50,green,bright_green,game_loop)
        button("Highscore",275,450,100,50,blue,bright_blue,high_score)
        button("Rules",475,450,100,50,grey,white,rules)
        button("Quit",675,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        button("Board Test",520,0,120,50,blue,bright_blue,gameBoard)
        button("Stop",720,0,80,50,red,bright_red,toMenu)
        ship(x,y)

        if x > display_width - ship_width or x < 0:
            crashIntoWall()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
