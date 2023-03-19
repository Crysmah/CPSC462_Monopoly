import pygame, sys
from mathopoly.button import Button

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")
background_image = pygame.image.load("mathopoly/images/background.PNG")
button_rect_image = image=pygame.image.load("mathopoly/images/Button Rect.png")


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
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        draw_background("mathopoly/images/playBackground.png")

        play_back_button = pygame.image.load("mathopoly/images/playBackButton.png")
        scaled_play_back_button = pygame.transform.scale(play_back_button, (40, 40))
        return_button = Button(scaled_play_back_button, pos=(25, 25), text_input="", font=get_font(40),
                            base_color="#d7fcd4", hovering_color="White")
        
        widget_button = pygame.image.load("mathopoly/images/widgetButton.png")
        scaled_widget_button = pygame.transform.scale(widget_button, (40, 40))
        settings = Button(scaled_widget_button, pos=(1250, 25), text_input="", font=get_font(40),
                        base_color="#d7fcd4", hovering_color="White")

        return_button.update(DISPLAY)
        settings.update(DISPLAY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.checkForInput(PLAY_MOUSE_POS):
                    return
                if settings.checkForInput(PLAY_MOUSE_POS):
                    setting_button()
                
        pygame.display.update() 

# Changing the music and sound
def setting_button():
    volume = 0.1 # initialize volume to a default value
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        draw_background("mathopoly/images/playBackground.png")

        button_rect = pygame.transform.scale(button_rect_image, (300, 80))
        VOLUME_LABEL = get_font(40).render(f"Volume: {int(volume * 100)}%", True, (255, 255, 255))
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
                    return # exit the function

        pygame.display.update()

    
# Close the application
## thinking about it
def quit_button():
    pygame.quit()
    sys.exit()

#  Change color and appearance when
#  the mouse cursor interacts with them.
def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)