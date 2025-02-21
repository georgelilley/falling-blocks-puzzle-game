from settings import Settings
from move_shape import MoveShape
from rotate_shape import RotateShape

class PlayerAction:

    def __init__(self, hero):
        self.settings = Settings
        self.move = MoveShape(hero)
        self.rotate = RotateShape()


