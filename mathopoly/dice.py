"""Dice Class"""

import pygame, sys
import random

# initialize pygame
pygame.init()

# set the dimensions of the window
WIDTH = 400
HEIGHT = 200
WINDOW_SIZE = (WIDTH, HEIGHT)

# create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# load the images of the dice faces
dice_faces = [
    pygame.image.load("mathopoly/images/die1.png"),
    pygame.image.load("mathopoly/images/die2.png"),
    pygame.image.load("mathopoly/images/die3.png"),
    pygame.image.load("mathopoly/images/die4.png"),
    pygame.image.load("mathopoly/images/die5.png"),
    pygame.image.load("mathopoly/images/die6.png")
]

# define the size and position of the dice
DICE_SIZE = 100
DICE_MARGIN = 50
DICE_POS_1 = (DICE_MARGIN, HEIGHT/2 - DICE_SIZE/2)
DICE_POS_2 = (WIDTH - DICE_SIZE - DICE_MARGIN, HEIGHT/2 - DICE_SIZE/2)

# set the initial values for the dice
dice_value_1 = 1
dice_value_2 = 1

# function to roll the dice and update their values
def roll_dice():
    global dice_value_1, dice_value_2
    dice_value_1 = random.randint(1, 6)
    dice_value_2 = random.randint(1, 6)

# draw the dice on the screen
def draw_dice():
    # clear the screen
    screen.fill((255, 255, 255))

    # draw the first dice
    screen.blit(dice_faces[dice_value_1-1], DICE_POS_1)

    # draw the second dice
    screen.blit(dice_faces[dice_value_2-1], DICE_POS_2)

    # update the screen
    pygame.display.flip()

# roll the dice initially
roll_dice()

# loop to handle events and draw the dice
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll_dice()

    draw_dice()

# quit pygame
pygame.quit()