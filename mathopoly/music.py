import pygame

pygame.init()

# Set up the screen
screen_width = 400
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the music
pygame.mixer.music.load('sonic.mp3')
pygame.mixer.music.play(-1)

# Set up the initial volume
volume = 1.0
pygame.mixer.music.set_volume(volume)

# Set up the slider
slider_x = 50
slider_y = 100
slider_width = 200
slider_height = 20
slider_pos = int(volume * slider_width) + slider_x

# Set up the text
text = font.render('Volume: {:.0%}'.format(volume), True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width // 2, slider_y - 30))

# Set up the button
button_text = font.render('Save', True, (255, 255, 255))
button_rect = button_text.get_rect(center=(screen_width // 2, slider_y + slider_height + 30))

# Define a function to update the volume and pause the music
def update_volume(pos):
    global volume, text
    volume = (pos - slider_x) / slider_width
    pygame.mixer.music.set_volume(volume)
    text = font.render('Volume: {:.0%}'.format(volume), True, (255, 255, 255))

# Define a function to save the volume to a file
def save_volume():
    with open('volume.txt', 'w') as f:
        f.write(str(volume))

# Set up the game loop
running = True
dragging = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if slider_rect.collidepoint(event.pos):
                dragging = True
            elif button_rect.collidepoint(event.pos):
                save_volume()
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                slider_pos = min(max(event.pos[0], slider_x), slider_x + slider_width)
                update_volume(slider_pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the slider
    pygame.draw.rect(screen, (255, 255, 255), (slider_x, slider_y, slider_width, slider_height))
    slider_rect = pygame.draw.circle(screen, (255, 255, 255), (slider_pos, slider_y + slider_height // 2), slider_height // 2)
    
    # Draw the text
    screen.blit(text, text_rect)
    
    # Draw the button
    pygame.draw.rect(screen, (255, 0, 0), button_rect)
    screen.blit(button_text, button_rect)
    
    # Update the display
    pygame.display.update()

pygame.quit()
