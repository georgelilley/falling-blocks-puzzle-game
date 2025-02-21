import numpy as np

def rotate_point(x, y, cx, cy, theta):
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