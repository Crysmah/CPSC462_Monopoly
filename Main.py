import pygame, sys
import os.path
from button import Button


pygame.init()


WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)


def start():
    """Starts the music"""
    if True:
        try:
            pygame.mixer.music.load("sonic.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 500)
        except pygame.error as pygame_error:
            print(f'Cannot open {sonic.mp3}')
            raise SystemExit(1) from pygame_error
       
def stop(self):
    """Stops the music"""
    pygame.mixer.fadeout(500)
    pygame.mixer.music.stop()


# Draw the background for the Menu Screen
# Create 3 button: Play, Setting, Quit
def draw_background():
    background_image = pygame.image.load("images/background.PNG")
    ''' Re-size the background image'''
    background = pygame.transform.scale(background_image,(WIDTH, HEIGHT))
   
    DISPLAY.blit(background, (0,0))


    SETTING_BUTTON = Button(image=pygame.image.load("images/Button Rect.png"),
                        pos=(640, 400), text_input="SETTINGS", font=get_font(40),
                        base_color="#d7fcd4", hovering_color="White")
    MENU_MOUSE_POS = pygame.mouse.get_pos()


    for button in [SETTING_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(DISPLAY)
           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
            #     play()
            if SETTING_BUTTON.checkForInput(MENU_MOUSE_POS):
                setting_button()
            # if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
            #     pygame.quit()
            #     sys.exit()
    pygame.display.update()


# Access to the game    
def play_button():
    return


# Changing the music and sound
def setting_button():
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        DISPLAY.fill("white")


        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(MENU_MOUSE_POS)
        OPTIONS_BACK.update(DISPLAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(MENU_MOUSE_POS):
                    main()

        pygame.display.update()
   
# Close the application
def quit_button():
    return

def main():
    start()
    while True:
        draw_background()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

if __name__ == '__main__':
    main()