import pygame
import sys

# Define colors
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Language Learning App")
FONT = pygame.font.Font(None, 32)

class InputBox:
    def __init__(self, x, y, w, h, prompt):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLUE
        self.text = ''
        self.prompt = prompt
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle the active variable.
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                result = self.text
                self.text = ''
                self.active = False
                return result
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None

    def draw(self, screen):
        # Draw prompt
        prompt_surface = FONT.render(self.prompt, True, BLACK)
        screen.blit(prompt_surface, (self.rect.x, self.rect.y - 30))
        # Draw text
        txt_surface = FONT.render(self.text, True, BLACK)
        width = max(200, txt_surface.get_width()+10)
        self.rect.w = width
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def display_message(lines, color, y_start=100):
    screen.fill(YELLOW)
    for i, line in enumerate(lines):
        msg_surface = FONT.render(line, True, color)
        screen.blit(msg_surface, (100, y_start + i * 40))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    input_boxes = [
        InputBox(300, 200, 200, 40, "What is your name?"),
        InputBox(300, 300, 200, 40, "Language to learn?"),
        InputBox(300, 400, 200, 40, "Hours per week?")
    ]
    user_data = ["", "", ""]
    current_box = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(YELLOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            result = input_boxes[current_box].handle_event(event)
            if result is not None:
                user_data[current_box] = result.strip()
                current_box += 1
                if current_box >= len(input_boxes):
                    name, language, hours = user_data
                    display_message([
                        f"Welcome {name}!",
                        f"You chose to learn {language}.",
                        f"{hours} hours/week is awesome!",
                        "Creating your personalized plan..."
                    ], GREEN)

                    if language.lower() == "spanish":
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
                    elif language.lower() == "french":
                        vocab = [
                            "bonjour - hello",
                            "l'homme - a man",
                            "la femme - a woman",
                            "le garçon - a boy",
                            "la fille - a girl",
                            "merci - thank you",
                            "s'il vous plaît - please",
                            "de rien - you're welcome",
                            "je suis désolé - sorry",
                            "au revoir - goodbye"
                        ]
                    else:
                        vocab = ["Sorry, vocabulary for this language is not available yet."]

                    display_message(["Let's learn some words!"], RED)
                    display_message(vocab, BLUE, y_start=20)
                    display_message([f"See you next time, {name}!"], GREEN)
                    running = False

        for i, box in enumerate(input_boxes):
            if i == current_box:
                box.color = GREEN
            else:
                box.color = BLUE
            box.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()