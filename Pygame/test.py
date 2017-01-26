import pygame

pygame.init()

gameDisplay = [800, 600]
screen = pygame.display.set_mode(gameDisplay)
pygame.display.set_caption("Array Backed Grid")


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen.fill(black)

# This sets the grid_width and grid_height of each grid location
grid_width = 30
grid_height = 30
# This sets the grid_margin between each cell
grid_margin = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(18):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(18):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1
 

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (grid_width + grid_margin)
            row = pos[1] // (grid_height + grid_margin)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    for row in range(18):
        for column in range(18):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(screen,
                             color,
                             [(grid_margin + grid_width) * column + grid_margin,
                              (grid_margin + grid_height) * row + grid_margin,
                              grid_width,
                              grid_height])

    clock.tick(60)
    pygame.display.flip()


pygame.quit()

