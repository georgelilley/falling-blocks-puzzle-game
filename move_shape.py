import copy

from settings import Settings

def track_method_call(method):
    def wrapper(self, *args, **kwargs):
        self._method_called = True  # Set the flag to True when any method is called
        return method(self, *args, **kwargs)
    return wrapper

class MoveShape:

    def __init__(self, hero):
        self.settings = Settings()
        self._method_called = False

        self.hero = hero

    def right(self):
        self._move(axis = 'x', movement_value = 1)

    def left(self):
        self._move(axis = 'x', movement_value = -1)

    def down(self):
        self._move(axis = 'y', movement_value = 1)

    @track_method_call
    def _move(self, axis, movement_value):
        self._calculate_new_coordinates(axis, movement_value) 
        self._evaluate_new_position_within_bounds()
        if not self._evaluate_new_position_within_bounds():
            print('boundary')
        else:
            self.execute_move() 

    def _calculate_new_coordinates(self, axis, movement_value):
        self.new_block_coordinates = copy.deepcopy(self.hero.block_coordinates)
        for block, coordinate in self.hero.block_coordinates.items():
            for axi, value in coordinate.items():
                if axi == axis:
                    self.new_block_coordinates[block][axis] += movement_value

    def _evaluate_new_position_within_bounds(self):
        for block, coordinate in self.new_block_coordinates.items():
            for axis, value in coordinate.items():
                if axis == 'x':
                    if (value > 9) or (value < 0):
                        return False
                if axis == 'y':
                    if (value >= 20):
                        return False
            return True

    
    def execute_move(self):
        self.hero.block_coordinates = self.new_block_coordinates

    def is_any_movement_method_called(self):
        return self._method_called
    
    def reset_method_called_flag(self):
        self._method_called = False