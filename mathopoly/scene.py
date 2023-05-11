import pygame, sys
from mathopoly.button import Button
import random
import time
from pygame.locals import *

dice_1 = 0

count = 0

roll = True

load_dice_image = 0

game_over = 0

winning_player = ''

players = []

pygame.init()

# WIDTH, HEIGHT = 1280, 720
WIDTH, HEIGHT = 1400, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")
background_image = pygame.image.load("mathopoly/images/background.PNG")
button_rect_image = image=pygame.image.load("mathopoly/images/Button Rect.png")

dice_images = [pygame.image.load('mathopoly/images/dice_one.png'), pygame.image.load('mathopoly/images/dice_two.png'), pygame.image.load('mathopoly/images/dice_three.png'),
               pygame.image.load('mathopoly/images/dice_four.png'), pygame.image.load('mathopoly/images/dice_five.png'), pygame.image.load('mathopoly/images/dice_six.png')]

win_image = pygame.image.load('mathopoly/images/win.png').convert_alpha()
win_image = pygame.transform.scale(win_image, (250, 250))

WHITE = ((255, 255, 255))
BLACK = ((0, 0, 0))

dog_piece = pygame.image.load('mathopoly/images/dog.png')
dog_piece = pygame.transform.scale(dog_piece, (100, 100))

plus = pygame.image.load('mathopoly/images/plus.png')
plus = pygame.transform.scale(plus, (100, 100))
plus.set_colorkey((255, 255, 255))

minus = pygame.image.load('mathopoly/images/minus.png')
minus = pygame.transform.scale(minus, (100, 50))
minus.set_colorkey((255, 255, 255))

player1 = {'name': 'Alice', 'balance': 1500,'property': 0, 'position': 0, 'piece': plus}
player2 = {'name': 'Lux', 'balance': 1500, 'property': 0, 'position': 0, 'piece': minus}
# player3 = {'name': 'Joe', 'balance': 1500, 'position': 0, 'piece': dog_piece}
# player4 = {'name': 'Mama', 'balance': 1500, 'position': 0, 'piece': dog_piece}


player_list = []
player_list.append(player1)
player_list.append(player2)
# player_list.append(player3)
# player_list.append(player4)

size = 140

board = {
    # START to top right
    0: (190, 35),
    1: (400, 35),
    2: (600, 35),
    3: (790, 35),
    4: (990, 35),

    # Right top to bottom right
    5: (990, 170),
    6: (990, 315),
    7: (990, 460),

    # Bottom right to bottom left
    8: (990, 590),
    9: (790, 590),
    10: (600, 590),
    11: (400, 590),
    12: (190, 590),

    # Bottom left to START
    13: (190, 460),
    14: (190, 315),
    15: (190, 170)
}

properties = {
    0: {'pos': (155, 35),  'name': 'Go!!',           'owner': ''},
    1: {'pos': (360, 35),  'name': 'Carl\'s Jr',     'owner': '', 'price': 100},
    2: {'pos': (560, 35),  'name': 'Bookstore',      'owner': '', 'price': 150},
    3: {'pos': (760, 35),  'name': 'Titan House',    'owner': '', 'price': 200},
    4: {'pos': (950, 35),  'name': 'Visit to Jail',  'owner': ''},
    5: {'pos': (950, 170), 'name': 'ECS Building',   'owner': '', 'price': 200},
    6: {'pos': (950, 315), 'name': 'Visual Art',     'owner': '', 'price': 150},
    7: {'pos': (950, 460), 'name': 'Gymnasium',      'owner': '', 'price': 100},
    8: {'pos': (950, 590), 'name': 'Free Parking',   'owner': ''},
    9: {'pos': (760, 590), 'name': 'Game Store',    'owner': '', 'price': 200},
    10: {'pos': (555, 590), 'name': 'Titan Stadium',  'owner': '', 'price': 300},
    11: {'pos': (360, 590), 'name': 'Titan Union',    'owner': '', 'price': 300},
    12: {'pos': (155, 590), 'name': 'Visit to Jail',  'owner': ''},
    13: {'pos': (150, 460), 'name': 'Pollak Library', 'owner': '', 'price': 100},
    14: {'pos': (155, 315), 'name': 'Electric Co',    'owner': '', 'price': 150},
    15: {'pos': (155, 170), 'name': 'Mihaylo Hall',   'owner': '', 'price': 200}
}

playerMove = 0

x = 0
y = 0
userInput = ''
solveMath = False
rightOrWrong = False

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

# stops the music
def stop():
    """Stops the music"""
    pygame.mixer.fadeout(500)
    pygame.mixer.music.stop()


