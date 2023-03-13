import pygame, sys
from button import Button
from scene import *

class Game():

    pygame.init()

    def run():
        start()
        while True:
            draw_background("images/background.PNG")
            MENU_MOUSE_POS = pygame.mouse.get_pos()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                        play_button()
                    if SETTING_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                        setting_button()
                    if QUIT_BUTTON.rect.collidepoint(MENU_MOUSE_POS):
                        quit_button()

            pygame.display.update()