import pygame, sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1280, 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Screen")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

# Draw the background for the Menu Screen
def draw_background():
    background_image = pygame.image.load("images/background.PNG")
    ''' Re-size the background image'''
    background = pygame.transform.scale(background_image,(WIDTH, HEIGHT))
    DISPLAY.blit(background, (0,0))
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

#  Change color and appearance when
#  the mouse cursor interacts with them.
def update_button(button, MENU_MOUSE_POS):
    button.changeColor(MENU_MOUSE_POS)
    button.update(DISPLAY)
    
def main():
    draw_background()
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

    pygame.display.update()
    


if __name__ == '__main__':
    main()
    
