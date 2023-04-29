import pygame
pygame.init()

# Set up the screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monopoly 5x5")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define font
font = pygame.font.SysFont('Arial', 25)

# Define tile positions
tile_positions = [
    (120, 20), (120, 140), (120, 260), (120, 380), (120, 500),
    (260, 740), (380, 740), (500, 740), (620, 740), (740, 740),
    (740, 620), (740, 500), (740, 380), (740, 260), (740, 140), (740, 20),
    (600, 20), (600, 140), (600, 260), (600, 380), (600, 500)
]

leftAdjusted = 145
size = 140
start = 13

top_row_start = leftAdjusted + size
left_column = [(leftAdjusted, start), (leftAdjusted, start + size), (leftAdjusted, start + size * 2), (leftAdjusted, start + size * 3), (leftAdjusted, start + size * 4)]
top_row = [(top_row_start, start), (top_row_start + size, start), (top_row_start + size * 2, start), (top_row_start + size * 3, start), (top_row_start + size * 4, start), (top_row_start + size * 5, start)]
right_column = [(top_row_start + size * 5, start + size), (top_row_start + size * 5, start + size * 2), (top_row_start + size * 5, start + size * 3), (top_row_start + size * 5, start + size * 4)]
bottom_row = [(leftAdjusted + size, start + size * 4), (leftAdjusted + size * 2, start + size * 4), (leftAdjusted + size * 3, start + size * 4), (leftAdjusted + size * 4, start + size * 4), (leftAdjusted + size * 5, start + size * 4)]
# Define function to draw the board
def draw_board():
    screen.fill(WHITE)
    for i in range(5):
        pygame.draw.rect(screen, RED, [left_column[i][0], left_column[i][1], size, size], 1)
    for i in range(6):
        pygame.draw.rect(screen, RED, [top_row[i][0], top_row[i][1], size, size], 1)
    for i in range(4):
        pygame.draw.rect(screen, RED, [right_column[i][0], right_column[i][1], size, size], 1)
    for i in range(5):
        pygame.draw.rect(screen, RED, [bottom_row[i][0], bottom_row[i][1], size, size], 1)
    # for i in range(5):
    #     pygame.draw.rect(screen, RED, [tile_positions[i][0], tile_positions[i][1], 120, 120], 2)
    # for i in range(6, 11):
    #     pygame.draw.rect(screen, RED, [tile_positions[i][0], tile_positions[i][1], 120, 120], 2)
    # for i in range(12, 17):
    #     pygame.draw.rect(screen, RED, [tile_positions[i][0], tile_positions[i][1], 120, 120], 2)
    # for i in range(18, 21):
    #     pygame.draw.rect(screen, RED, [tile_positions[i][0], tile_positions[i][1], 120, 120], 2)
    pygame.display.update()

# Set up game loop
draw_board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame properly
pygame.quit()