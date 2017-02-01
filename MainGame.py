import pygame, Colors, Images, Functions, Classes, time
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
        Functions.button("Highscore",295,450,100,50,Colors.blue,Colors.bright_blue, high_score)
        Functions.button("Rules",415,450,100,50,Colors.grey,Colors.white,rules)
        Functions.button("Quit",535,450,100,50,Colors.red,Colors.bright_red,quit)
        pygame.display.update()

def gameBoard():
    gameDisplay.fill(Colors.grey)
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

        for row in range(20):
            for column in range(20):
                color = Colors.white
                pygame.draw.rect(gameDisplay,color,
                                 [(grid_margin + grid_width) * column + grid_margin,
                                  (grid_margin + grid_height) * row + grid_margin,grid_width,grid_height])


        player.turns()
        player.place_ship()
        player.move1()
        player.move2()
        player.attack1()
        player.attack2()
        player.realmove()
        player.attackship()
        player.frame_ship()
        player.announcewinner()
        Functions.button("pause", 670, 0, 130, 50,  Colors.yellow, Colors.bright_yellow, pause)
        Functions.button("Stop",670,550,130,50,Colors.red,Colors.bright_red, intro)
        pygame.display.update()

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
        Functions.button("Refresh", 340, display_height*9/20, 120, 40,  Colors.green, Colors.bright_green, gameBoard)
        Functions.button("Rules", 340, display_height*11/20, 120, 40,  Colors.blue, Colors.bright_blue, rules)
        Functions.button("Main Menu", 340, display_height*13/20, 120, 40,  Colors.red, Colors.bright_red, intro)
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

