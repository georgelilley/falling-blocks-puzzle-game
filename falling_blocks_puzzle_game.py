import pygame
import sys

from settings import Settings
from grid import Grid
from button import Button
from random_shape import Random_Shape
from hero import Hero

class falling_blocks:
    """Main class of falling blocks game."""

    def __init__(self):
        """Initialise falling blocks game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        self.grid = Grid(self)
        self.button = Button(self.screen)
        self.tetrominos = []

    def run_game(self):
        while True:
            self._check_event()
            self.grid.update()
            self.update_screen()
            if self.settings.game_active == True:
                self.check_active_falling_shape()
                self.check_if_hero_moved()

    def check_active_falling_shape(self):
        if self.settings.active_falling_shape == False:
            self.hero = Hero()
            self.tetrominos.append(self.hero)
            print(self.hero.block_coordinates)
    #        self.create_new_falling_shape() # --
    #        self.grid.set_active_hero(self.hero)
            self.settings.active_falling_shape = True

    #def create_new_falling_shape(self):
    #    self.hero = Hero()
    #    self.grid.set_active_hero(self.hero)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == 256: # Click Quit Event.
                sys.exit()
            if event.type == 771: # Keyboard Key Down Event.
                if event.dict['text'] == 'q':
                    sys.exit()
            if event.type == 1025: # Mouse Click.
                self.mouse_click(event.pos)
            if self.settings.game_active == True:
                self.gameActive_check_keydown_events(event)

    def gameActive_check_keydown_events(self, event):
        if event.type == 768:
            self.IsGameKeyPressed(event)

    def IsGameKeyPressed(self, event):
        #print('active')
        key_actions = {
            pygame.K_RIGHT: self.hero.player_action.move.right, # decouple from hero - it should be player action with all the methods and then the current tetromino is used 
            pygame.K_LEFT: self.hero.player_action.move.left,
            pygame.K_DOWN: self.hero.player_action.move.down,
            pygame.K_a: self.hero.player_action.rotate.left,
            pygame.K_d: self.hero.player_action.rotate.right
        }
        action = key_actions.get(event.key)
        if action:
            self.grid.reset()
            #print('reset here')
            action()

    def check_if_hero_moved(self):
        if self.hero.player_action.move.is_any_movement_method_called():
            #print('catcher') # need to make sure this is working as intended
            #print(self.hero.block_coordinates)
            self.grid.set_active_hero(self.hero)
            self.hero.player_action.move.reset_method_called_flag()
        #if self.hero.player_action.

    def mouse_click(self, pos):
        """Check if """
        x, y = pos[0], pos[1]
        if y < 200 and self.settings.game_active == False:
            self.start_button_clicked() 
    
    def start_button_clicked(self):
        self.settings.game_active = True
        
    def update_screen(self):
        self.screen.fill((255, 255, 255))
        self.grid.draw_border(self.screen)
        self.grid.cell_images.draw(self.screen)
        #self.grid.squares.draw(self.screen)
        if self.settings.game_active == False:
            self.button.draw()# I think i need to draw a fresh screen each time
        pygame.display.flip()

if __name__ == "__main__":  
    fb = falling_blocks()
    fb.run_game()

        
