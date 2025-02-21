import pygame

# Initialize Pygame
pygame.init()

# Set up the surface
width, height = 200, 200  # Dimensions of the surface
surface = pygame.Surface((width, height))

# Fill the surface with a background color
surface.fill((255, 255, 255))  # White background

# Define rectangle parameters
rect_color = (255, 0, 0)  # Red color
rect_x, rect_y = 50, 50   # Top-left corner
rect_width, rect_height = 100, 100  # Rectangle dimensions

# Draw the rectangle on the surface
pygame.draw.rect(surface, rect_color, (rect_x, rect_y, rect_width, rect_height))

# Save the surface as an image
pygame.image.save(surface, "rectangle_image.png")

print("Image saved as rectangle_image.png")

# Quit Pygame (optional here, as the script is ending)
pygame.quit()