# end screen music
def end_music():
    """ending music"""
    if True:
        try:
            pygame.mixer.music.load("mathopoly/music/TheWickedWild.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0.0, 500)
        except pygame.error as pygame_error:
            print(f'Cannot open {"TheWickedWild.mp3"}')
            raise SystemExit(1) from pygame_error

# Draw the background for the Menu Screen
# update this function
def draw_background(image):
    background_image = pygame.image.load(image)
    ''' Re-size the background image'''
    background = pygame.transform.scale(background_image,(WIDTH, HEIGHT))
    DISPLAY.blit(background, (0,0))

# Access to the game
def play_button():
    global playerMove, count, plus, minus, roll, x, y, userInput, solveMath, game_over, players
    font = get_font(20)
    p = 0
    for i in players:
        player_list[p]['name'] = i
        p += 1
    print(player_list)

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")
        play_back_button = pygame.image.load(
            "mathopoly/images/playBackButton.png")
        draw_board()
        text_properties()

        # draw_stats(player_list)
        properties_owned(player_list)

        #Create the output box for players' info
        player_info = pygame.Rect(1150, 14, 230, 225)
        pygame.draw.rect(DISPLAY, pygame.Color("beige"), player_info)
        pygame.draw.rect(DISPLAY, pygame.Color("gray"), player_info, 2)
        #Display player_info
        for i, player in enumerate(player_list):
            player_name_surface = font.render(player['name'], True, pygame.Color("black"))
            DISPLAY.blit(player_name_surface, (player_info.x +
                                               5, player_info.y + 15 + i * 50))

            player_balance_surface = font.render(str(player['balance']),
                                                 True, pygame.Color("black"))
            DISPLAY.blit(player_balance_surface, (player_info.x +
                                                  130, player_info.y + 15 + i * 50))


        scaled_play_back_button = pygame.transform.scale(
            play_back_button, (40, 40))
        return_button = Button(scaled_play_back_button, pos=(25, 25), text_input="", font=get_font(40),
                            base_color="#d7fcd4", hovering_color="White")

        # widget button
        widget_button = pygame.image.load("mathopoly/images/widgetButton.png")
        scaled_widget_button = pygame.transform.scale(widget_button, (40, 40))
        settings = Button(scaled_widget_button, pos=(1375, 25), text_input="", font=get_font(40),
                          base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(
            button_rect_image, (150, 40))
        roll_button = Button(scaled_build_button, pos=(640, 280), text_input="Roll", font=get_font(20),
                             base_color="#d7fcd4", hovering_color="White")

        scaled_build_button = pygame.transform.scale(
            button_rect_image, (150, 40))
        build_button = Button(scaled_build_button, pos=(400, 200), text_input="BUILD", font=get_font(20),
                              base_color="#d7fcd4", hovering_color="White")

        scaled_sell_button = pygame.transform.scale(
            button_rect_image, (150, 40))
        sell_button = Button(scaled_sell_button, pos=(800, 200), text_input="SELL", font=get_font(20),
                             base_color="#d7fcd4", hovering_color="White")

        scaled_end_turn_button = pygame.transform.scale(
            button_rect_image, (190, 50))
        end_turn_button = Button(scaled_end_turn_button, pos=(640, 470), text_input="END TURN", font=get_font(20),
                                 base_color="#d7fcd4", hovering_color="White")

        scaled_end_turn_button = pygame.transform.scale(
            button_rect_image, (190, 50))
        buy_button = Button(scaled_end_turn_button, pos=(820, 370), text_input="Buy", font=get_font(20),
                            base_color="#d7fcd4", hovering_color="White")

        scaled_end_turn_button = pygame.transform.scale(
            button_rect_image, (190, 50))
        restart = Button(scaled_end_turn_button, pos=(1300, 690), text_input="Restart", font=get_font(20),
                         base_color="#d7fcd4", hovering_color="White")

        buy_button.update(DISPLAY)
        return_button.update(DISPLAY)
        end_turn_button.update(DISPLAY)
        roll_button.update(DISPLAY)
        return_button.update(DISPLAY)
        settings.update(DISPLAY)
        restart.update(DISPLAY)
        #DISPLAY.blit(scaled_play_back_button, (10,10))

        if count >= len(player_list):
            count = 0

        '''Check everything in here'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.checkForInput(PLAY_MOUSE_POS):
                    return
                if settings.checkForInput(PLAY_MOUSE_POS):
                    setting_button()
                if game_over == 0:
                    if roll:  # If true, you can click the roll button
                        if roll_button.checkForInput(PLAY_MOUSE_POS):
                            roll_and_update()
                            roll = False
                            solveMath = True
                            x = random.randint(1, 10)
                            y = random.randint(1, 10)
                            num = random.randint(1,3)
                    else:  # Else, you can click the buy and end turn buttons
                        if buy_button.checkForInput(PLAY_MOUSE_POS) and solveMath == False and rightOrWrong == True:
                            buy_event()
                            gameStatus(player_list, properties)
                        if end_turn_button.checkForInput(PLAY_MOUSE_POS) and solveMath == False:
                            end_turn_message(player_list[count])
                            count += 1
                            roll = True
                else:
                    if restart.checkForInput(PLAY_MOUSE_POS):
                        for prop in properties.values():
                            prop['owner'] = ''

                        for player in player_list:
                            player['position'] = 0
                            player['balance'] = 1500

                        game_over = 0
                        count = 0
                        playerMove = 0
                        roll = True
                        stop()
                        start()

                        # Takes key inputs when a problem is present
            if solveMath == True and event.type == KEYDOWN:
                if event.unicode.isnumeric():
                    userInput += event.unicode
                elif event.key == K_BACKSPACE:
                    userInput = userInput[:-1]
                elif event.key == K_RETURN:

                    if ((num == 1) and (x + y == int(userInput))) or ((num == 2) and (x - y == int(userInput)) or (y - x == int(userInput))) or ((num == 3) and (x * y == int(userInput))) :
                        print('Correct')
                        rightOrWrong = True
                        # creating the message box
                        correct_font = get_font(100)
                        rendered_correct = correct_font.render("Correct", True, BLACK)
                        # the position for the message
                        correct_position = rendered_correct.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                        # loads the correct message
                        DISPLAY.blit(rendered_correct, correct_position)
                        pygame.display.update()
                        pygame.time.delay(1800)

                    else:
                        print('Wrong')
                        rightOrWrong = False
                        # creating the message box
                        wrong_font = get_font(100)
                        rendered_wrong = wrong_font.render("Wrong", True, BLACK)
                        # the position for the message
                        wrong_position = rendered_wrong.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                        # loads the correct message
                        DISPLAY.blit(rendered_wrong, wrong_position)
                        pygame.display.update()
                        pygame.time.delay(1800)

                    userInput = ''
                    solveMath = False

        # Displays only when the roll button is pressed
        if solveMath == True:
            if (num == 1):
                mathProblem = get_font(40).render(
                    "{0}+{1}".format(x, y), True, (0, 0, 0))
                block = get_font(40).render(userInput, True, (0, 0, 0))
            elif (num == 2):
                if (y > x):
                    mathProblem = get_font(40).render(
                        "{0}-{1}".format(y, x), True, (0, 0, 0))
                    block = get_font(40).render(userInput, True, (0, 0, 0))
                else:
                    mathProblem = get_font(40).render(
                        "{0}-{1}".format(x, y), True, (0, 0, 0))
                    block = get_font(40).render(userInput, True, (0, 0, 0))
            elif (num == 3):
                mathProblem = get_font(40).render(
                    "{0}*{1}".format(x, y), True, (0, 0, 0))
                block = get_font(40).render(userInput, True, (0, 0, 0))

            xRect = mathProblem.get_rect()
            rect = block.get_rect()
            # the math question being displayed
            xRect.center = (450, 280)
            # the users input is being displayed
            rect.center = (450, 475)

            DISPLAY.blit(block, rect)
            DISPLAY.blit(mathProblem, xRect)

        '''End of solveMath'''

        if playerMove >= 16:
            playerMove -= 16
        # print(playerMove)
        draw_piece(player1)
        draw_piece(player2)
        # draw_piece(player3)
        # draw_piece(player4)
        show_dice()

        if game_over != 0:
            if game_over == 1:
                DISPLAY.blit(win_image, (500, 250))
                winner_message(player_list, properties)

        pygame.display.update()

# Changing the music and sound
def setting_button():
    # initialize volume to a default value
    volume = pygame.mixer.music.get_volume()
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        draw_background("mathopoly/images/playBackground.png")

        button_rect = pygame.transform.scale(button_rect_image, (300, 80))
        VOLUME_LABEL = get_font(40).render(
            f"Volume: {int(round(volume * 100, -1))}%", True, BLACK)
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
    global dice_1, count, load_dice_image
    for i in range(10):
        dice1_image = random.choice(dice_images)
        dice1_image = pygame.transform.scale(dice1_image, (100, 100))
        DISPLAY.blit(dice1_image, (590, 320))
        pygame.display.update()
        time.sleep(0.1)

    roll1 = roll_dice()
    load_dice_image = roll1

    dice_1 = player_list[count]['position']
    print(player_list[count]['position'])
    dice_1 += roll1

    if dice_1 >= len(board):
        dice_1 = dice_1 - 16

    # Position 13
    # Rolls 6
    # Position 19
    # 19 - 16 - 1

    player_list[count]['position'] = dice_1
    playerMove = dice_1

    print(dice_1)

    print(f"Total: {dice_1}")

# End turn message that will display when the user ends their turn to notify players
def end_turn_message(player):
    font = get_font(30)
    text = font.render(
        f"End of Turn: {player['name']}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(635, 515))
    DISPLAY.blit(text, text_rect)
    draw_piece(player1)
    draw_piece(player2)
    show_dice()
    pygame.display.update()
    pygame.time.delay(1800)


# Function that shows the dice that was rolled
def show_dice():
    dice1_image = dice_images[load_dice_image-1]
    dice1_image = pygame.transform.scale(dice1_image, (100, 100))

    DISPLAY.blit(dice1_image, (590, 320))

# draws the board on the screen
def draw_board():
    background_image = pygame.image.load('mathopoly/images/board.PNG')
    background_image = pygame.transform.scale(background_image, (1000, 700))
    background_image.set_colorkey((255, 255, 255))
    DISPLAY.blit(background_image, (145, 13))

# displays the pieces for the players
def draw_piece(player):
    # DISPLAY.blit(dog_piece, (190+210, 35))
    if playerMove >= 4 and playerMove <= 11:
        print("")
    else:
        player_piece = pygame.transform.flip(player['piece'], True, False)

    DISPLAY.blit(player_piece, board[player['position']])

# creates the players who will play the game
def create_players():
    global players
    player_input = ""
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

# Function that allows users to buy properties
def buy_property(player, tile_number, properties):
    message = ""
    # If the key price is not found in properties, then the property can't be bought
    if 'price' not in properties[tile_number]:
        message = f"{properties[tile_number]['name']} square cannot be bought"
    # Else if the property has an owner in the tile, it can't be bought
    elif properties[tile_number]['owner'] != '':
        message = f"{properties[tile_number]['owner']} owns this property"
    elif properties[tile_number]['owner'] == '' and player['balance'] >= properties[tile_number]['price']:
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

# Function to create images that are clickable
def create_button(image, w, h, x, y):
    # Load and scale image
    button_image = pygame.image.load(image)
    button_image = pygame.transform.scale(button_image, (w, h))
    # Create and center button rectangle
    button_rect = button_image.get_rect()
    button_rect.center = (x, y)
    return button_image, button_rect

# function takes of buying properties
def buy_event():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")

        yes_image, yes_button = create_button(
            "mathopoly/images/giga_yes.png", 175, 100, 550, 300)
        yes_image.set_colorkey((255, 255, 255))
        no_image, no_button = create_button(
            "mathopoly/images/No.png", 200, 100, 800, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(MOUSE_POS):
                    message = buy_property(
                        player_list[count], player_list[count]['position'], properties)
                    display_message(message)
                    pygame.time.delay(1800)
                    return

                elif no_button.collidepoint(MOUSE_POS):
                    return

        DISPLAY.blit(yes_image, yes_button)
        DISPLAY.blit(no_image, no_button)
        pygame.display.update()

# this function takes care of the naming for the properties
def text_properties():
    font = pygame.font.SysFont(None, 40)
    for index in properties:
        text = font.render(properties[index]['name'], True, (0, 0, 0))
        pos = properties[index]['pos']
        DISPLAY.blit(text, pos)


def gameStatus(player_list, properties):
    global game_over, winning_player, count
    counts = {}
    for player in player_list:
        counts[player['name']] = 0
        for prop in properties.values():
            if prop['owner'] == player['name']:
                counts[player['name']] += 1

        if counts[player['name']] >= 3:
            winning_player = player['name']
            game_over = 1
            stop()
            end_music()
    print(counts)
    return counts

def properties_owned(player):
    #Create the output box for players' info
    font = get_font(20)
    counts = {}
    for player in player_list:
        counts[player['name']] = 0
        for prop in properties.values():
            if prop['owner'] == player['name']:
                counts[player['name']] += 1
 
    # creat the output box for the players property
    property_info = pygame.Rect(1150, 720/2, 230, 225)
    pygame.draw.rect(DISPLAY, pygame.Color("beige"), property_info)
    pygame.draw.rect(DISPLAY, pygame.Color("gray"), property_info, 2)
    #Display player_info
    for i, player in enumerate(counts.keys()):
        #Display property_info
        player_name_surface = font.render(player, True, pygame.Color("black"))
        DISPLAY.blit(player_name_surface, (property_info.x +
                                            5, property_info.y + 15 + i * 50))
        player_property_surface = font.render(str(counts[player]), True, pygame.Color("black"))
        DISPLAY.blit(player_property_surface, (property_info.x + 
                                            130, property_info.y + 15 + i * 50))

def winner_message(player_list, properties):
    global winning_player
    font = get_font(20)
    text = font.render(f"Winner: {winning_player}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(635, 515))
    DISPLAY.blit(text, text_rect)