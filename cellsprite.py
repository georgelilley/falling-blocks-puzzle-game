import pygame
from settings import Settings

class CellSprite(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.settings = Settings()

        self.surface = pygame.Surface((self.settings.square_width, 
                                            self.settings.square_height))
        cell_colour = (255, 255, 255)
        self.surface.fill(cell_colour)
        self.draw_grid_lines()

        self.image = self.surface
        self.rect = pygame.Rect(0, 0, self.settings.square_width, 
                                self.settings.square_height)
        self.rect.topleft = (160 + (x * self.settings.square_width), 
                            160 + (y * self.settings.square_height))
        
    def make_hero(self):
        self.surface.fill((255, 0, 0))
        self.draw_grid_lines()

    def make_empty(self):
        self.surface.fill((255, 255, 255))
        self.draw_grid_lines()

    def draw_grid_lines(self):
        grid_lines_colour = (128, 128, 128)
        pygame.draw.rect(self.surface, grid_lines_colour, 
                                    (0, 0, self.settings.square_width, 
                                    self.settings.square_height),
                                    width=1)