class Player():
    def __init__(self):
        self.active_player = 1
        self.winner = None

        self.turn = 0

        self.ship1 = False
        self.ship2 = False
        self.ship3 = False
        self.ship4 = False
        self.ship5 = False
        self.ship6 = False
        self.ship7 = False
        self.ship8 = False

        self.ship_move = 0
        self.ship_turn = 0
        self.ship_attackpower = 0

        self.thing = 0

    def base_color(self):
        if self.shipimg1.healthpoints == 0:
            self.shipimg1.shipimg = Images.dead_ship_red_big

        if self.shipimg3.healthpoints == 0:
            self.shipimg3.shipimg = Images.dead_ship_red_medium2

        if self.shipimg5.healthpoints == 0:
            self.shipimg5.shipimg = Images.dead_ship_red_medium3

        if self.shipimg7.healthpoints == 0:
            self.shipimg7.shipimg = Images.dead_ship_red_small

        if self.shipimg2.healthpoints == 0:
            self.shipimg2.shipimg = Images.dead_ship_blue_small

        if self.shipimg4.healthpoints == 0:
            self.shipimg4.shipimg = Images.dead_ship_blue_medium2

        if self.shipimg6.healthpoints == 0:
            self.shipimg6.shipimg = Images.dead_ship_blue_medium3

        if self.shipimg8.healthpoints == 0:
            self.shipimg8.shipimg = Images.dead_ship_blue_big



    def input1(self):
        self.active_player += 1
        self.shipimg1.moves = 1
        self.shipimg3.moves = 2
        self.shipimg5.moves = 2
        self.shipimg7.moves = 3
        self.shipimg1.attackpower = 1
        self.shipimg3.attackpower = 1
        self.shipimg5.attackpower = 1
        self.shipimg7.attackpower = 1
        self.ship_move = 0
        self.ship_turn = 0
        self.ship_attackpower = 0
        self.base_color()
        self.thing = 0

    def input2(self):
        self.active_player -= 1
        self.shipimg2.moves = 3
        self.shipimg4.moves = 2
        self.shipimg6.moves = 2
        self.shipimg8.moves = 1
        self.shipimg2.attackpower = 1
        self.shipimg4.attackpower = 1
        self.shipimg6.attackpower = 1
        self.shipimg8.attackpower = 1
        self.ship_move = 0
        self.ship_turn = 0
        self.ship_attackpower = 0
        self.base_color()
        self.thing = 0


    def turns(self):
        pygame.draw.rect(gameDisplay,Colors.bright_grey, (600, 65, 12*12, 12*2))
        pygame.draw.rect(gameDisplay,Colors.bright_grey, (720, 65, 12*5.5, 12*2))
        Functions.screentext("arial", 20, saved_player1, 640, 75, Colors.green if self.active_player == 1 else Colors.red)
        Functions.screentext("arial", 20, saved_player2, 740, 75, Colors.green if self.active_player == 2 else Colors.red)

    def place_ship(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if self.turn < 8:
            if self.active_player == 1:
                if click[0] and mouse[0] >= 0 and mouse[0] <= 560 and mouse[1] >= 476 and mouse[1] <= 560:

                    self.turn += 1
                    self.active_player += 1
                    if self.turn == 1:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg1 = Classes.ships(Images.ship_red_big, 3, 1, x,(560-108), 1)
                        self.ship1 = True
                    elif self.turn == 3:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg3 = Classes.ships(Images.ship_red_medium2, 2, 1, x,(560-83), 2)
                        self.ship3 = True
                    elif self.turn == 5:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg5 = Classes.ships(Images.ship_red_medium3, 2, 1, x,(560-83), 2)
                        self.ship5 = True
                    elif self.turn == 7:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg7 = Classes.ships(Images.ship_red_small, 1, 1, x,(560-56), 3)
                        self.ship7 = True
            elif self.active_player == 2:
                if click[0] and mouse[0] >= 0 and mouse[0] <= 560 and mouse[1] >= 0 and mouse[1] <= 84:

                    self.turn += 1
                    self.active_player -= 1
                    if self.turn == 2:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg2 = Classes.ships(Images.ship_blue_small, 1, 1, x, 0, 3)
                        self.ship2 = True
                    elif self.turn == 4:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg4 = Classes.ships(Images.ship_blue_medium2, 2, 1, x, 0, 2)
                        self.ship4 = True
                    elif self.turn == 6:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg6 = Classes.ships(Images.ship_blue_medium3, 2, 1, x, 0, 2)
                        self.ship6 = True
                    elif self.turn == 8:
                        x = mouse[0]
                        while x % 28 != 0:
                            x -=1
                        self.shipimg8 = Classes.ships(Images.ship_blue_big, 3, 1, x, 0, 1)
                        self.ship8 = True
        else:
            if self.active_player == 1:
                Functions.button("move", 605, 90, 75, 25, Colors.green, Colors.bright_green, self.move_ship1)
                Functions.button("lol", 605, 115, 75, 25, Colors.blue, Colors.bright_blue, None)
                Functions.button("attack", 605, 140, 75, 25, Colors.yellow, Colors.bright_yellow, self.attack_ship1)
                Functions.button("end turn", 605, 165, 75, 25, Colors.red, Colors.bright_red, self.input1)
                pygame.draw.rect(gameDisplay,Colors.bright_grey, (590, 240, 15*14, 15*14))
                Functions.screentext("comicsansms",15, "Player 1", 685, 250, Colors.bright_red)
                Functions.screentext("comicsansms",15, "ship 1 health:" + str(self.shipimg1.healthpoints),  645, 280, Colors.bright_red)
                Functions.screentext("comicsansms",15, "ship 2 health:" + str(self.shipimg3.healthpoints), 645, 330, Colors.bright_red)
                Functions.screentext("comicsansms",15, "ship 3 health:" + str(self.shipimg5.healthpoints), 645, 380, Colors.bright_red)
                Functions.screentext("comicsansms",15, "ship 4 health:" + str(self.shipimg7.healthpoints), 645, 430, Colors.bright_red)
            elif self.active_player == 2:
                Functions.button("move", 705, 90, 75, 25, Colors.green, Colors.bright_green, self.move_ship2)
                Functions.button("lol", 705, 115, 75, 25, Colors.blue, Colors.bright_blue, None)
                Functions.button("attack", 705, 140, 75, 25, Colors.yellow, Colors.bright_yellow, self.attack_ship2)
                Functions.button("end turn", 705, 165, 75, 25, Colors.red, Colors.bright_red, self.input2)
                pygame.draw.rect(gameDisplay,Colors.bright_grey, (590, 240, 15*14, 15*14))
                Functions.screentext("comicsansms",15, "Player 2", 685, 250, Colors.bright_blue)
                Functions.screentext("comicsansms",15, "ship 1 health:" + str(self.shipimg2.healthpoints), 645, 280, Colors.bright_blue)
                Functions.screentext("comicsansms",15, "ship 2 health:" + str(self.shipimg4.healthpoints), 645, 330, Colors.bright_blue)
                Functions.screentext("comicsansms",15, "ship 3 health:" + str(self.shipimg6.healthpoints), 645, 380, Colors.bright_blue)
                Functions.screentext("comicsansms",15, "ship 4 health:" + str(self.shipimg8.healthpoints), 645, 430, Colors.bright_blue)


    def frame_ship(self):
        if self.ship1 is True:
            self.shipimg1.drawship()
        if self.ship2 is True:
            self.shipimg2.drawship()
        if self.ship3 is True:
            self.shipimg3.drawship()
        if self.ship4 is True:
            self.shipimg4.drawship()
        if self.ship5 is True:
            self.shipimg5.drawship()
        if self.ship6 is True:
            self.shipimg6.drawship()
        if self.ship7 is True:
            self.shipimg7.drawship()
        if self.ship8 is True:
            self.shipimg8.drawship()
            if self.shipimg1.healthpoints == 0 and self.shipimg3.healthpoints == 0 and self.shipimg5.healthpoints == 0 and self.shipimg7.healthpoints == 0:
                self.winner = 1
            if self.shipimg2.healthpoints == 0 and self.shipimg4.healthpoints == 0 and self.shipimg6.healthpoints == 0 and self.shipimg8.healthpoints == 0:
                self.winner = 2


    def move_ship1(self):
        self.thing = 1
        self.ship_move = 0
        self.ship_attackpower = 0
        self.base_color()

    def move_ship2(self):
        self.thing = 4
        self.ship_move = 0
        self.ship_attackpower = 0
        self.base_color()

    def attack_ship1(self):
        self.thing = 3
        self.ship_move = 0
        self.ship_attackpower = 0
        self.base_color()


    def attack_ship2(self):
        self.thing = 6
        self.ship_move = 0
        self.ship_attackpower = 0
        self.base_color()

    def move1(self):
        if self.thing == 1:
            Functions.button("ship 1", 530, 90, 75, 25, Colors.green, Colors.bright_green, self.movemove1)
            Functions.button("ship 2", 530, 115, 75, 25, Colors.green, Colors.bright_green, self.movemove3)
            Functions.button("ship 3", 530, 140, 75, 25, Colors.green, Colors.bright_green, self.movemove5)
            Functions.button("ship 4", 530, 165, 75, 25, Colors.green, Colors.bright_green, self.movemove7)


    def move2(self):
        if self.thing == 4:
            Functions.button("ship 1", 630, 90, 75, 25, Colors.green, Colors.bright_green, self.movemove2)
            Functions.button("ship 2", 630, 115, 75, 25, Colors.green, Colors.bright_green, self.movemove4)
            Functions.button("ship 3", 630, 140, 75, 25, Colors.green, Colors.bright_green, self.movemove6)
            Functions.button("ship 4", 630, 165, 75, 25, Colors.green, Colors.bright_green, self.movemove8)

    def attack1(self):
        if self.thing == 3:
            Functions.button("ship 1", 530, 90, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack1)
            Functions.button("ship 2", 530, 115, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack3)
            Functions.button("ship 3", 530, 140, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack5)
            Functions.button("ship 4", 530, 165, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack7)

    def attack2(self):
        if self.thing == 6:
            Functions.button("ship 1", 630, 90, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack2)
            Functions.button("ship 2", 630, 115, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack4)
            Functions.button("ship 3", 630, 140, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack6)
            Functions.button("ship 4", 630, 165, 75, 25, Colors.yellow, Colors.bright_yellow, self.attackattack8)


    def movemove1(self):
        self.ship_move = 1
        self.base_color()


    def movemove3(self):
        self.ship_move = 3
        self.base_color()


    def movemove5(self):
        self.ship_move = 5
        self.base_color()


    def movemove7(self):
        self.ship_move = 7
        self.base_color()


    def movemove2(self):
        self.ship_move = 2
        self.base_color()


    def movemove4(self):
        self.ship_move = 4
        self.base_color()


    def movemove6(self):
        self.ship_move = 6
        self.base_color()


    def movemove8(self):
        self.ship_move = 8
        self.base_color()


    def realmove(self):
        if self.ship_move == 1:
            if self.shipimg1.moves != 0 and self.shipimg1.healthpoints !=0 :
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg1.x -= 28
                    self.shipimg1.moves -= 1
                    if self.shipimg1.x < 0:
                        self.shipimg1.x += 28
                        self.shipimg1.moves += 1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg1.x += 28
                    self.shipimg1.moves -= 1
                    if self.shipimg1.x > 532:
                        self.shipimg1.x -= 28
                        self.shipimg1.moves += 1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg1.y += 28
                    self.shipimg1.moves -= 1
                    if self.shipimg1.y > 440:
                        self.shipimg1.y -= 28
                        self.shipimg1.moves += 1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg1.y -= 28
                    self.shipimg1.moves -= 1
                    if self.shipimg1.y < 0:
                        self.shipimg1.y += 28
                        self.shipimg1.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 2:
            if self.shipimg2.moves != 0 and self.shipimg2.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg2.x -= 28
                    self.shipimg2.moves -= 1
                    if self.shipimg2.x < 0:
                        self.shipimg2.x += 28
                        self.shipimg2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg2.x += 28
                    self.shipimg2.moves -= 1
                    if self.shipimg2.x > 500:
                        self.shipimg2.x -= 28
                        self.shipimg2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg2.y += 28
                    self.shipimg2.moves -= 1
                    if self.shipimg2.y > 470:
                        self.shipimg2.y -= 28
                        self.shipimg2.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg2.y -= 28
                    self.shipimg2.moves -= 1
                    if self.shipimg2.y < 0:
                        self.shipimg2.y += 28
                        self.shipimg2.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 3:
            if self.shipimg3.moves != 0 and self.shipimg3.healthpoints != 0 :
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg3.x -= 28
                    self.shipimg3.moves -= 1
                    if self.shipimg3.x < 0:
                        self.shipimg3.x += 28
                        self.shipimg3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg3.x += 28
                    self.shipimg3.moves -= 1
                    if self.shipimg3.x > 532:
                        self.shipimg3.x -= 28
                        self.shipimg3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg3.y += 28
                    self.shipimg3.moves -= 1
                    if self.shipimg3.y > 470:
                        self.shipimg3.y -= 28
                        self.shipimg3.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg3.y -= 28
                    self.shipimg3.moves -= 1
                    if self.shipimg3.y < 0:
                        self.shipimg3.y += 28
                        self.shipimg3.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 4:
            if self.shipimg4.moves != 0 and self.shipimg4.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg4.x -= 28
                    self.shipimg4.moves -= 1
                    if self.shipimg4.x < 0:
                        self.shipimg4.x += 28
                        self.shipimg4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg4.x += 28
                    self.shipimg4.moves -= 1
                    if self.shipimg4.x > 532:
                        self.shipimg4.x -= 28
                        self.shipimg4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg4.y += 28
                    self.shipimg4.moves -= 1
                    if self.shipimg4.y > 470:
                        self.shipimg4.y -= 28
                        self.shipimg4.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg4.y -= 28
                    self.shipimg4.moves -= 1
                    if self.shipimg4.y < 0:
                        self.shipimg4.y += 28
                        self.shipimg4.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 5:
            if self.shipimg5.moves != 0 and self.shipimg5.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg5.x -= 28
                    self.shipimg5.moves -= 1
                    if self.shipimg5.x < 0:
                        self.shipimg5.x += 28
                        self.shipimg5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg5.x += 28
                    self.shipimg5.moves -= 1
                    if self.shipimg5.x > 532:
                        self.shipimg5.x -= 28
                        self.shipimg5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg5.y += 28
                    self.shipimg5.moves -= 1
                    if self.shipimg5.y > 470:
                        self.shipimg5.y -= 28
                        self.shipimg5.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg5.y -= 28
                    self.shipimg5.moves -= 1
                    if self.shipimg5.y < 0:
                        self.shipimg5.y += 28
                        self.shipimg5.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 6:
            if self.shipimg6.moves != 0 and self.shipimg6.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg6.x -= 28
                    self.shipimg6.moves -= 1
                    if self.shipimg6.x < 0:
                        self.shipimg6.x += 28
                        self.shipimg6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg6.x += 28
                    self.shipimg6.moves -= 1
                    if self.shipimg6.x > 532:
                        self.shipimg6.x -= 28
                        self.shipimg6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg6.y += 28
                    self.shipimg6.moves -= 1
                    if self.shipimg6.y > 470:
                        self.shipimg6.y -= 28
                        self.shipimg6.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg6.y -= 28
                    self.shipimg6.moves -= 1
                    if self.shipimg6.y < 0:
                        self.shipimg6.y += 28
                        self.shipimg6.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 7:
            if self.shipimg7.moves != 0 and self.shipimg7.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg7.x -= 28
                    self.shipimg7.moves -= 1
                    if self.shipimg7.x < 0:
                        self.shipimg7.x += 28
                        self.shipimg7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg7.x += 28
                    self.shipimg7.moves -= 1
                    if self.shipimg7.x > 532:
                        self.shipimg7.x -= 28
                        self.shipimg7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg7.y += 28
                    self.shipimg7.moves -= 1
                    if self.shipimg7.y > 500:
                        self.shipimg7.y -= 28
                        self.shipimg7.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg7.y -= 28
                    self.shipimg7.moves -= 1
                    if self.shipimg7.y < 0:
                        self.shipimg7.y += 28
                        self.shipimg7.moves +=1
                    time.sleep(0.2)
        elif self.ship_move == 8:
            if self.shipimg8.moves != 0 and self.shipimg8.healthpoints != 0:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.shipimg8.x -= 28
                    self.shipimg8.moves -= 1
                    if self.shipimg8.x < 0:
                        self.shipimg8.x += 28
                        self.shipimg8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_d]:
                    self.shipimg8.x += 28
                    self.shipimg8.moves -= 1
                    if self.shipimg8.x > 532:
                        self.shipimg8.x -= 28
                        self.shipimg8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_s]:
                    self.shipimg8.y += 28
                    self.shipimg8.moves -= 1
                    if self.shipimg8.y > 440:
                        self.shipimg8.y -= 28
                        self.shipimg8.moves +=1
                    time.sleep(0.2)
                elif keys[pygame.K_w]:
                    self.shipimg8.y -= 28
                    self.shipimg8.moves -= 1
                    if self.shipimg8.y < 0:
                        self.shipimg8.y += 28
                        self.shipimg8.moves +=1
                    time.sleep(0.2)


    def attackattack1(self):
       self.ship_attackpower = 1



    def attackattack2(self):
        self.ship_attackpower = 2


    def attackattack3(self):
       self.ship_attackpower = 3

    def attackattack4(self):
        self.ship_attackpower = 4


    def attackattack5(self):
        self.ship_attackpower = 5


    def attackattack6(self):
        self.ship_attackpower = 6

    def attackattack7(self):
       self.ship_attackpower = 7


    def attackattack8(self):
       self.ship_attackpower = 8


    def attackship(self):
        if self.ship_attackpower == 7:
            if self.shipimg1.attackpower != 0 :
                self.draw_rect(Colors.bright_red, self.shipimg7.x, (self.shipimg7.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg7.x, (self.shipimg7.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg7.x, (self.shipimg7.y + 56))
                self.draw_rect(Colors.bright_red, self.shipimg7.x, (self.shipimg7.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg7.x - 28), self.shipimg7.y)
                self.draw_rect(Colors.bright_red, (self.shipimg7.x - 56), self.shipimg7.y)
                self.draw_rect(Colors.bright_red, (self.shipimg7.x - 28), (self.shipimg7.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg7.x - 56), (self.shipimg7.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg7.x + 28), self.shipimg7.y)
                self.draw_rect(Colors.bright_red, (self.shipimg7.x + 56), self.shipimg7.y)
                self.draw_rect(Colors.bright_red, (self.shipimg7.x + 28), (self.shipimg7.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg7.x + 56), (self.shipimg7.y + 28))

        elif self.ship_attackpower == 6:
            if self.shipimg2.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg6.x, (self.shipimg6.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg6.x, (self.shipimg6.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg6.x, (self.shipimg6.y + 56))
                self.draw_rect(Colors.bright_red, self.shipimg6.x, (self.shipimg6.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg6.x - 28), self.shipimg6.y)
                self.draw_rect(Colors.bright_red, (self.shipimg6.x - 56), self.shipimg6.y)
                self.draw_rect(Colors.bright_red, (self.shipimg6.x - 28), (self.shipimg6.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg6.x - 56), (self.shipimg6.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg6.x + 28), self.shipimg6.y)
                self.draw_rect(Colors.bright_red, (self.shipimg6.x + 56), self.shipimg6.y)
                self.draw_rect(Colors.bright_red, (self.shipimg6.x + 28), (self.shipimg6.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg6.x + 56), (self.shipimg6.y + 28))

        elif self.ship_attackpower == 5:
            if self.shipimg3.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y + 84))
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg5.x, (self.shipimg5.y + 140))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 28), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 56), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 84), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 28), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 56), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 84), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 28), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 56), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 84), self.shipimg5.y)
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 28), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 56), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 84), (self.shipimg5.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 28), (self.shipimg5.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 56), (self.shipimg5.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x + 84), (self.shipimg5.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 28), (self.shipimg5.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 56), (self.shipimg5.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg5.x - 84), (self.shipimg5.y + 56))

        elif self.ship_attackpower == 4:
            if self.shipimg4.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y + 84))
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg4.x, (self.shipimg4.y + 140))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 28), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 56), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 84), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 28), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 56), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 84), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 28), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 56), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 84), self.shipimg4.y)
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 28), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 56), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 84), (self.shipimg4.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 28), (self.shipimg4.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 56), (self.shipimg4.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x + 84), (self.shipimg4.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 28), (self.shipimg4.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 56), (self.shipimg4.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg4.x - 84), (self.shipimg4.y + 56))

        elif self.ship_attackpower == 3:
            if self.shipimg5.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y + 84))
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg3.x, (self.shipimg3.y + 140))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 28), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 56), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 84), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 28), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 56), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 84), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 28), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 56), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 84), self.shipimg3.y)
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 28), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 56), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 84), (self.shipimg3.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 28), (self.shipimg3.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 56), (self.shipimg3.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x + 84), (self.shipimg3.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 28), (self.shipimg3.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 56), (self.shipimg3.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg3.x - 84), (self.shipimg3.y + 56))

        elif self.ship_attackpower == 2:
            if self.shipimg6.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y + 84))
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg2.x, (self.shipimg2.y + 140))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 28), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 56), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 84), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 28), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 56), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 84), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 28), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 56), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 84), self.shipimg2.y)
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 28), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 56), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 84), (self.shipimg2.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 28), (self.shipimg2.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 56), (self.shipimg2.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x + 84), (self.shipimg2.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 28), (self.shipimg2.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 56), (self.shipimg2.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg2.x - 84), (self.shipimg2.y + 56))

        elif self.ship_attackpower == 1:
            if self.shipimg7.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y - 28))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y - 56))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y - 112))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y + 140))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y + 168))
                self.draw_rect(Colors.bright_red, self.shipimg1.x, (self.shipimg1.y + 196))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 28), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 56), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 84), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 112), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 28), (self.shipimg1.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 56), (self.shipimg1.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 84), (self.shipimg1.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 112), (self.shipimg1.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 28), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 56), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 84), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 112), self.shipimg1.y)
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 28), (self.shipimg1.y + 45))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 56), (self.shipimg1.y + 45))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 84), (self.shipimg1.y + 45))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 112), (self.shipimg1.y + 45))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 28), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 56), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 84), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 112), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 28), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 56), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 84), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 112), (self.shipimg1.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 28), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 56), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 84), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x + 112), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 28), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 56), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 84), (self.shipimg1.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg1.x - 112), (self.shipimg1.y + 84))

        elif self.ship_attackpower == 8:
            if self.shipimg8.attackpower != 0:
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y - 45))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y - 90))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y - 84))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y - 112))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y + 112))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y + 140))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y + 168))
                self.draw_rect(Colors.bright_red, self.shipimg8.x, (self.shipimg8.y + 196))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 28), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 56), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 84), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 112), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 28), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 56), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 84), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 112), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 28), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 56), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 84), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 112), self.shipimg8.y)
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 28), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 56), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 84), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 112), (self.shipimg8.y + 28))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 28), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 56), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 84), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 112), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 28), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 56), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 84), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 112), (self.shipimg8.y + 56))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 28), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 56), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 84), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x + 112), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 28), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 56), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 84), (self.shipimg8.y + 84))
                self.draw_rect(Colors.bright_red, (self.shipimg8.x - 112), (self.shipimg8.y + 84))

    def draw_rect(self, color, x, y):
        if x >= 0 and x < 560 and y >= 0 and y < 560:
            pygame.draw.rect(gameDisplay, color,(x, y, 27,27))
            if self.ship_attackpower == 1 and self.shipimg1.attackpower != 0 and self.shipimg2.healthpoints != 0:
                if x + 27 > self.shipimg2.x + 14 > x and y + 27 > self.shipimg2.y + 14 > y or x + 27 > self.shipimg2.x + 14 > x and y + 27 > self.shipimg2.y + 39 > y:
                    self.shipimg2.healthpoints -= 1
                    self.shipimg1.attackpower -= 1


            if self.ship_attackpower == 1 and self.shipimg1.attackpower != 0 and self.shipimg4.healthpoints != 0:
                if x + 27 > self.shipimg4.x + 14 > x and y + 27 > self.shipimg4.y + 14 > y or x + 27 > self.shipimg4.x + 14 > x and y + 27 > self.shipimg4.y + 39 > y or x + 27 > self.shipimg4.x + 14 > x and y + 27 > self.shipimg4.y + 112 > y:
                    self.shipimg4.healthpoints -= 1
                    self.shipimg1.attackpower -= 1


            if self.ship_attackpower == 1 and self.shipimg1.attackpower != 0 and self.shipimg6.healthpoints != 0:
                if x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 14 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 39 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 112 > y:
                    self.shipimg6.healthpoints -= 1
                    self.shipimg1.attackpower -= 1


            if self.ship_attackpower == 1 and self.shipimg1.attackpower != 0 and self.shipimg8.healthpoints != 0:
                if x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 14 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 39 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 112 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 98 > y:
                    self.shipimg8.healthpoints -= 1
                    self.shipimg1.attackpower -= 1



            if self.ship_attackpower == 3 and self.shipimg3.attackpower != 0 and self.shipimg2.healthpoints != 0:
                if x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 14 > y or x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 39 > y:
                    self.shipimg2.healthpoints -= 1
                    self.shipimg3.attackpower -= 1


            if self.ship_attackpower == 3 and self.shipimg3.attackpower != 0 and self.shipimg4.healthpoints != 0:
                if x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 14 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 39 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 112 > y:
                    self.shipimg4.healthpoints -= 1
                    self.shipimg3.attackpower -= 1


            if self.ship_attackpower == 3 and self.shipimg3.attackpower != 0 and self.shipimg6.healthpoints != 0:
                if x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 14 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 39 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 112 > y:
                    self.shipimg6.healthpoints -= 1
                    self.shipimg3.attackpower -= 1


            if self.ship_attackpower == 3 and self.shipimg3.attackpower != 0 and self.shipimg8.healthpoints != 0:
                if x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 14 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 39 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 112 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 98 > y:
                    self.shipimg8.healthpoints -= 1
                    self.shipimg3.attackpower -= 1



            if self.ship_attackpower == 5 and self.shipimg5.attackpower != 0 and self.shipimg2.healthpoints != 0:
                if x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 14 > y or x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 39 > y:
                    self.shipimg2.healthpoints -= 1
                    self.shipimg5.attackpower -= 1


            if self.ship_attackpower == 5 and self.shipimg5.attackpower != 0 and self.shipimg4.healthpoints != 0:
                if x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 14 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 39 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 112 > y:
                    self.shipimg4.healthpoints -= 1
                    self.shipimg5.attackpower -= 1


            if self.ship_attackpower == 5 and self.shipimg5.attackpower != 0 and self.shipimg6.healthpoints != 0:
                if x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 14 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 39 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 112 > y:
                    self.shipimg6.healthpoints -= 1
                    self.shipimg5.attackpower -= 1


            if self.ship_attackpower == 5 and self.shipimg5.attackpower != 0 and self.shipimg8.healthpoints != 0:
                if x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 14 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 39 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 112 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 98 > y:
                    self.shipimg8.healthpoints -= 1
                    self.shipimg5.attackpower -= 1


            if self.ship_attackpower == 7 and self.shipimg7.attackpower != 0 and self.shipimg2.healthpoints != 0:
                if x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 14 > y or x+27 > self.shipimg2.x + 14 > x and y+27 > self.shipimg2.y + 39 > y:
                    self.shipimg2.healthpoints -= 1
                    self.shipimg7.attackpower -= 1


            if self.ship_attackpower == 7 and self.shipimg7.attackpower != 0 and self.shipimg4.healthpoints != 0:
                if x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 14 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 39 > y or x+27 > self.shipimg4.x + 14 > x and y+27 > self.shipimg4.y + 112 > y:
                    self.shipimg4.healthpoints -= 1
                    self.shipimg7.attackpower -= 1


            if self.ship_attackpower == 7 and self.shipimg7.attackpower != 0 and self.shipimg6.healthpoints != 0:
                if x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 14 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 39 > y or x+27 > self.shipimg6.x + 14 > x and y+27 > self.shipimg6.y + 112 > y:
                    self.shipimg6.healthpoints -= 1
                    self.shipimg7.attackpower -= 1


            if self.ship_attackpower == 7 and self.shipimg7.attackpower != 0 and self.shipimg8.healthpoints != 0:
                if x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 14 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 39 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 112 > y or x+27 > self.shipimg8.x + 14 > x and y+27 > self.shipimg8.y + 98 > y:
                    self.shipimg8.healthpoints -= 1
                    self.shipimg7.attackpower -= 1



            if self.ship_attackpower == 2 and self.shipimg2.attackpower != 0 and self.shipimg1.healthpoints != 0:
                if x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 14 > y or x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 39 > y:
                    self.shipimg1.healthpoints -= 1
                    self.shipimg2.attackpower -= 1


            if self.ship_attackpower == 2 and self.shipimg2.attackpower != 0 and self.shipimg3.healthpoints != 0:
                if x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 14 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 39 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 70 > y:
                    self.shipimg3.healthpoints -= 1
                    self.shipimg2.attackpower -= 1


            if self.ship_attackpower == 2 and self.shipimg2.attackpower != 0 and self.shipimg5.healthpoints != 0 :
                if x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 14 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 39 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 70 > y:
                    self.shipimg5.healthpoints -= 1
                    self.shipimg2.attackpower -= 1


            if self.ship_attackpower == 2 and self.shipimg2.attackpower != 0 and self.shipimg7.healthpoints != 0:
                if x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 14 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 39 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 70 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 98 > y:
                    self.shipimg7.healthpoints -= 1
                    self.shipimg2.attackpower -= 1



            if self.ship_attackpower == 4 and self.shipimg4.attackpower != 0 and self.shipimg1.healthpoints != 0:
                if x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 14 > y or x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 39 > y:
                    self.shipimg1.healthpoints -= 1
                    self.shipimg4.attackpower -= 1


            if self.ship_attackpower == 4 and self.shipimg4.attackpower != 0 and self.shipimg3.healthpoints != 0:
                if x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 14 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 39 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 70 > y:
                    self.shipimg3.healthpoints -= 1
                    self.shipimg4.attackpower -= 1


            if self.ship_attackpower == 4 and self.shipimg4.attackpower != 0 and self.shipimg5.healthpoints != 0:
                if x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 14 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 39 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 70 > y:
                    self.shipimg5.healthpoints -= 1
                    self.shipimg4.attackpower -= 1


            if self.ship_attackpower == 4 and self.shipimg4.attackpower != 0 and self.shipimg7.healthpoints != 0:
                if x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 14 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 39 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 70 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 98 > y:
                    self.shipimg7.healthpoints -= 1
                    self.shipimg4.attackpower -= 1



            if self.ship_attackpower == 6 and self.shipimg6.attackpower != 0 and self.shipimg1.healthpoints != 0:
                if x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 14 > y or x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 39 > y:
                    self.shipimg1.healthpoints -= 1
                    self.shipimg6.attackpower -= 1


            if self.ship_attackpower == 6 and self.shipimg6.attackpower != 0 and self.shipimg3.healthpoints != 0:
                if x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 14 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 39 > y or x+44 > self.shipimg3.x + 22 > x and y+44 > self.shipimg3.y + 70 > y:
                    self.shipimg3.healthpoints -= 1
                    self.shipimg6.attackpower -= 1


            if self.ship_attackpower == 6 and self.shipimg6.attackpower != 0 and self.shipimg5.healthpoints != 0:
                if x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 14 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 39 > y or x+44 > self.shipimg5.x + 22 > x and y+44 > self.shipimg5.y + 70 > y:
                    self.shipimg5.healthpoints -= 1
                    self.shipimg6.attackpower -= 1


            if self.ship_attackpower == 6 and self.shipimg6.attackpower != 0 and self.shipimg7.healthpoints != 0:
                if x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 14 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 39 > y or x+44 > self.shipimg7.x + 22 > x and y+44 > self.shipimg7.y + 70 > y or x+44 > self.shipimg7.x + 22 > x and y+44 > self.shipimg7.y + 98 > y:
                    self.shipimg7.healthpoints -= 1
                    self.shipimg6.attackpower -= 1



            if self.ship_attackpower == 8 and self.shipimg8.attackpower != 0 and self.shipimg1.healthpoints != 0:
                if x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 14 > y or x+27 > self.shipimg1.x + 14 > x and y+27 > self.shipimg1.y + 39 > y:
                    self.shipimg1.healthpoints -= 1
                    self.shipimg8.attackpower -= 1


            if self.ship_attackpower == 8 and self.shipimg8.attackpower != 0 and self.shipimg3.healthpoints != 0:
                if x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 14 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 39 > y or x+27 > self.shipimg3.x + 14 > x and y+27 > self.shipimg3.y + 70 > y:
                    self.shipimg3.healthpoints -= 1
                    self.shipimg8.attackpower -= 1


            if self.ship_attackpower == 8 and self.shipimg8.attackpower != 0 and self.shipimg5.healthpoints != 0:
                if x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 14 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 39 > y or x+27 > self.shipimg5.x + 14 > x and y+27 > self.shipimg5.y + 70 > y:
                    self.shipimg5.healthpoints -= 1
                    self.shipimg8.attackpower -= 1


            if self.ship_attackpower == 8 and self.shipimg8.attackpower != 0 and self.shipimg7.healthpoints != 0:
                if x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 14 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 39 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 70 > y or x+27 > self.shipimg7.x + 14 > x and y+27 > self.shipimg7.y + 98 > y:
                    self.shipimg7.healthpoints -= 1
                    self.shipimg8.attackpower -= 1




    def announcewinner(self):
        if self.winner != None:
            while not quitgame():
                gameDisplay.fill(Colors.white)
                if self.winner == 1:
                    Functions.screentext("arial", 50, saved_player1, display_width/2, display_height/3, Colors.green)
                    Functions.screentext("arial", 50, "Congrats!", display_width/2, display_height/2.5, Colors.green)
                    Functions.button("Main Menu", 600, 550, 100, 50, Colors.green, Colors.bright_green, action="play")
                    Functions.button("quit", 700, 550, 100, 50, Colors.red, Colors.bright_red, action="quit")
                if self.winner == 2:
                    Functions.screentext("arial", 100, saved_player2,display_width/2, display_height/2,Colors.green)
                    Functions.screentext("arial", 100, "Congrats!", display_width/2, display_height/1.5, Colors.green)
                    Functions.button("Main Menu", 600, 550, 100, 50, Colors.green, Colors.bright_green, intro)
                    Functions.button("quit", 700, 550, 100, 50, Colors.red, Colors.bright_red, quit)


                pygame.display.update()

def quitgame():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

player = Player()
intro()
pygame.quit()
