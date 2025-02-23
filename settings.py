class Settings:
    """Class to manage the game settings."""

    def __init__(self):
        """Create the game state."""
        self.game_active = False
        self.active_falling_shape = False

        self.screen_width = 720
        self.screen_height = 960
        self.squares_per_row = 10
        self.squares_per_column = 20

        # Grid squares settings.
        self.square_width = int((self.screen_width-320)/self.squares_per_row)
        self.square_height = int((self.screen_height-160)/self.squares_per_column)
        #print(self.square_height)

