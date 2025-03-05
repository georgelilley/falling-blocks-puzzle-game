import pygame
import sys

from settings import Settings
from grid import Grid
from button import Button
from random_shape import Random_Shape
from hero import Hero
from player_action import PlayerAction

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
                if self.settings.active_falling_shape == False:
                    self.hero = Hero()
                    self.active_tetromino = self.hero
                    self.tetrominos.append(self.hero)
                    self.settings.active_falling_shape = True

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
        self.player_action = PlayerAction(self)
        key_actions = {
            pygame.K_RIGHT: self.player_action.move_right,
            pygame.K_LEFT: self.player_action.move_left,
            pygame.K_DOWN: self.player_action.move_down,
            pygame.K_a: self.player_action.rotate_left,
            pygame.K_d: self.player_action.rotate_right
        }
        action = key_actions.get(event.key)
        if action:
            action()

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
        if self.settings.game_active == False:
            self.button.draw()
        pygame.display.flip()

if __name__ == "__main__":  
    fb = falling_blocks()
    fb.run_game()

        
