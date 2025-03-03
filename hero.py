import numpy as np
import copy

from settings import Settings
from rotate_point import rotate_point
from get_individual_block_xy import get_individual_block_xy

from player_action import PlayerAction

def track_method_call(method):
    def wrapper(self, *args, **kwargs):
        self._method_called = True  # Set the flag to True when any method is called
        return method(self, *args, **kwargs)
    return wrapper

class Hero:

    def __init__(self):
        self.settings = Settings()
        self._method_called = False

        self.create_shape()
        self.player_action = PlayerAction(self)

    def reset_method_called_flag(self):
        self._method_called = False
    
    def create_shape(self):

        self.block_coordinates = {
            'alpha': {
                'x': 0,
                'y': 3
                },

            'beta': {
                'x': 0,
                'y': 2
                },

            'charlie': {
                'x': 0,
                'y': 1
                },

            'delta': {
                'x': 0,
                'y': 0
                },
        }

    #def get_individual_block_xy(self, coordinates):
    #    return get_individual_block_xy(coordinates)
        
    #def is_any_movement_method_called(self):
    #    return self._method_called


        
    





    