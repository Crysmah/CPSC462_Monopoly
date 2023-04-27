import pygame
import sys
from mathopoly.button import Button
import random
import time


# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Game Variables
total_value = 0
player1 = {'name': 'Alice', 'balance': 1500}
properties = {
    0: {'name': 'Go', 'type': 'corner'},
    1: {'name': 'Mediterranean Avenue', 'color': 'brown', 'price': 60, 'owner': 'Empty'},
    2: {'name': 'Community Chest', 'type': 'chest'},
    3: {'name': 'Baltic Avenue', 'color': 'brown', 'price': 60, 'owner': 'Empty'},
    4: {'name': 'Income Tax', 'type': 'tax', 'price': 200, 'owner': 'Empty'},
}

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
            pygame.mixer.music.load("mathopoly/music/vibes.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0.0, 500)
        except pygame.error as pygame_error:
            print(f'Cannot open {"vibes.mp3"}')
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

        return_button = clickable_image_buttons(
            "mathopoly/images/playBackButton.png", (25, 25), 40, 40)
        settings = clickable_image_buttons(
            "mathopoly/images/widgetButton.png", (1250, 25), 40, 40)

        scaled_build_button = pygame.transform.scale(
            button_rect_image, (150, 40))
        roll_button = Button(scaled_build_button, pos=(500, 200), text_input="Roll", font=get_font(20),
                             base_color="#d7fcd4", hovering_color="White")

        scaled_buy_button = pygame.transform.scale(
            button_rect_image, (150, 40))
        buy_button = Button(scaled_buy_button, pos=(700, 200), text_input="Buy", font=get_font(20),
                            base_color="#d7fcd4", hovering_color="White")

        buy_button.update(DISPLAY)
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
                if buy_button.checkForInput(PLAY_MOUSE_POS):
                    buy_event()

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
            f"Volume: {int(round(volume * 100, -1))}%", True, (255, 255, 255))
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
        dice1_image = pygame.transform.scale(dice1_image, (100, 100))
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
    dice1_image = pygame.transform.scale(dice1_image, (100, 100))

    dice2_image = dice_images[roll2-1]
    dice2_image = pygame.transform.scale(dice2_image, (100, 100))

    DISPLAY.blit(dice1_image, (500, 250))
    DISPLAY.blit(dice2_image, (600, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return


def create_button(pos, text_input, font, base_color, hovering_color):
    scaled_button_image = pygame.transform.scale(button_rect_image, (300, 80))
    return Button(scaled_button_image, pos=pos, text_input=text_input, font=get_font(font),
                  base_color=base_color, hovering_color=hovering_color)

# Function to draw text on the screen


def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Function to create the image based buttons


def clickable_image_buttons(image_path, position, width, height):
    button_image = pygame.image.load(image_path)
    scaled_button_image = pygame.transform.scale(button_image, (width, height))
    button = Button(scaled_button_image, pos=position, text_input="", font=get_font(40),
                    base_color="#d7fcd4", hovering_color="White")
    return button


def create_players():
    font = pygame.font.SysFont("Comic Sans MS", 24)

    players = []
    player_input = ""
    input_rect = pygame.Rect(200, 200, 440, 50)
    input_active = False

    button_background = pygame.transform.scale(button_rect_image, (300, 80))

    list_rect = pygame.Rect(200, 400, 400, 120)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/back.png")

        return_button = clickable_image_buttons(
            "mathopoly/images/playBackButton.png", (25, 25), 40, 40)
        settings = clickable_image_buttons(
            "mathopoly/images/widgetButton.png", (1250, 25), 40, 40)

        return_button.update(DISPLAY)
        settings.update(DISPLAY)

        add_Player = create_button(
            (420, 330), "Add Player", 28, "#d7fcd4", "White")
        start_Game = create_button(
            (420, 590), "Start Game", 28, "#d7fcd4", "White")

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

        draw_text(player_input, font, pygame.Color("black"),
                  DISPLAY, input_rect.x + 5, input_rect.y + 5)
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), input_rect, 2)

        # Draw the player list box
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), list_rect, 2)
        for i, player in enumerate(players):
            draw_text(player, font, pygame.Color("black"), DISPLAY,
                      list_rect.x + 5, list_rect.y + 5 + i * 25)
            pygame.draw.rect(DISPLAY, pygame.Color("gray"), list_rect, 2)

        # Update the display
        pygame.display.flip()

        pygame.display.update()


def buy_property(player, tile_number, properties):
    message = ""
    if 'price' not in properties[tile_number]:
        message = f"{properties[tile_number]['name']} square cannot be bought"
    elif properties[tile_number]['owner'] != 'Empty':
        message = f"{player['name']} owns this property"
    elif properties[tile_number]['owner'] == 'Empty' and player['balance'] >= properties[tile_number]['price']:
        player['balance'] -= properties[tile_number]['price']
        properties[tile_number]['owner'] = player['name']
        message = f"{player['name']} bought {properties[tile_number]['name']} for {properties[tile_number]['price']}."
    print(message)
    return message


def display_message(message):
    # Clear the screen
    DISPLAY.fill(WHITE)
    draw_background("mathopoly/images/playBackground.png")

    # Calculate the width of the message
    font = get_font(20)
    message_width = font.size(message)[0]

    # Create a message box
    message_box_width = message_width + 20
    message_box = pygame.Rect(
        (1280 - message_box_width) / 2, (720 - 100) / 2, message_box_width, 100)
    pygame.draw.rect(DISPLAY, BLACK, message_box, 2)

    # Display the message
    message_text = font.render(message, True, BLACK)
    message_rect = message_text.get_rect(center=message_box.center)
    DISPLAY.blit(message_text, message_rect)

    # Update the Pygame window
    pygame.display.update()


def buy_event():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")

        yes_button = clickable_image_buttons(
            "mathopoly/images/Yes.png", (500, 200), 80, 80)
        no_button = clickable_image_buttons(
            "mathopoly/images/No.png", (700, 200), 80, 80)

        yes_button.update(DISPLAY)
        no_button.update(DISPLAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.checkForInput(MOUSE_POS):
                    message = buy_property(player1, 1, properties)
                    display_message(message)
                    pygame.time.delay(1800)
                    return

                elif no_button.checkForInput(MOUSE_POS):
                    return

        pygame.display.update()
