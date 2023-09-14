import pygame
import time

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the width and height of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Python RPG Game")

# Load player image
player_image = pygame.image.load("player.png")

# Define player attributes
player_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
player_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Update the game screen
    window.fill(BLACK)
    window.blit(player_image, player_pos)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    time.sleep(0.02)

# Quit Pygame
pygame.quit()