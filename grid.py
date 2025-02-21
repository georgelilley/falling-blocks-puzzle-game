import pygame
from settings import Settings
from grid_squares import Square
from get_individual_block_xy import get_individual_block_xy

class Grid:

    def __init__(self, fb_game):
        """Create the grid and set game space dimensions."""
        self.screen = fb_game.screen
        self.settings = Settings()

    def initialise_squares(self):
        """Initialise the grid."""
        self.grid = {}
        self.squares = pygame.sprite.Group()
        for x in range(0, 10):
            for y in range(0, 20):
                self.grid_square = Square(self, x, y)
                self.grid[(x, y)] = self.grid_square
                self.squares.add(self.grid_square)

    def draw_border(self, game_screen):
        """
        Draws a Border around the grid this is important for uniformity as
        internal square borders have double thickness due to them being
        the border of two squares.
        """
        self.colour = (128, 128, 128)
        pygame.draw.line(game_screen, self.colour, (160, 159), (560, 159))
        pygame.draw.line(game_screen, self.colour, (159, 160), 
                         (159, self.settings.screen_height), width=1)
        pygame.draw.line(game_screen, self.colour, (560, 160), 
                         (560, self.settings.screen_height), width=1)
        pygame.draw.line(game_screen, self.colour, (160, 160), (self.settings.screen_width-160, 160))

    def get_individual_block_xy(self, coordinates):
        return get_individual_block_xy(coordinates)

    def set_active_hero(self, hero_instance):
        self.hero = hero_instance
        for block, coordinates in self.hero.block_coordinates.items():
            x_value, y_value = self.get_individual_block_xy(coordinates)
            self.grid[(x_value, y_value)].create_hero_square()
            
    def reset(self):
        for block, coordinates in self.hero.block_coordinates.items():
            x_value, y_value = self.get_individual_block_xy(coordinates)
            self.grid[(x_value, y_value)].create_blank_square()



        

