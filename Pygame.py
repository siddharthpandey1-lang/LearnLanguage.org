import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LearnLanguage.org")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)

# Fonts
font = pygame.font.SysFont("comicsansms", 32)
small_font = pygame.font.SysFont("arial", 24)

# Input box class
class InputBox:
    def __init__(self, x, y, w, h, prompt):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLUE
        self.text = ''
        self.font = small_font
        self.active = False
        self.prompt = prompt

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None

    def draw(self, screen):
        prompt_surface = self.font.render(self.prompt, True, BLACK)
        screen.blit(prompt_surface, (self.rect.x, self.rect.y - 30))
        txt_surface = self.font.render(self.text, True, BLACK)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

# Display messages
def display_message(lines, color=BLACK, y_start=50):
    screen.fill(WHITE)
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (50, y_start + i * 40))
    pygame.display.flip()
    pygame.time.wait(2000)

# Main app logic
def main():
    input_boxes = [
        InputBox(300, 200, 200, 40, "What is your name?"),
        InputBox(300, 300, 200, 40, "Language to learn?"),
        InputBox(300, 400, 200, 40, "Hours per week?")
    ]
    user_data = []

    running = True
    while running:
        screen.fill(YELLOW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                result = box.handle_event(event)
                if result is not None:
                    user_data.append(result)

        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()

        if len(user_data) == 3:
            name, language, hours = user_data
            display_message([
                f"Welcome {name}!",
                f"You chose to learn {language}.",
                f"{hours} hours/week is awesome!",
                "Creating your personalized plan..."
            ], GREEN)

            if language.lower() == ("spanish"):
                vocab = [
                    "hola - hello",
                    "el hombre - a man",
                    "la mujer - a woman",
                    "el niño - a boy",
                    "la niña - a girl",
                    "gracias - thank you",
                    "por favor - please",
                    "de nada - you're welcome",
                    "lo siento - sorry",
                    "adiós - goodbye"
                ]
            elif language.lower() == ("french"):
                vocab = [
                    "bonjour - hello",
                    "le homme - a man",
                    "la femme - a woman",
                    "le garçon - a boy",
                    "la fille - a girl",
                    "merci - thank you",
                    "s'il vous plaît - please",
                    "de rien - you're welcome",
                    "désolé - sorry",
                    "au revoir - goodbye"
                ]
            else:
                vocab = ["Sorry, vocabulary for this language is not available yet."]

            display_message(["Let's learn some words!"], RED)
            display_message(vocab, BLUE, y_start=20)
            display_message([f"See you next time, {name}!"], GREEN)
            running = False

    pygame.quit()
    sys.exit()

main()