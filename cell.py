import pygame

from cellsprite import CellSprite

class Cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False
        self.tetromino_id = False
        #self._create_cell_image()

        self.sprite = CellSprite(x, y)

    #def _create_cell_image(self, character=None):
    #    self.surface = pygame.Surface((self.settings.square_width, 
    #                                        self.settings.square_height))
    #    if character == 'Hero':
    #        cell_colour = (255, 0, 0)
    #    else:
    #        cell_colour = (255, 255, 255)
    #    grid_lines_colour = (128, 128, 128)
    #    pygame.draw.rect(self.surface, grid_lines_colour, 
    #                                (0, 0, self.settings.square_width, 
    #                                self.settings.square_height),
    #                                width=1)
    #    self.image = self.surface
    #    self.rect = pygame.Rect(0, 0, self.settings.square_width, 
    #                            self.settings.square_height)
    #    self.rect.topleft = (160 + (self.x * self.settings.square_width), 
    #                        160 + (self.y * self.settings.square_height))
        
        