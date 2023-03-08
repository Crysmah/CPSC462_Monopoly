import pygame, sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

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
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                options()
            # if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
            #     pygame.quit()
            #     sys.exit()
    pygame.display.update()

# Access to the game    
def play_button():
    return

# Changing the music and sound
def setting_button():
    return
    
# Close the application
def quit_button():
    return

def main():
    while True:
        draw_background()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

if __name__ == '__main__':
    main()
    
