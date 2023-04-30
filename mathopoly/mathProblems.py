import pygame
from mathopoly.scene import *
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1400 , 720
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the font for the text
FONT_SIZE = 32
FONT_COLOR = (0, 0, 0)
font = pygame.font.Font(None, FONT_SIZE)

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

background_image = pygame.image.load("mathopoly/images/background.PNG")

class MathQuiz:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        
        # Generate a math question
        self.generate_question()
        
        # Set up the text box
        self.input_box = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 32)
        self.user_answer = ""
        self.message = ""

    def generate_question(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operator = random.choice(['+', '-', '*', '/'])
        if self.operator == '+':
            self.answer = self.num1 + self.num2
        elif self.operator == '-':
            self.answer = self.num1 - self.num2
        elif self.operator == '*':
            self.answer = self.num1 * self.num2
        elif self.operator == '/':
            self.answer = self.num1 / self.num2
        self.question = f"What is {self.num1} {self.operator} {self.num2}?"

    def handle_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check the user's answer
                    try:
                        if float(self.user_answer) == self.answer:
                            self.message = "Correct!"
                        else:
                            self.message = "Incorrect."
                    except ValueError:
                        self.message = "Please enter a number."
                    
                    # Generate a new math question
                    self.generate_question()
                    self.user_answer = ""
    
                else:
                    # Add the pressed key to the user's answer
                    self.user_answer += event.unicode

    def draw(self):
        DISPLAY.blit(background_image, (0,0))
        # Draw the question
        question_text = font.render(self.question, True, FONT_COLOR)
        question_rect = question_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        DISPLAY.blit(question_text, question_rect)

        # Draw the text box
        pygame.draw.rect(DISPLAY, GRAY, self.input_box, 2)
        answer_text = font.render(self.user_answer, True, FONT_COLOR)
        answer_rect = answer_text.get_rect(center=self.input_box.center)
        DISPLAY.blit(answer_text, answer_rect)

        # Draw the message
        message_text = font.render(self.message, True, FONT_COLOR)
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        DISPLAY.blit(message_text, message_rect)
    
        
    def run(self):
        # Run the game loop
        while True:
            # Handle events
            self.handle_events()
            
            # Draw the screen
            self.draw()
            
            # Update the screen
            pygame.display.update()

            # Limit the frame rate
            pygame.time.Clock().tick(60)
