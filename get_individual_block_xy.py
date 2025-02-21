def get_individual_block_xy(coordinates):
    for axis, value in coordinates.items():
        if axis == 'x':
            x_value = value
        if axis == 'y':
            y_value = value
    return x_value, y_value