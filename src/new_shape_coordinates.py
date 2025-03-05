import copy

from settings import Settings

class NewShapeCoordinates:

    def __init__(self, movement_str):
        self.settings = Settings()
        self.movement_str = movement_str

    def calculate(self):
        self.new_block_coordinates = copy.deepcopy(self.block_coordinates)
        for block, coordinate in self.block_coordinates.items():
            for axis, value in coordinate.items():
                switch
                if axis == 'x':
                    self.new_block_coordinates[block][axis] += 1
