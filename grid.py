import pygame
from settings import Settings
from get_individual_block_xy import get_individual_block_xy

from cell import Cell

class Grid:

    def __init__(self, fb_game):
        """Create the grid and set game space dimensions."""
        self.screen = fb_game.screen
        self.game = fb_game
        self.settings = Settings()
        self.cells = {}
        self.cell_images = pygame.sprite.Group()
        for x in range(0, 10):
            for y in range(0, 20):
                cell_id = (x, y)
                self.cells[cell_id] = Cell(x, y)
                self.cell_images.add(self.cells[cell_id].sprite)

       
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

    def reset_cells(self):
        for x in range(0, 10):
            for y in range(0, 20):
                cell_id = (x, y)
                self.cells[cell_id].make_empty()

    def update(self):
        self.reset_cells()
        if self.game.tetrominos:
            for tetromino in self.game.tetrominos:
                for block, coordinates in tetromino.block_coordinates.items():
                    for key, value in coordinates.items():
                        if key == 'x':
                            x = value
                        if key == 'y':
                            y = value
                    self.cells[x,y].make_hero()

    #def get_individual_block_xy(self, coordinates):
    #    return get_individual_block_xy(coordinates)

    #def set_active_hero(self, hero_instance):
    #    self.hero = hero_instance
    #    for block, coordinates in self.hero.block_coordinates.items():
    #        x_value, y_value = self.get_individual_block_xy(coordinates)
    #        self.grid[(x_value, y_value)].create_hero_square()
            
    #def reset(self):
    #    for block, coordinates in self.hero.block_coordinates.items():
    #        x_value, y_value = self.get_individual_block_xy(coordinates)
    #        self.grid[(x_value, y_value)].create_blank_square()



        

