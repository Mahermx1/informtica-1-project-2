import pygame, time, Colors, Images


display_width = 800
display_height = 600
ship_width = 130
gameDisplay = pygame.display.set_mode((display_width,display_height))

def ship(x,y):
    gameDisplay.blit(Images.shipImg,(x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def screentext(font,size, word, x, y, color):
    Text = pygame.font.SysFont(font,size)
    textSurf, textRect = text_objects(word, Text, color)
    textRect.center = (x), (y)
    gameDisplay.blit(textSurf, textRect)

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
        textSurf, textRect = text_objects(msg,smallText, Colors.black)
        textRect.center = ( (x + (w / 2)), y +(h / 2) )
        gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg, color, x, y):
    screen_text = pygame.font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x- x/2, y- y/2])


