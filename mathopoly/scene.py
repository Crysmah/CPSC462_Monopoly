import pygame
import sys
from mathopoly.button import Button
import random
import time

total_value = 0

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")
background_image = pygame.image.load("mathopoly/images/background.PNG")
button_rect_image = image = pygame.image.load(
    "mathopoly/images/Button Rect.png")

dice_images = [pygame.image.load('mathopoly/images/dice_one.png'), pygame.image.load('mathopoly/images/dice_two.png'), pygame.image.load('mathopoly/images/dice_three.png'),
               pygame.image.load('mathopoly/images/dice_four.png'), pygame.image.load('mathopoly/images/dice_five.png'), pygame.image.load('mathopoly/images/dice_six.png')]

# Board coordinates 
# board =  [
#     (145, 13), (145, 153), (145, 293), (145, 433), (145, 573),
#     (285, 13), (425, 13), (565, 13), (705, 13), (845, 13), (985, 13),
#     (985, 153), (985, 293), (985, 433), (985, 573),
#     (285, 573), (425, 573), (565, 573), (705, 573), (845, 573)
# ]
# Square size
size = 140

new_board = [
    # Top
    (190, 35), (400, 35), (600, 35), (790, 35), (990, 35),
    # Left
    (190, 170), (190, 315), (190, 460),
    # Right
    (990, 170), (990, 315), (990, 460),
    # Bottom
    (190, 590), (400, 590), (600, 590), (790, 590), (990, 590)
]

board = {
    # START to top right
    0 : (190, 35),
    1 : (400, 35), 
    2 : (600, 35), 
    3 : (790, 35), 
    4 : (990, 35),

    # Right top to bottom right
    5 : (990, 170),
    6 : (990, 315),
    7 : (990, 460),

    # Bottom right to bottom left
    8 : (990, 590),
    9 : (790, 590),
    10 : (600, 590),
    11 : (400, 590),
    12 : (190, 590),

    # Bottom left to START
    13 : (190, 460),
    14 : (190, 315),
    15 : (190, 170)
}

playerMove = 0

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("mathopoly/images/font.ttf", size)

# plays music


def start():
    """Starts the music"""
    if True:
        try:
            pygame.mixer.music.load("mathopoly/music/Late-at-Night.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0.0, 500)
        except pygame.error as pygame_error:
            print(f'Cannot open {"FirstSteps.mp3"}')
            raise SystemExit(1) from pygame_error

# Draw the background for the Menu Screen
# update this function


def draw_background(image):
    background_image = pygame.image.load(image)
    ''' Re-size the background image'''
    background = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    DISPLAY.blit(background, (0, 0))

# Access to the game


def play_button():
    global playerMove, total_value
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")
        play_back_button = pygame.image.load("mathopoly/images/playBackButton.png")
        draw_board()
        scaled_play_back_button = pygame.transform.scale(play_back_button, (40, 40))
        return_button = Button(scaled_play_back_button, pos=(25, 25), text_input="", font=get_font(40),
                               base_color="#d7fcd4", hovering_color="White")

        widget_button = pygame.image.load("mathopoly/images/widgetButton.png")
        scaled_widget_button = pygame.transform.scale(widget_button, (40, 40))
        settings = Button(scaled_widget_button, pos=(1250, 25), text_input="", font=get_font(40),
                          base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(button_rect_image, (150, 40))
        roll_button = Button(scaled_build_button, pos=(640, 280), text_input="Roll", font=get_font(20),
                              base_color="#d7fcd4", hovering_color="White")

        roll_button.update(DISPLAY)
        return_button.update(DISPLAY)
        settings.update(DISPLAY)
        #DISPLAY.blit(scaled_play_back_button, (10,10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.checkForInput(PLAY_MOUSE_POS):
                    return
                if settings.checkForInput(PLAY_MOUSE_POS):
                    setting_button()
                if roll_button.checkForInput(PLAY_MOUSE_POS):
                    roll_and_update()
                    playerMove += total_value
        if playerMove >= 16:
            playerMove -= 16
        print(playerMove)
        draw_piece('mathopoly/images/dog.png', playerMove)
        pygame.display.update()

# Changing the music and sound


def setting_button():
    # initialize volume current volume
    volume = pygame.mixer.music.get_volume()
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        draw_background("mathopoly/images/playBackground.png")

        button_rect = pygame.transform.scale(button_rect_image, (300, 80))
        VOLUME_LABEL = get_font(40).render(
            f"Volume: {int(volume * 100)}%", True, (255, 255, 255))
        UP_BUTTON = Button(button_rect, pos=(640, 300), text_input="UP",
                           font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        DOWN_BUTTON = Button(button_rect, pos=(640, 450), text_input="DOWN",
                             font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(button_rect, pos=(640, 600), text_input="BACK",
                             font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        update_button(UP_BUTTON, MENU_MOUSE_POS)
        update_button(DOWN_BUTTON, MENU_MOUSE_POS)
        update_button(BACK_BUTTON, MENU_MOUSE_POS)

        DISPLAY.blit(VOLUME_LABEL, (640 - VOLUME_LABEL.get_width() // 2, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if UP_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    volume = min(volume + 0.1, 1.0)
                    pygame.mixer.music.set_volume(volume)
                elif DOWN_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    volume = max(volume - 0.1, 0.0)
                    pygame.mixer.music.set_volume(volume)
                elif BACK_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                    return  # exit the function

        pygame.display.update()


# Close the application
# thinking about it
def quit_button():
    pygame.quit()
    sys.exit()

# Change color and appearance when
# the mouse cursor interacts with them.
def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def roll_and_update():
    global total_value
    draw_piece('mathopoly/images/dog.png', playerMove)
    for i in range(10):
        dice1_image = random.choice(dice_images)
        dice1_image = pygame.transform.scale(dice1_image, (100,100))
        dice2_image = random.choice(dice_images)
        dice2_image = pygame.transform.scale(dice2_image, (100, 100))
        DISPLAY.blit(dice1_image, (540, 310))
        DISPLAY.blit(dice2_image, (640, 310))
        pygame.display.update()
        time.sleep(0.1)


    roll1 = roll_dice()
    roll2 = roll_dice()

    total_value = roll1 + roll2
    print(f"Total: {total_value}")

    dice1_image = dice_images[roll1-1]
    dice1_image = pygame.transform.scale(dice1_image, (100,100))

    dice2_image = dice_images[roll2-1]
    dice2_image = pygame.transform.scale(dice2_image,(100,100))

    DISPLAY.blit(dice1_image,(540,310))
    DISPLAY.blit(dice2_image,(640,310))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 

def draw_board():
    background_image = pygame.image.load('mathopoly/images/board.PNG')
    background_image = pygame.transform.scale(background_image, (1000, 700))
    background_image.set_colorkey((255,255,255))
    DISPLAY.blit(background_image, (145, 13))
    # for i in range(20):
    #     pygame.draw.rect(DISPLAY, (120,120,120) , [board[i][0], board[i][1], size, size], 1)

def draw_piece(image, move):
    dog_piece = pygame.image.load(image)
    dog_piece = pygame.transform.scale(dog_piece, (100, 100))
    # DISPLAY.blit(dog_piece, (190+210, 35))
    DISPLAY.blit(dog_piece, board[move])
# TO DO
# Properly display on screen
# Add sound effects to rolling animation
