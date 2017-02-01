def Player1_wins():
    win = True

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Player 1 wins!", green, -100, size="Large")
        message_to_screen("Congrats!!!", black, -30)

        button("play again", 150, 500, 150, 500, green, bright_green, action="play")
        button("quit", 150, 500, 150, 500, red, bright_red, action="quit")

        pygame.display.update()

        clock.tick(15)


Player1_wins()


def Player2_wins():
    win = True

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Player 2 wins!", green, -100, size="Large")
        message_to_screen("Congrats!!!", black, -30)

        button("play again", 150, 500, 150, 500, green, bright_green, action="play")
        button("quit", 150, 500, 150, 500, red, bright_red, action="quit")

        pygame.display.update()

        clock.tick(15)


Player2_wins()

if Player1_boats < 1:
    Player2_wins()
elif Player2_boats < 1:
    Plater1_wins()