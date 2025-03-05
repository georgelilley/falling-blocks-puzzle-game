import copy
import numpy as np

from settings import Settings
from get_individual_block_xy import get_individual_block_xy

class PlayerAction:

    def __init__(self, fb_game):
        self.settings = Settings
        self.fb_game = fb_game
        self.new_active_tetromino_block_coordinates = copy.deepcopy(self.fb_game.active_tetromino.block_coordinates)

    def move_right(self):
        self.new_proposed_coordinates = self._generate_new_proposed_coordinates(axis = 'x', movement_value = 1)
        self._evaluate_coordinates()

    def move_left(self):
        self.new_proposed_coordinates = self._generate_new_proposed_coordinates(axis = 'x', movement_value = -1)
        self._evaluate_coordinates()

    def move_down(self):
        self.new_proposed_coordinates = self._generate_new_proposed_coordinates(axis = 'y', movement_value = 1)
        self._evaluate_coordinates()

    def _generate_new_proposed_coordinates(self, axis, movement_value):
        for block, coordinate in self.new_active_tetromino_block_coordinates.items():
            for axi, value in coordinate.items():
                if axi == axis:
                    self.new_active_tetromino_block_coordinates[block][axi] += movement_value
        return self.new_active_tetromino_block_coordinates

    def _evaluate_coordinates(self):
        if self._check_boundaries() == True:  #and self.check_collision() == False
            self.fb_game.active_tetromino.block_coordinates = self.new_proposed_coordinates

    def _check_boundaries(self):
        for block, coordinate in self.new_active_tetromino_block_coordinates.items():
            for axis, value in coordinate.items():
                if axis == 'x':
                    if (value > 9) or (value < 0):
                        return False
                if axis == 'y':
                    if (value >= 20):
                        return False
        return True
    
    def rotate_right(self):
        self._rotate(-90)

    def rotate_left(self):
        self._rotate(90)

    def _rotate(self, degrees):
        self.new_proposed_coordinates = self._generate_new_proposed_rotation_coordinates(degrees)
        self._evaluate_coordinates() # I think the bug is that it is taking the previous stuff and putting it in - so even if false it is using the previous value
        
    def _generate_new_proposed_rotation_coordinates(self, angle):
        x_average, y_average = self._find_center_of_rotation()
        for block, coordinates in self.new_active_tetromino_block_coordinates.items():
            x_value, y_value = get_individual_block_xy(coordinates)
            rotated_x_coordinate, rotated_y_coordinate = self._rotate_point(x_value, y_value,  x_average, y_average, angle)
            rounded_rotated_x_coordinate = round(rotated_x_coordinate)
            rounded_rotated_y_coordinate = round(rotated_y_coordinate)
            new_coordinate = {
                'x': rounded_rotated_x_coordinate,
                'y': rounded_rotated_y_coordinate
            }
            self.new_active_tetromino_block_coordinates[block] = new_coordinate
        return self.new_active_tetromino_block_coordinates
        
    def _rotate_point(self, x, y, cx, cy, theta):
        # Convert angle to radians
        theta_rad = np.radians(theta)
    
        # Translate the point to the origin (center of rotation)
        x_translated = x - cx
        y_translated = y - cy
    
        # Apply the rotation matrix
        x_rot = x_translated * np.cos(theta_rad) - y_translated * np.sin(theta_rad)
        y_rot = x_translated * np.sin(theta_rad) + y_translated * np.cos(theta_rad)
    
        # Translate back to original position
        x_final = x_rot + cx
        y_final = y_rot + cy
    
        return x_final, y_final

    def _find_center_of_rotation(self):
        x_positions, y_positions = [], []
        for block, coordinate in self.new_active_tetromino_block_coordinates.items():
            for axis, value in coordinate.items():
                if axis == 'x':
                    x_positions.append(value)
                if axis == 'y':
                    y_positions.append(value)
        x_average = round(sum(x_positions)/4)
        y_average = round(sum(y_positions)/4)
        return(x_average, y_average)
