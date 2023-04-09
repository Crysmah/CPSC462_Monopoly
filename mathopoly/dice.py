import pygame
import random

# initialize Pygame
pygame.init()

# set the window size
WINDOW_SIZE = (400, 400)

# create the Pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)

# set the Pygame window title
pygame.display.set_caption("Dice Roller")

# load the dice images
dice_images = []
for i in range(1, 7):
    dice_images.append(pygame.image.load(f"images/die_{i}.png"))

# set the font for the roll button
font = pygame.font.SysFont(None, 30)

# create the roll button
roll_button = pygame.Rect(150, 300, 100, 50)

# initialize the dice values
die1_value = 1
die2_value = 1

# initialize the total value
total_value = 0

# initialize the roll button state
button_down = False

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                button_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if roll_button.collidepoint(event.pos):
                button_down = False
                # roll the dice
                die1_value = random.randint(1, 6)
                die2_value = random.randint(1, 6)
                total_value = die1_value + die2_value

    # fill the background color
    screen.fill((255, 255, 255))

    # draw the dice
    screen.blit(dice_images[die1_value - 1], (50, 90))
    screen.blit(dice_images[die2_value - 1], (200, 90))

    # draw the roll button
    color = (200, 200, 200)
    if button_down:
        color = (150, 150, 150)
    pygame.draw.rect(screen, color, roll_button)
    text = font.render("Roll", True, (0, 0, 0))
    text_rect = text.get_rect(center=roll_button.center)
    screen.blit(text, text_rect)

    # draw the total
    total_text = font.render(f"Total: {total_value}", True, (0, 0, 0))
    screen.blit(total_text, (160, 250))

    # update the display
    pygame.display.update()
    print(f"Total: {total_value}")


# quit Pygame
pygame.quit()
