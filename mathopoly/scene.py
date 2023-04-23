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
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")

        play_back_button = pygame.image.load(
            "mathopoly/images/playBackButton.png")
        scaled_play_back_button = pygame.transform.scale(
            play_back_button, (40, 40))
        return_button = Button(scaled_play_back_button, pos=(25, 25), text_input="", font=get_font(40),
                               base_color="#d7fcd4", hovering_color="White")

        widget_button = pygame.image.load("mathopoly/images/widgetButton.png")
        scaled_widget_button = pygame.transform.scale(widget_button, (40, 40))
        settings = Button(scaled_widget_button, pos=(1250, 25), text_input="", font=get_font(40),
                          base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(button_rect_image, (150, 40))
        roll_button = Button(scaled_build_button, pos=(600, 200), text_input="Roll", font=get_font(20),
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

#  Change color and appearance when
#  the mouse cursor interacts with them.


def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def roll_and_update():
    for i in range(10):
        dice1_image = random.choice(dice_images)
        dice1_image = pygame.transform.scale(dice1_image, (100,100))
        dice2_image = random.choice(dice_images)
        dice2_image = pygame.transform.scale(dice2_image, (100, 100))
        DISPLAY.blit(dice1_image, (500, 250))
        DISPLAY.blit(dice2_image, (600, 250))
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

    DISPLAY.blit(dice1_image,(500,250))
    DISPLAY.blit(dice2_image,(600,250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

# TO DO
# Properly display on screen
# Add sound effects to rolling animation


def create_players():
    font = pygame.font.SysFont("Comic Sans MS", 24)

    players = []
    player_input = ""
    input_rect = pygame.Rect(400, 200, 440, 50)
    input_active = False

    button_background = pygame.transform.scale(button_rect_image, (300, 80))

    list_rect = pygame.Rect(400, 400, 440, 120)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/simple.jpg")

        play_back_button = pygame.image.load(
            "mathopoly/images/playBackButton.png")
        scaled_play_back_button = pygame.transform.scale(
            play_back_button, (40, 40))
        return_button = Button(scaled_play_back_button, pos=(25, 25), text_input="", font=get_font(40),
                               base_color="#d7fcd4", hovering_color="White")

        widget_button = pygame.image.load("mathopoly/images/widgetButton.png")
        scaled_widget_button = pygame.transform.scale(widget_button, (40, 40))
        settings = Button(scaled_widget_button, pos=(1250, 25), text_input="", font=get_font(40),
                          base_color="#d7fcd4", hovering_color="White")

        return_button.update(DISPLAY)
        settings.update(DISPLAY)
        
        add_Player = Button(button_background, pos=(625, 330), text_input="Add Player",
                            font=get_font(28), base_color="#d7fcd4", hovering_color="White")

        start_Game = Button(button_background, pos=(625, 590), text_input="Start Game",
                            font=get_font(28), base_color="#d7fcd4", hovering_color="White")

        update_button(add_Player, MOUSE_POS)
        update_button(start_Game, MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if input_rect.collidepoint(event.pos):
                    input_active = True
                    pygame.mouse.set_visible(False)

                elif add_Player.rect.collidepoint(MOUSE_POS):
                    if player_input != "" and len(players) < 4:
                        if player_input not in players:
                            players.append(player_input)
                            player_input = ""
                        else:
                            print("Name already exists, choose a different name")

                elif return_button.checkForInput(MOUSE_POS):
                    return
                elif settings.checkForInput(MOUSE_POS):
                    setting_button()

                elif start_Game.rect.collidepoint(MOUSE_POS):
                    if len(players) >= 2:
                        play_button()
                    else:
                        print("Not enough players")

                elif list_rect.collidepoint(event.pos):
                    print(players)

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]

                elif event.key == pygame.K_RETURN:
                    if player_input != "" and len(players) < 4:
                        if player_input not in players:
                            players.append(player_input)
                            player_input = ""
                        else:
                            print("Name already exists, choose a different name")

                else:

                    if len(player_input) < 20:
                        player_input += event.unicode

            elif event.type == pygame.MOUSEBUTTONUP:
                if input_active:
                    pygame.mouse.set_visible(True)
                    input_active = False

        pygame.draw.rect(DISPLAY, pygame.Color("beige"), input_rect)
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), input_rect, 2)
        
        font = get_font(20)
        input_surface = font.render(player_input, True, pygame.Color("black"))
        DISPLAY.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        # Draw the player list box
        pygame.draw.rect(DISPLAY, pygame.Color("beige"), list_rect)
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), list_rect, 2)
        for i, player in enumerate(players):
            player_surface = font.render(player, True, pygame.Color("black"))
            DISPLAY.blit(player_surface, (list_rect.x +
                         5, list_rect.y + 5 + i * 25))

        # Update the display
        pygame.display.flip()

        pygame.display.update()
