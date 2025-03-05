import pygame

class Button:
    def __init__(self, screen):
        self.text = 'Welcome to: Falling Blocks Puzzle Game. Click to Start!'
        self.screen = screen
        self.position = (0, 0)
        self.image =  pygame.Surface((720, 160))
        self.image.fill((0, 0, 255))

    def draw(self):
        self.screen.blit(self.image, self.position)
        self.render_text()

    def render_text(self):
        myfont = pygame.font.SysFont("monospace", 20)

        # render text
        text = myfont.render(self.text, 1, (255,255,0))
        text_rect = text.get_rect(center = (360, 80))
        self.screen.blit(text, text_rect)
