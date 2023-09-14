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
player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
player_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    player_pos.x -= player_speed * keys[pygame.K_LEFT]
    player_pos.x += player_speed * keys[pygame.K_RIGHT]
    player_pos.y -= player_speed * keys[pygame.K_UP]
    player_pos.y += player_speed * keys[pygame.K_DOWN]
    
    # Clamp player position within window boundaries
    player_pos.x = max(0, min(WINDOW_WIDTH - player_image.get_width(), player_pos.x))
    player_pos.y = max(0, min(WINDOW_HEIGHT - player_image.get_height(), player_pos.y))

    # Update the game screen
    window.fill(BLACK)
    window.blit(player_image, player_pos)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()