import copy

from settings import Settings
from rotate_point import rotate_point

def track_method_call(method):
    def wrapper(self, *args, **kwargs):
        self._method_called = True  # Set the flag to True when any method is called
        return method(self, *args, **kwargs)
    return wrapper

class RotateShape:

    def __init__(self, hero):
        self.settings = Settings()
        self._method_called = False

        self.hero = hero
        
    def right(self):
        self._rotate(-90)
        print(self.hero.block_coordinates)

    def left(self):
        self._rotate(90)
        print(self.hero)

    def _rotate(self, degrees):
        self.calculate_rotated_coordinates(degrees)
        print(self.hero)

    @track_method_call
    def calculate_rotated_coordinates(self, angle):
        self.rotated_coordinates = {}
        self.find_center_of_rotation()
        for block, coordinates in self.hero.block_coordinates.items():
            x_value, y_value = self.hero.get_individual_block_xy(coordinates)
            rotated_x_coordinate, rotated_y_coordinate = rotate_point(x_value, y_value, self.x_average, self.y_average, angle)
            rounded_rotated_x_coordinate = round(rotated_x_coordinate)
            rounded_rotated_y_coordinate = round(rotated_y_coordinate)
            new_coordinate = {
                'x': rounded_rotated_x_coordinate,
                'y': rounded_rotated_y_coordinate
            }
            self.rotated_coordinates[block] = new_coordinate
        self.hero.block_coordinates = self.rotated_coordinates
        

    def find_center_of_rotation(self):
        self.x_positions, self.y_positions = [], []
        for block, coordinate in self.hero.block_coordinates.items():
            for axis, value in coordinate.items():
                if axis == 'x':
                    self.x_positions.append(value)
                if axis == 'y':
                    self.y_positions.append(value)
        self.x_average = round(sum(self.x_positions)/4)
        self.y_average = round(sum(self.y_positions)/4)
        return(self.x_average, self.y_average)