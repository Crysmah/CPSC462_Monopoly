import pygame, sys
from mathopoly.button import Button
import random
import time

# Waiting to disappear dice
wait = 0

dice_1 = 0

pygame.init()

# WIDTH, HEIGHT = 1280, 720
WIDTH, HEIGHT = 1400 , 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")
background_image = pygame.image.load("mathopoly/images/background.PNG")
button_rect_image = image=pygame.image.load("mathopoly/images/Button Rect.png")

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

def get_font(size): # Returns Press-Start-2P in the desired size
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
## update this function
def draw_background(image):
    background_image = pygame.image.load(image)
    ''' Re-size the background image'''
    background = pygame.transform.scale(background_image,(WIDTH, HEIGHT))
    DISPLAY.blit(background, (0,0))

# Access to the game
def play_button():
    global playerMove
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
        settings = Button(scaled_widget_button, pos=(1375, 25), text_input="", font=get_font(40),
                        base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(button_rect_image, (150, 40))
        roll_button = Button(scaled_build_button, pos=(640, 280), text_input="Roll", font=get_font(20),
                              base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(button_rect_image, (150, 40))
        build_button = Button(scaled_build_button, pos=(400, 200), text_input="BUILD", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="White")
        
        scaled_sell_button = pygame.transform.scale(button_rect_image, (150, 40))
        sell_button = Button(scaled_sell_button, pos=(800, 200), text_input="SELL", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="White")
        
        scaled_end_turn_button = pygame.transform.scale(button_rect_image, (190, 50))
        end_turn_button = Button(scaled_end_turn_button, pos=(600, 250), text_input="END TURN", font=get_font(20),
                        base_color="#d7fcd4", hovering_color="White")
        
        
        return_button.update(DISPLAY)
        build_button.update(DISPLAY)
        sell_button.update(DISPLAY)
        end_turn_button.update(DISPLAY)

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
                    # playerMove += dice_1
                    playerMove += dice_1
        if playerMove >= 16:
            playerMove -= 16
        # print(playerMove)
        draw_piece('mathopoly/images/dog.png', playerMove)
        show_dice()
        pygame.display.update()

# Changing the music and sound
def setting_button():
    volume = 0.1 # initialize volume to a default value
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        draw_background("mathopoly/images/playBackground.png")

        button_rect = pygame.transform.scale(button_rect_image, (300, 80))
        VOLUME_LABEL = get_font(40).render(f"Volume: {int(volume * 100)}%", True, (255, 255, 255))
        UP_BUTTON = Button(button_rect, pos=(640 + 60, 300), text_input="UP",
                           font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        DOWN_BUTTON = Button(button_rect, pos=(640 + 60, 450), text_input="DOWN",
                             font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(button_rect, pos=(640 + 60, 600), text_input="BACK",
                             font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        update_button(UP_BUTTON, MENU_MOUSE_POS)
        update_button(DOWN_BUTTON, MENU_MOUSE_POS)
        update_button(BACK_BUTTON, MENU_MOUSE_POS)

        # DISPLAY.blit(VOLUME_LABEL, (640 - VOLUME_LABEL.get_width() // 2, 150))
        DISPLAY.blit(VOLUME_LABEL, (500, 150))
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
                    return # exit the function

        pygame.display.update()


# Close the application
## thinking about it
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
    global dice_1
    for i in range(10):
        dice1_image = random.choice(dice_images)
        dice1_image = pygame.transform.scale(dice1_image, (100, 100))
        DISPLAY.blit(dice1_image, (590, 320))
        pygame.display.update()
        time.sleep(0.1)

    roll1 = roll_dice()

    dice_1 = roll1

    print(f"Total: {dice_1}")


def show_dice():
    dice1_image = dice_images[dice_1-1]
    dice1_image = pygame.transform.scale(dice1_image, (100, 100))

    DISPLAY.blit(dice1_image, (590, 320))
    
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
    if playerMove >= 4 and playerMove <= 11:
        print("")
    else:
        dog_piece = pygame.transform.flip(dog_piece, True, False)

    DISPLAY.blit(dog_piece, board[move])
# TO DO
# Properly display on screen
# Add sound effects to rolling animation
def create_players():
    font = pygame.font.SysFont("Comic Sans MS", 24)

    players = []
    player_input = ""
    # input_rect = pygame.Rect(400, 200, 440, 50)
    input_rect = pygame.Rect(483, 200, 440, 50)
    input_active = False

    button_background = pygame.transform.scale(button_rect_image, (300, 80))

    list_rect = pygame.Rect(483, 400, 440, 120)

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
        settings = Button(scaled_widget_button, pos=(1375, 25), text_input="", font=get_font(40),
                          base_color="#d7fcd4", hovering_color="White")

        return_button.update(DISPLAY)
        settings.update(DISPLAY)
        
        add_Player = Button(button_background, pos=(700, 330), text_input="Add Player",
                            font=get_font(28), base_color="#d7fcd4", hovering_color="White")

        start_Game = Button(button_background, pos=(700, 590), text_input="Start Game",
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
        # DISPLAY.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
        DISPLAY.blit(input_surface, (input_rect.x + 5, input_rect.y + 15))
        # Draw the player list box
        pygame.draw.rect(DISPLAY, pygame.Color("beige"), list_rect)
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), list_rect, 2)
        for i, player in enumerate(players):
            player_surface = font.render(player, True, pygame.Color("black"))
            DISPLAY.blit(player_surface, (list_rect.x +
                         5, list_rect.y + 15 + i * 25))

        # Update the display
        pygame.display.flip()

        pygame.display.update()