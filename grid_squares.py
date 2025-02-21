import pygame

from settings import Settings

class Square(pygame.sprite.Sprite):
    """Each Square in the Grid."""

    def __init__(self, fb_game, x, y):
        """Initialise the square instance."""
        super().__init__()
        self.settings = Settings()
        self.x_group_position = x
        self.y_group_position = y
        self.default_colour = ((255, 255, 255))

        self.create_square()

    def create_square(self, hero=False):
        """
        This function creates the square. 
        A surface object containing a square is set as the image.
        Its rect attribute is set.
        These steps are important to enable the sprite group functionality.
        """
        self.create_square_surface(hero)
        self.create_rect_attribute()

    def create_square_surface(self, hero):
        """Create a surface object, draw a square and set as image."""
        self.surface = pygame.Surface((self.settings.square_width, 
                                      self.settings.square_height))
        self.set_colour(hero)

        pygame.draw.rect(self.surface, self.grid_lines_colour, 
                         (0, 0, self.settings.square_width, 
                          self.settings.square_height),
                          width=1)
        
        self.image = self.surface
        
    def set_colour(self, hero):
        if hero == False:
            self.surface.fill(self.default_colour)
        else:
            self.surface.fill((255, 0, 0))
        self.grid_lines_colour = (128, 128, 128)

    def create_rect_attribute(self):
        """
        Create the rect attribute for the square 
        This is where it will be placed in the gamespace.
        """
        self.rect = pygame.Rect(0, 0, self.settings.square_width, 
                                self.settings.square_height)
        self.rect.topleft = (160 + (self.x_group_position * self.settings.square_width), 
                            160 + (self.y_group_position * self.settings.square_height))

    def create_blank_square(self):
        self.create_square()

    def create_hero_square(self):
        self.create_square(hero=True)
