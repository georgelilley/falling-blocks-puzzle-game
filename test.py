import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 400))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a line
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (200, 200))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
