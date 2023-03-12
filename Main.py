import pygame, sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

# plays music
def start():
    """Starts the music"""
    if True:
        try:
            pygame.mixer.music.load("Soul.mp3")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1, 0.0, 500)
        except pygame.error as pygame_error:
            print(f'Cannot open {Soul.mp3}')
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
    return

# Changing the music and sound
def setting_button():
    return
    
# Close the application
## thinking about it
def quit_button():
    sys.exit()

#  Change color and appearance when
#  the mouse cursor interacts with them.
def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)
    
    sys.exit()

#  Change color and appearance when
#  the mouse cursor interacts with them.
def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)
    
def main():
    start()
    while True:
        draw_background("images/background.PNG")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        button_rect_image = image=pygame.image.load("images/Button Rect.png")
        button_rect = pygame.transform.scale(button_rect_image, (300, 80))
        PLAY_BUTTON = Button(button_rect, pos=(640, 220), text_input="PLAY", font=get_font(40),
                            base_color="#d7fcd4", hovering_color="White")
        SETTING_BUTTON = Button(button_rect, pos=(640, 350), text_input="SETTING",
                                font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(button_rect, pos=(640, 480), text_input="QUIT",
                            font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        update_button(PLAY_BUTTON, MENU_MOUSE_POS)
        update_button(SETTING_BUTTON, MENU_MOUSE_POS)
        update_button(QUIT_BUTTON, MENU_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
    
if __name__ == '__main__':
    main()

